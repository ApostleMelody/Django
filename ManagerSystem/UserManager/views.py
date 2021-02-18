from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm, SignInForm
from django.contrib import messages
from .models import UserModel
class signin(View):
    def get(self, request):
        return render(request, 'signin.html')
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            print('账户登录表单验证成功')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = UserModel.objects.filter(username=username, password=password).first()
            if user:
                request.session['username'] = username

                return redirect(reverse('LineManager:index'))
            else:
                messages.info(request,'用户名或密码错误！')
                return redirect(reverse('UserManager:signin'))


class signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data.get('pwd1')
            user.save()
            messages.info(request, '注册成功')
            return redirect(reverse('LineManager:index'))
        else:
            errors = form.get_errors()
            print(errors)
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('UserManager:signup'))