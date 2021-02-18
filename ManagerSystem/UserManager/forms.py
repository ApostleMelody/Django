from django import forms
from .models import UserModel
class BaseForm(forms.ModelForm):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = []
        for messages in errors.values():
            for message_dicts in messages:
                for key, message in message_dicts.items():
                    if key == 'message':
                        new_errors.append(message)
        return new_errors

class RegisterForm(BaseForm):
    pwd1 = forms.CharField(max_length=16, min_length=6, required=True, error_messages={'min_length': '密码长度最少为6！', })
    pwd2 = forms.CharField(max_length=16, min_length=6, required=True, error_messages={'min_length': '密码长度最少为6！', })
    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        exists = UserModel.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError('该用户已存在')
        else:
            return username


    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        print(pwd1, pwd2)
        if pwd1 != pwd2:
            print('两次密码输入不一致')
            raise forms.ValidationError('两次密码输入不一致')
        return cleaned_data

    class Meta:
        model = UserModel
        exclude = ['password']

class SignInForm(BaseForm):
    class Meta:
        model = UserModel
        fields = "__all__"