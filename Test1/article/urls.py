from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'article'
urlpatterns = [
    path('', views.article_index, name='article_index'),
    path('article_add/', views.article_add.as_view(), name='article_add'),
    path('articlelist/', views.ArticleList.as_view(), name='articlelist'),
    path('text/', views.TextView.as_view(), name='text_index'),
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('blog/',views.Blog, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
