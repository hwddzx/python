from django.shortcuts import render


# 商品详情
def detail(request):
    return render(request, 'commodity/detail.html')


# 首页
def index(request):
    return render(request, 'commodity/index.html')
