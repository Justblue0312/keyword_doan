# Keyword Extraction website
## Features
- Keyword extraction using YAKE and RẠKE algorithm
- Design as news website for entertainment.
- Collect and use data from a lot of source like Facebook, Youtube, MSN News...
- Watch the news and leave your comments

## Tech

Keyword Extraction website uses a number of open source projects to work properly:
- [Django](https://github.com/django/django) - a web framework base on Python.
- [HTML/CSS/JS]() - the streaming build system
- [Celery](https://github.com/celery/celery) - A library allow worker program perform beneath the progress
- [Redis](https://github.com/redis/redis) - A cache server for celery


## Installation

This project requires [Django]() v3.2+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd keyword_proj
python3 manage.py migrate
python3 manage.py runserver
```

For production environments...

```sh
pip install - r requriments.txt
virtualenv env
./env/Script/activate
deactivate
```

## Plugins

Project need some plugins to working out.

| Plugin | README |
| ------ | ------ |
| Django | [https://github.com/django/django] |
| Celery | [https://github.com/celery/celery] |
| Pytrends | [https://github.com/GeneralMills/pytrends] | 
| Requests | [https://github.com/psf/requests] |
| BeautifulSoup | [https://github.com/wention/BeautifulSoup4] |



