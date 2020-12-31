from django.db import models

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    # removed = models.BooleanField(null=True)
    removed = models.NullBooleanField()
    # longtext
    title = models.CharField(max_length=200)
    create_time = models.DateField()


