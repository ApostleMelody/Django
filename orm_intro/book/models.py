from django.db import models
# 如果要讲一个普通的类变成一个可以映射到数据库中的ORM模型
# 那么必须要将父类设置为models.Model或者他的子类
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False,default=0)

class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)