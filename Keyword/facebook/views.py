from django.shortcuts import render
from facebook_page_scraper import Facebook_scraper
from .utils import getFbPostList, getKeyword
from .models import Post


def getPosts(request):
    # Post.objects.all().delete()

    # page_name_beat = "Theanh28.Hanoi"
    # fb_posts_beat = getFbPostList(request, page_name_beat)

    # for post in fb_posts_beat:
    #     m1 = Post(**post)
    #     m1.save()

    # page_name_theanh = "Theanh28.Hanoi"
    # fb_posts_theanh = getFbPostList(request, page_name_theanh)

    # for post in fb_posts_theanh:
    #     m2 = Post(**post)
    #     m2.save()

    # page_name_yan = "yannews"
    # fb_posts_yan = getFbPostList(request, page_name_yan)

    # for post in fb_posts_yan:
    #     m3 = Post(**post)
    #     m3.save()

    # page_name_ttcp = "thongtinchinhphu"
    # fb_posts_ttcp = getFbPostList(request, page_name_ttcp)

    # for post in fb_posts_ttcp:
    #     m4 = Post(**post)
    #     m4.save()

    # page_name_24 = "tintucvtv24"
    # fb_posts_24 = getFbPostList(request, page_name_24)

    # for post in fb_posts_24:
    #     m5 = Post(**post)
    #     m5.save()

    posts = Post.objects.all()

    post_kw = list()
    for post in posts:
        kw_list = list()
        kw = getKeyword(request, post.content)
        for i in kw:
            kw_list.append(i[0])
        a = {
            'name': post.name,
            'keyword': kw_list
        }
        post_kw.append(a)

    context = {'posts': posts, 'keywords': post_kw}

    return render(request, 'facebook/posts.html', context)
