from django import forms

class ArticleForms(forms.Form):
    article_name = forms.CharField(max_length=255, label='标题', min_length=2,error_messages={"min_length":'名称太短'})
    article_context = forms.CharField(max_length=65535, label='标题', min_length=2,error_messages={"min_length":'内容太少'})
