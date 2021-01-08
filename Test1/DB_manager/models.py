from django.db import models

class Line(models.Model):
    name = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    length = models.FloatField()
    class Meta:
        db_table = 'line'