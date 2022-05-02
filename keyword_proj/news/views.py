from ast import While
from django.shortcuts import render
from keyword_proj.const import MSN_URL, available_flag
from .utils import get_msn_content_from_url, get_msn_url_from_body_html, get_news_posts, convert_datetime
from .models import SliceNews, ArticleNews


def home(request):

    next_page_url, articles, weathers, slices = get_news_posts(MSN_URL)

    # SliceNews.objects.all().delete()
    for slice in slices:
        publish_date = slice['publishedDateTime']
        for item in slice['slides']:
            slice_obj, _ = SliceNews.objects.get_or_create(
                title=slice['title'], body_html=item['body'])
            slice_obj.title = item['title']
            slice_obj.body_html = item['body']
            slice_obj.url = get_msn_url_from_body_html(item['body'])
            slice_obj.image_url = item['image'].get('url', '')
            slice_obj.image_name = item['image'].get('title', '')
            slice_obj.image_caption = item['image'].get('caption', '')
            slice_obj.attribution = item['image'].get('attribution', '')
            slice_obj.source = item['image'].get('source', '')
            slice_obj.publish_date = convert_datetime(publish_date)
            slice_obj.save()

    lastSeenId = str('inf')
    slice_rows = SliceNews.objects.all().order_by('title')
    for row in slice_rows:
        if row.title == lastSeenId:
            row.delete()
        else:
            lastSeenId = row.title

    # ArticleNews.objects.all().delete()
    for article in articles:
        article_obj, _ = ArticleNews.objects.get_or_create(
            title=article['title'])
        article_obj.title = article['title']
        article_obj.abstract = article['abstract']
        article_obj.url = article['url']
        article_obj.publish_date = convert_datetime(
            article['publishedDateTime'])
        article_obj.content = get_msn_content_from_url(article['url'])
        article_obj.image_url = article['images'][0]['url']
        article_obj.attribution = article['images'][0]['attribution']
        article_obj.image_name = article['images'][0]['title']
        article_obj.image_caption = article['images'][0]['caption'] if article['images'][0].get(
            'caption') else ''
        article_obj.source = article['images'][0]['source']
        article_obj.reaction_count = article['reactionSummary']['totalCount']
        article_obj.save()

    lastSeenId = str('inf')
    article_rows = ArticleNews.objects.all().order_by('title')
    for row in article_rows:
        if row.title == lastSeenId:
            row.delete()
        else:
            lastSeenId = row.title

    slice_object = SliceNews.objects.order_by('publish_date')[:10]
    article_object = ArticleNews.objects.order_by('publish_date')[:10]

    context = {'slices': slice_object, 'articles': article_object}
    return render(request, 'news/home.html', context)


def getArticleNews(request, pk):
    artist_obj = ArticleNews.objects.get(id=pk)
    context = {'article': artist_obj}
    return render(request, 'news/single_article_news.html', context)
