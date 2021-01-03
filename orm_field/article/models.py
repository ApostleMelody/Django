from django.db import models
from datetime import datetime
from django.utils.timezone import  now
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    # removed = models.BooleanField(null=True)
    removed = models.NullBooleanField()
    # longtext
    title = models.CharField(max_length=200)
    # auto_now_add 第一次添加数据获取的时间
    # auto_now 调用save更新数据
    # create_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(auto_now=True)
class Person(models.Model):
    email = models.EmailField()

class Author(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField(null=True,db_column='author_age')
    create_time = models.DateTimeField(default=now)
    telephone = models.CharField(max_length=11,unique=True,null=True)
    def __str__(self):
        return "<（Author id:%s,create_time:%s)>" % (self.id,self.create_time)
    class Meta:
        db_table='author'
        ordering = ['-create_time','id']