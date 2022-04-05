from django.shortcuts import render
from .utils import get_category_news_link, get_news_posts, get_post_info
from .models import NewsPost


def getNewsPosts(request):
    # url = 'https://vnexpress.net/'
    # cate_links = get_category_news_link(url)
    # hot_news = get_news_posts(cate_links)
    # post_info = get_post_info(hot_news)

    # NewsPost.objects.all().delete()
    # for post in post_info:
    #     m = NewsPost(**post)
    #     m.save()

    posts = NewsPost.objects.all()

    context = {'news_posts': posts}
    return render(request, 'vnexpress/news_posts.html', context)
