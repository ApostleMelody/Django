from django.urls import path
from . import views
app_name = 'LineManager'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('add', views.add.as_view(), name='add')
]