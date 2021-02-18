from django import forms
from .models import LineModel
# 用来提取错误信息
class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = []
        for messages in errors.values():
            for message_dicts in messages:
                for key, message in message_dicts.items():
                    if key == 'message':
                        new_errors.append(message)
        return new_errors

# 线路表单
class LineForm(BaseForm):
    name = forms.CharField(max_length=50, label='name', min_length=1, error_messages={'min_length':'最少输入一个字！', 'required': '线路名称不能为空'})
    length = forms.FloatField(max_value=5000,label='length', error_messages={'max_value':'最长长度不能超过5000公里。', 'required': '线路长度不能为空'})
    degree = forms.CharField(min_length=1, label='degree')
    degree_list = ['330kV', '110kV', '220kV', '35kV', '750kV']
    # class Meta:
    #     Model = Line
    #     fields = ['name', ]
    #     error_messages = {
    #         'name' : {'required':'线路名称不能为空'},
    #     }
    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        exists = LineModel.objects.filter(name=name).exists()
        if exists:
            raise forms.ValidationError('该线路已存在')
        else:
            return name
    def clean_degree(self):
        cleaned_data = super().clean()
        degree = cleaned_data.get('degree')
        if degree in self.degree_list:
            return degree
        else:
            raise forms.ValidationError(message='别想用前端突破电压等级校验')


