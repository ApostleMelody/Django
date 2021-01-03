from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField('Article',related_name='tags')


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField('Article')
    # category = models.ForeignKey('Category',on_delete=models.PROTECT)
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    # category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, null=True,default=Category.objects.get(id=3))
    # category = models.ForeignKey('Category', on_delete=models.SET(Category.objects.get(id=3)), null=True)
    # category = models.ForeignKey('Category', on_delete=models.SET(Category.objects.get(id=4)), null=True,related_name="articles")
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_name='articles')
    author = models.ForeignKey('frontuser.FrontUser',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id,self.title)

class Comment(models.Model):
    content = models.TextField()
    # 引用自身
    origin_comment = models.ForeignKey('self',on_delete=models.CASCADE)



