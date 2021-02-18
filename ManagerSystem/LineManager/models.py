from django.db import models

# Create your models here.
class LineModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    length = models.FloatField(max_length=100)
    degree = models.CharField(max_length=10)
