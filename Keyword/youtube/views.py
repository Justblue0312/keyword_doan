from django.http import HttpResponse
from django.shortcuts import render
from .models import VietNamMusicVideo, VietNamTrendVideo
from .utils import getVietNamYoutubeTrends


def getTopYtVideo(request):
    VietNamTrendVideo.objects.all().delete()
    VietNamMusicVideo.objects.all().delete()

    trend_vids, music_vids = getVietNamYoutubeTrends(request)
    for vid in trend_vids:
        m1 = VietNamTrendVideo(**vid)
        m1.save()

    for vid in music_vids:
        m2 = VietNamMusicVideo(**vid)
        m2.save()

    trend_vid_obj = VietNamTrendVideo.objects.all()
    music_vid_obj = VietNamMusicVideo.objects.all()

    context = {'trend_vid': trend_vid_obj, 'music_vid': music_vid_obj}
    return render(request, 'youtube/vid.html', context)
