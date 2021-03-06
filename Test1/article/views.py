from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Articles
from django.views.generic import ListView
from .forms import ArticleForms
from django.contrib import messages


class article_add(View):
    def get(self,request,*args,**kwargs):
        form = ArticleForms()
        return render(request,'article_add.html')


    def post(self,request,*args,**kwargs):
        form = ArticleForms(request.POST)
        if form.is_valid():
            article_name = form.cleaned_data.get('article_name')
            article_context = form.cleaned_data.get('article_context')
            file = request.FILES.get('myfile')
            if not file:
                return HttpResponse('文件不存在')
            Articles.objects.create(name=article_name,context=article_context, thumbnail=file)
            return HttpResponse('提交成功！')
        else:
            print(form.errors)
            return HttpResponse("提交失败，内容不符合要求%s" % form.errors)
def article_index(request):
    articles = Articles.objects.all()
    context = {'articles':articles}
    return render(request,'article_index.html',context=context)


class ArticleList(ListView):
    model = Articles  # 用在哪个模块
    template_name = 'article_list.html' # 渲染用哪个模板
    paginate_by = 5  # 一页多少条数据
    context_object_name = 'articles' # 上下文名字
    ordering = 'click_number' # 排序字段
    page_kwarg = 'page' # 翻页的参数名字

    def get_context_data(self, **kwargs): # 给模板传输上下文
        # 调用父类方法
        context = super(ArticleList, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')

        # print(context)
        return context

    def get_queryset(self): # 默认全部返回Article.objects.all()
        # 可以用来把标记为删除的文章过滤掉
        return Articles.objects.filter(id__lte=89)

    def get_paginator_data(self,paginator,page_obj,around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages
        left_has_more = False
        right_has_more = False
        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_pages = range(current_page - around.count, current_page)
            left_has_more = True
        if current_page >= paginator.num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_pages = range(current_page + 1, current_page + around_count + 1)
            right_has_more = True
        return {'left_pages': left_pages, 'right_pages': right_pages, 'current_page': current_page,
                'left_has_more': left_has_more, 'right_has_more': right_has_more}

class TextView(View):
    def get(self,request):
        # 已经做好context上下文处理器，则会自动执行
        # user_id = request.session.get('user_id')
        # # print(user_id)
        # context = {}
        # try:
        #     user = User.objects.get(pk=user_id)
        #     # print('找到了用户存在的证据')
        #     context['front_user'] = user
        # except:
        #     pass
        return render(request,'text.html')

from .forms import SigninForm
from .models import User
class SignIn(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self,request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('article:text_index'))
            else:
                messages.info(request,'用户名或密码错误！')
                return redirect(reverse('article:signin'))
        else:
            errors = form.get_error()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('article:signin'))

from .forms import SignUpForm
from django.shortcuts import redirect,reverse

class SignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('article:text_index'))
        else:
            errors = form.errors.get_json_data()
            print(errors)
            return redirect(reverse('article:signup'))

def Blog(request):
    return render(request, 'blog.html')