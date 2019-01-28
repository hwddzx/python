from django.contrib import admin
from user.models import User, UserAddress


# 对模型进行管理(管理显示结构)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'username', 'telephone', 'password', 'gender', 'birthday',
                    'school', 'location', 'hometown', 'head', 'create_time',
                    'update_time', 'is_delete']


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['id', 'user', 'username', 'phone', 'province',
                    'city', 'area', 'brief', 'is_default',
                    'create_time', 'update_time', 'is_delete']
