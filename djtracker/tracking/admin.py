from django.contrib import admin

from .models import Paper, Story

class PaperAdmin(admin.ModelAdmin):
    list_display = ['name', 'handle']

class StoryAdmin(admin.ModelAdmin):
    list_display = ['headline', 'date', 'has_data']

admin.site.register(Paper, PaperAdmin)
admin.site.register(Story, StoryAdmin)
