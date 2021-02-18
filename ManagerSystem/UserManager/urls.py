from django.urls import path
from . import views
app_name = 'UserManager'
urlpatterns = [

    path('signup/', views.signup.as_view(), name='signup'),
    path('signin/', views.signin.as_view(), name='signin')
]