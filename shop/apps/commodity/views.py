from django.shortcuts import render
from user.helps import check_login


# 商品详情
@check_login
def detail(request):
    return render(request, 'commodity/detail.html')


# 首页
@check_login
def index(request):
    return render(request, 'commodity/index.html')


# 消息中心
@check_login
def tidings(request):
    return render(request, 'commodity/tidings.html')


# 充值
@check_login
def recharge(request):
    return render(request, 'commodity/recharge.html')


# 零食飞速
@check_login
def speed(request):
    return render(request, 'commodity/speed.html')


# 店铺详情
@check_login
def list_detail(request):
    return render(request, 'commodity/list.html')


# 选择城市
@check_login
def city(request):
    return render(request, 'commodity/city.html')


# 超市
@check_login
def category(request):
    return render(request, 'commodity/category.html')


# 校区选择
@check_login
def village(request):
    return render(request, 'commodity/village.html')
