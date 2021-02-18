from django.db import models
from django.core.validators import MinLengthValidator
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    context = models.TextField(null=False,default='')
    click_number = models.IntegerField(null=False, default=0)
    thumbnail = models.FileField(upload_to="%Y/%m/%d/",null=True)
    class Meta:
        db_table = 'article'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False, validators=[MinLengthValidator(4)])
    telephone = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False, validators=[MinLengthValidator(6)])