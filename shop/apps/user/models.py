from django.db import models


# 用户表
class User(models.Model):
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '保密')
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    username = models.CharField(max_length=20, null=True, verbose_name='用户名')
    telephone = models.CharField(max_length=11,
                                 verbose_name='手机号码'
                                 )
    password = models.CharField(max_length=32, verbose_name='密码')
    gender = models.SmallIntegerField(choices=gender_choices, default=3, verbose_name='性别')
    birthday = models.DateField(null=True, verbose_name='生日')
    school = models.CharField(null=True, max_length=50, verbose_name='学校')
    location = models.CharField(null=True, max_length=100, verbose_name='地址')
    hometown = models.CharField(null=True, max_length=100, verbose_name='故乡')

    class Meta:
        # 设置表名
        db_table = "user"
        # 后台管理
        verbose_name = "用户表"

    def __str__(self):
        return self.telephone
