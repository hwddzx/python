from django.db import models


# 用户表
class User(models.Model):
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '保密')
    )
    create_time = models.DateTimeField(auto_now_add=True)  # 注册时间
    update_time = models.DateTimeField(auto_now=True)  # 更新时间
    is_delete = models.BooleanField(default=False)  # 是否删除
    username = models.CharField(max_length=20, null=True)  # 用户名
    telephone = models.CharField(max_length=11)  # 手机号
    password = models.CharField(max_length=32)  # 密码
    gender = models.SmallIntegerField(choices=gender_choices, default=3)  # 性别
    birthday = models.DateTimeField(null=True)  # 生日
    school = models.CharField(null=True, max_length=50)  # 学校
    location = models.CharField(null=True, max_length=100)  # 地址
    hometown = models.CharField(null=True, max_length=100)  # 故乡

    class Meta:
        # 设置表名
        db_table = "user"
        # 后台管理
        verbose_name = "用户表"

    def __str__(self):
        return self.telephone
