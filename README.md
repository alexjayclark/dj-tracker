# Who's writing about data?
A Django app for tracking whether British broadsheets are publishing data stories.

The app uses the Twitter api to gather tweets from the timelines of The Telegraph as well as BBC News, The Guardian and The Times.

It then scrapes stories - including headline and opening paragraphs - before searching for the word 'data' and flagging if found.

The app then displays counts of these flagged stories and displays them in a table.
