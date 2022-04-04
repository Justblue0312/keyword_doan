import requests
from bs4 import BeautifulSoup


def getVietNamYoutubeTrends(request):
    url = 'https://kworb.net/youtube/trending/vn.html'
    req = requests.get(url)

    soup = BeautifulSoup(req.content, 'html.parser')

    trend_card = soup.find_all('tr')

    overall_vid = trend_card[1:51]
    music_vid = trend_card[52:]
    stt = 0

    trend_vid_list = list()
    for vid in overall_vid:
        vid_con = vid.find_all('td')
        vid_name = vid_con[2].find('a').text
        vid_link = vid_con[2].find('a').get('href')

        stt += 1
        vid_dict = {
            'pos': stt,
            'vid_name': vid_name,
            'vid_link': vid_link
        }

        trend_vid_list.append(vid_dict)

    stt1 = 0
    overall_vid_list = list()
    for vid in music_vid:
        vid_con = vid.find_all('td')
        vid_name = vid_con[2].find('a').text
        vid_link = vid_con[2].find('a').get('href')

        stt1 += 1
        vid_dict = {
            'pos': stt1,
            'vid_name': vid_name,
            'vid_link': vid_link
        }

        overall_vid_list.append(vid_dict)

    return trend_vid_list, overall_vid_list
