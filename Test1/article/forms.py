from django import forms
from .models import User
class ArticleForms(forms.Form):
    article_name = forms.CharField(max_length=255, label='标题', min_length=2,error_messages={"min_length":'名称太短'})
    article_context = forms.CharField(max_length=65535, label='标题', min_length=2,error_messages={"min_length":'内容太少'})

class SignUpForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=16, min_length=6)
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message='两次密码不一致')
        return cleaned_data
    class Meta:
        model = User
        fields = "__all__"



class SigninForm(forms.ModelForm):
    def get_error(self):
        new_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.values():
            for message_dicts in messages:
                for key,message in message_dicts.items():
                    if key == 'message':
                        new_errors.append(message)
        return new_errors
    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username':{
                'min_length':'用户名最小长度不少于4位'
            },
            'password': {
                'min_length': '密码最小长度不少于6位'
            }
        }