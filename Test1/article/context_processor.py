from .models import User

def front_user(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:

            user = User.objects.get(pk=user_id)
            print('获取到了session并进行上下文传递')
            context['front_user'] = user
        except:
            pass
    return context