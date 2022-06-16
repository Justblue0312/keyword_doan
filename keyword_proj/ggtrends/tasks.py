from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep
from .models import TrendHotPosts
from .utils import get_trend_search


@shared_task
def checking_post_db():
    for title in TrendHotPosts.objects.values_list('title', flat=True).distinct():
        TrendHotPosts.objects.filter(pk__in=TrendHotPosts.objects.filter(
            title=title).values_list('id', flat=True)[1:]).delete()


@shared_task
def get_post_from_title():
    print('Starting to get data...')
    trendposts = get_trend_search()

    for post in trendposts:
        print(post)
        trendpost_obj = TrendHotPosts(**post)
        trendpost_obj.save()
        print('Saved')
        print('Checking database...')
        checking_post_db()
        print('Checking progess completed!!!')

        sleep(20)


get_post_from_title()
