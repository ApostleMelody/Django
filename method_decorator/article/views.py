from django.shortcuts import render
from .models import Article
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET
from django.http import HttpResponse

@require_http_methods(['GET'])
def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',context={"articles":articles})


@require_http_methods(['POST','GET'])
def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return HttpResponse('success')

from django.shortcuts import reverse,redirect
    # 如果有username参数，则默认登陆
def signup(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse('首页')
    else:
        return redirect(reverse('add_article'))
