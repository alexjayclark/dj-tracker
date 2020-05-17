from django.shortcuts import render
from django.http import HttpResponse
from .models import Paper, Story
import datetime

def index(request):
    prev = (datetime.datetime.now() - datetime.timedelta(days=6)).date()
    telegraph = Paper.objects.get(name='The Telegraph')
    total = telegraph.story_set.filter(has_data=True, date__gte=prev).count()
    stories = Story.objects.filter(has_data=True, date__gte=prev).order_by('-date')
    bbc_total = Paper.objects.get(name='BBC News').story_set.filter(has_data=True, date__gte=prev).count()
    g_total = Paper.objects.get(name='The Guardian').story_set.filter(has_data=True, date__gte=prev).count()
    tt_total = Paper.objects.get(name='The Times').story_set.filter(has_data=True, date__gte=prev).count()

    context = {'total': total,
    'stories': stories,
    'bbc_total': bbc_total,
    'g_total': g_total,
    'tt_total': tt_total}

    return render(request, 'tracking/index.html', context)
