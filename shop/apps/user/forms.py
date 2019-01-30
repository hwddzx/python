from django import forms
from django.core.validators import RegexValidator
from django_redis import get_redis_connection

from user import set_password
from user.models import User, UserAddress


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
    # 验证码
    captcha = forms.CharField(max_length=6,
                              error_messages={
                                  "required": "验证码不能为空"
                              })

    # 用户协议
    agree = forms.BooleanField(error_messages={'required': '必须同意用户协议'})

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
        # 验证用户传入验证码和redis中的是否一样
        # 获取用户传入的验证码
        try:
            captcha = self.cleaned_data.get('captcha')
            telephone = self.cleaned_data.get('telephone', '')
            # 获取redis中的
            r = get_redis_connection()
            random_code = r.get(telephone)  # 二进制,转码
            random_code = random_code.decode('utf-8')
            if captcha and captcha != random_code:
                raise forms.ValidationError({"captcha": "验证码输入错误"})
        except:
            raise forms.ValidationError({"captcha": "验证码输入错误"})
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


# 个人资料form
class InforForm(forms.Form):
    username = forms.CharField(max_length=20,
                               error_messages={"required": "昵称不能为空",
                                               "max_length": "昵称最多设置20个字符"
                                               })
    telephone = forms.CharField(max_length=11,
                                min_length=11,
                                error_messages={
                                    "required": "手机号不能为空",
                                },
                                validators=[
                                    RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误!')
                                ])

    # def clean_telephone(self):  # 验证手机号是否存在
    #     telephone = self.cleaned_data.get('telephone')
    #     flag = User.objects.filter(telephone=telephone).exists()
    #     if flag:
    #         # 已存在
    #         raise forms.ValidationError("该手机号已存在")
    #     else:
    #         return telephone


# 修改密码form
class PasswordForm(forms.Form):
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
                                   "required": "密码不能为空",
                                   "max_length": "密码最多设置16个字符",
                                   "min_length": "密码至少需要6个字符"
                               })
    password1 = forms.CharField(max_length=16,
                                min_length=6,
                                error_messages={
                                    "required": "密码不能为空",
                                    "max_length": "密码最多设置16个字符",
                                    "min_length": "密码至少需要6个字符"
                                })
    password2 = forms.CharField(max_length=16,
                                min_length=6,
                                error_messages={
                                    "required": "密码不能为空",
                                    "max_length": "密码最多设置16个字符",
                                    "min_length": "密码至少需要6个字符"
                                })

    def clean(self):
        # 判断旧密码是否正确
        # 获取手机号和旧密码
        telephone = self.cleaned_data.get('telephone')
        password = self.cleaned_data.get('password', "")
        # 查询数据库
        user = User.objects.get(telephone=telephone)
        # 验证密码
        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误'})

        # 判断两次输入的新密码是否一致
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError({"password2": "两次输入的密码不一致"})
        # 返回所有清洗后的数据
        return self.cleaned_data


# 收货地址form
class AddressForm(forms.Form):
    hcity = forms.CharField(error_messages={"required": "地区选择不能为空"})
    hproper = forms.CharField(error_messages={"required": "地区选择不能为空"})
    harea = forms.CharField(error_messages={"required": "地区选择不能为空"})
    brief = forms.CharField(max_length=100,
                            error_messages={
                                "required": "详细地址不能为空",
                                "max_length": "地址长度过长"
                            })
    username = forms.CharField(max_length=100,
                               error_messages={
                                   "required": "收货人不能为空",
                                   "max_length": "长度过长"
                               })
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            error_messages={
                                "required": "电话号码不能为空",
                                "max_length": "电话号码格式错误",
                                "min_length": "电话号码格式错误"
                            },
                            validators=[
                                RegexValidator(r'^1[3-9]\d{9}$', '电话号码格式错误')
                            ])
    is_default = forms.BooleanField(required=False)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     count = UserAddress.objects.filter(user_id=self.data.get('user_id')).count()
    #     if count >= 6:
    #         raise forms.ValidationError({'hcity': '收货地址最多保存6条'})
    #     return cleaned_data
