from django.shortcuts import render


# 商品详情
def detail(request):
    return render(request, 'commodity/detail.html')


# 首页
def index(request):
    return render(request, 'commodity/index.html')


# 消息中心
def tidings(request):
    return render(request, 'commodity/tidings.html')


# 充值
def recharge(request):
    return render(request, 'commodity/recharge.html')


# 零食飞速
def speed(request):
    return render(request, 'commodity/speed.html')


# 店铺详情
def list_detail(request):
    return render(request, 'commodity/list.html')


# 选择城市
def city(request):
    return render(request, 'commodity/city.html')


# 超市
def category(request):
    return render(request, 'commodity/category.html')
