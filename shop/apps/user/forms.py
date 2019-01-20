from django import forms
from django.core.validators import RegexValidator

from user import set_password
from user.models import User


# 注册form
class UsersForm(forms.Form):
    telephone = forms.CharField(max_length=11,
                                min_length=11,
                                error_messages={
                                    "required": "手机号不能为空",
                                },
                                validators=[
                                    RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误!')
                                ])
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   "required": "密码不能为空",
                                   "max_length": "密码最多设置16个字符",
                                   "min_length": "密码至少需要6个字符"
                               })
    repassword = forms.CharField(max_length=16,
                                 min_length=6,
                                 error_messages={
                                     "required": "密码不能为空",
                                     "max_length": "密码最多设置16个字符",
                                     "min_length": "密码至少需要6个字符"
                                 })

    def clean_telephone(self):  # 验证手机号是否存在
        telephone = self.cleaned_data.get('telephone')
        flag = User.objects.filter(telephone=telephone).exists()
        if flag:
            # 已存在
            raise forms.ValidationError("该手机号已注册")
        else:
            return telephone

    def clean(self):
        # 获取两次输入的密码
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password != repassword:
            raise forms.ValidationError({"repassword": "两次输入的密码不一致"})
        return self.cleaned_data


# 登陆form
class LoginForm(forms.Form):
    telephone = forms.CharField(max_length=11,
                                min_length=11,
                                error_messages={
                                    "required": "手机号不能为空",
                                    "max_length": "手机号长度是11位",
                                    "min_length": "手机号长度是11位"
                                })
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   "required": "登录密码不能为空",
                                   "max_length": "账号或密码错误",
                                   "min_length": "账号或密码错误"
                               })

    # 判断用户名和密码
    def clean(self):
        # 获取用户输入的手机号
        telephone = self.cleaned_data.get('telephone')
        # 查询数据库
        try:
            user = User.objects.get(telephone=telephone)
        except User.DoesNotExist:
            raise forms.ValidationError({'telephone': '手机号不存在'})
        # 验证密码
        password = self.cleaned_data.get('password', '')
        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误'})
        # 返回所有清洗后的数据
        self.cleaned_data['user'] = user
        return self.cleaned_data
