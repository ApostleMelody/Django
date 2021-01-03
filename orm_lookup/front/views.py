from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime
from django.utils.timezone import make_aware
def index(request):
    # article = Article.objects.filter(id__exact=1)
    # article = Article.objects.filter(id=1)
    # article = Article.objects.filter(title__exact='hello world')
    article = Article.objects.filter(title__iexact='hello world')
    print(article)
    print(article.query)
    return HttpResponse('success')

def index1(request):
    # get 没有query
    article = Article.objects.filter(pk=1)
    print(article.query)
    return HttpResponse("S")

def index2(request):
    result = Article.objects.filter(title__icontains='hello')
    print(result.query)
    print(result)
    return HttpResponse("S")

def index3(request):
    articles = Article.objects.filter(id__in=[1,2,3])
    for i in articles:
        print(i)
    return HttpResponse('SS')

def index4(request):
    # 查找 id1,2,3文章的分类
    # categories = Category.objects.filter(article__id__in=[1,2,3])
    # categories = Category.objects.filter(article__in=[1, 2, 3])
    # categories = Category.objects.filter(articles__in=[1, 2, 3])
    # for i in categories:
    #     print(i)

    articles = Article.objects.filter(title__icontains='hello')
    categories = Category.objects.filter(articles__in=articles)
    for i in categories:
        print(i)
    print(categories.query)
    return HttpResponse("13")

def index5(request):
    articles = Article.objects.filter(id__gte=2)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse('success')

def index6(request):
    articles = Article.objects.filter(title__startswith='hello')
    print(articles.query)
    print(articles)
    return HttpResponse('开始')

def index7(request):
    start_time = make_aware(datetime(year=2016,month=4,day=4,hour=19,minute=0,second=0))
    end_time = make_aware(datetime(year=2022, month=4, day=4, hour=19, minute=0, second=0))
    articles = Article.objects.filter(create_time__range=(start_time,end_time))
    print(articles.query)
    print(articles)
    return HttpResponse('index7')