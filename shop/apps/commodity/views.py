from django.shortcuts import render

from commodity.models import CommodityClassModel, CommoditySpuModel, CommoditySkuModel, BannerModel, ActivityZoneModel
from user.helps import check_login


@check_login  # 商品详情
def detail(request, id):
    # 获取商品sku的信息
    sku = CommoditySkuModel.objects.get(pk=id)
    context = {
        'sku': sku,
    }
    return render(request, 'commodity/detail.html', context=context)


@check_login  # 首页
def index(request):
    banner = BannerModel.objects.all()
    activity = ActivityZoneModel.objects.all()
    context = {
        'banners': banner,
        'activity': activity
    }
    return render(request, 'commodity/index.html', context=context)


@check_login  # 消息中心
def tidings(request):
    return render(request, 'commodity/tidings.html')


@check_login  # 充值
def recharge(request):
    return render(request, 'commodity/recharge.html')


@check_login  # 零食飞速
def speed(request):
    return render(request, 'commodity/speed.html')


@check_login  # 店铺详情
def list_detail(request):
    return render(request, 'commodity/list.html')


@check_login  # 选择城市
def city(request):
    return render(request, 'commodity/city.html')


@check_login  # 超市
def category(request):
    # 查询所有分类
    classes = CommodityClassModel.objects.filter(is_delete=False)
    # spus = CommoditySpuModel.objects.all()
    # 查询所有的商品
    skus = CommoditySkuModel.objects.filter(is_delete=False)
    context = {
        'classes': classes,
        'skus': skus
    }
    return render(request, 'commodity/category.html', context=context)


@check_login  # 校区选择
def village(request):
    return render(request, 'commodity/village.html')
