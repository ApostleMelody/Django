from .models import UserModel
from django.shortcuts import redirect, reverse, render
def UserStatus(request):
    username= request.session.get('username')
    print(username)
    context = {}
    if username:
        try:
            user = UserModel.objects.get(username=username)
            print('获取到了session并进行上下文传递')
            context['userstatus'] = user
        except:
            pass

    return context