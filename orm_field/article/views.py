from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.utils.timezone import  now,localtime
def index(request):
    # article = Article(removed=False)
    # article.save()
    # article = Article()
    # article.save()
    # import pytz
    # from datetime import datetime
    # now = datetime.now()
    # utc_timezone = pytz.timezone("UTC")
    # utc_now = now.astimezone(utc_timezone)
    # print(utc_now)

    # article = Article(title='abc',create_time=now())
    # article.save()

    article = Article.objects.get(pk=1)
    create_time = article.create_time
    print('='*3)
    print(create_time)

    print(localtime(create_time))
    print('=' * 3)
    return HttpResponse("success")
