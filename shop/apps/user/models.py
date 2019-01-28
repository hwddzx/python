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
    username = models.CharField(max_length=20, null=True, default="", verbose_name='用户名')
    telephone = models.CharField(max_length=11,
                                 verbose_name='手机号码'
                                 )
    password = models.CharField(max_length=32, verbose_name='密码')
    gender = models.SmallIntegerField(choices=gender_choices, default=3, verbose_name='性别')
    birthday = models.DateField(null=True, default="2000-01-01", verbose_name='生日')
    school = models.CharField(null=True, default="", max_length=50, verbose_name='学校')
    location = models.CharField(null=True, default="", max_length=100, verbose_name='地址')
    hometown = models.CharField(null=True, default="", max_length=100, verbose_name='故乡')
    head = models.ImageField(upload_to='head/%Y%m/%d', default='head/contactqq.png', verbose_name='头像')

    class Meta:
        # 设置表名
        db_table = "user"
        # 后台管理
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.telephone


# 收货地址
class UserAddress(models.Model):
    user = models.ForeignKey(to='User', verbose_name='创建人')
    username = models.CharField(verbose_name='收货人', max_length=100)
    phone = models.CharField(verbose_name='电话号码', max_length=11)
    province = models.CharField(verbose_name='省份', max_length=20)
    city = models.CharField(verbose_name='市', max_length=20)
    area = models.CharField(verbose_name='区', max_length=20)
    brief = models.CharField(verbose_name='详情地址', max_length=255)
    is_default = models.BooleanField(verbose_name="是否设置为默认", default=False, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name_plural = '收货地址管理'

    def __str__(self):
        return self.username
