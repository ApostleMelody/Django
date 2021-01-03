from django.shortcuts import render
from .models import Category,Article,Tag
from django.http import HttpResponse
from frontuser.models import FrontUser,UserExtension
def index(request):
    # category = Category(name='最新文章')
    # category.save()
    # article = Article(title='abc',content='111')
    # article.category = category
    # article.save()

    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse('Success')
def delete_view(request):
    category = Category.objects.get(pk=2)
    category.delete()
    return HttpResponse('delete success')

def one_to_many_view(request):
    # 1、一对多关联操作
    # article = Article(title='钢铁是怎样炼成的',content='abc')
    # category = Category.objects.first()
    # author = FrontUser.objects.get(pk=4)
    # article.category = category
    # article.author = author
    # article.save()
    # return HttpResponse('success')

    # 2、获取某个分类下所有文章
    # category = Category.objects.get(pk=3)
    # # relatedmanager
    # article = category.articles.all()
    # for i in article:
    #     print(i)

    category = Category.objects.first()
    article = Article(title='111',content='222')
    article.author = FrontUser.objects.first()
    # article.save()

    category.articles.add(article,bulk=False)

    # category.save()
    return HttpResponse('success')

def one_to_one_view(request):
    # user = FrontUser.objects.get(pk=4)
    # extension = UserExtension(school='sdu')
    # extension.user = user
    # extension.save()

    # extension = UserExtension.objects.first()
    # print(extension.user)
    # 一对一反向拿数据
    user = FrontUser.objects.first()
    print(user.extension)
    return HttpResponse('Success')

def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name='冷门文章')
    # tag.save()
    # # 多对多没有bulk参数
    # article.tag_set.add(tag)

    # 对某个标签添加一篇文章
    # tag = Tag.objects.get(pk=1)
    # article = Article.objects.get(pk=3)
    # tag.articles.add(article)

    article = Article.objects.get(pk=2)
    tags = article.tags.all()
    for tag in tags:
        print(tag)

    return HttpResponse("Success")