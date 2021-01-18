from django.urls import path
from . import views
app_name = 'DB_manager'
urlpatterns = [
    path('',views.index,name='line_index'),
    path('add/',views.add,name='line_add'),
    path('csv_download/',views.csv_download,name='csv_download'),
]