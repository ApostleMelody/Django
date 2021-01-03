from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .models import Person,Author
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

    #
    # print(localtime(create_time))
    # print('=' * 3)

    # article = Article(title='aaa', create_time=now())
    # article.save()

    # article = Article.objects.get(pk=10)
    # create_time = article.create_time
    #
    #
    # artile = Article(title='cde')
    # artile.save()

    artile1 = Article.objects.get(pk=3)
    artile1.title = '111'
    artile1.save()
    return HttpResponse("success")
    # return render(request,'index.html',context={"create_time":create_time})

def email_view(request):
    p = Person(email='xxx@qq.com')
    p.save()
    return HttpResponse("Hello")

def null_text_field_view(request):
    author = Author(username='')
    author.save()
    return HttpResponse("success")


def unique_view(request):
    author = Author(username='aaa',telephone='111')
    author.save()
    return HttpResponse("S")

def order_view(request):
    authors = Author.objects.all()
    for author in authors:
        print(author)
    return HttpResponse("成功")