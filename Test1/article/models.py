from django.db import models
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    context = models.TextField(null=False,default='')
    click_number = models.IntegerField(null=False, default=0)
    class Meta:
        db_table = 'article'
