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
def category(request, cate_id, order):
    # 查询所有分类
    classes = CommodityClassModel.objects.filter(is_delete=False).order_by('order')
    # 取出第一个分类
    # classe = classes[0]
    # classe = classes.first()
    if cate_id == "":
        commodityclass = classes.first()
        cate_id = commodityclass.id
    else:
        # 根据分类id查询对应的分类
        cate_id = int(cate_id)
        commodityclass = CommodityClassModel.objects.get(pk=cate_id)
        # print(commodityclass)
    # 查询对应类下的所有商品
    # print(commodityclass.commodityskumodel_set.all())
    # 查询所有的商品
    skus = CommoditySkuModel.objects.filter(is_delete=False, class_id=commodityclass)
    if order == "":
        order = 0
    order = int(order)
    # 排序规则列表
    order_rule = ['pk', '-sellnum', 'price', '-price', '-addtime']
    skus = skus.order_by(order_rule[order])
    # if order == 0:
    #     skus = skus.order_by('pk')
    # elif order == 1:
    #     skus = skus.order_by('-sellnum')
    # elif order == 2:
    #     skus = skus.order_by('price')
    # elif order == 3:
    #     skus = skus.order_by('-price')
    # elif order == 4:
    #     skus = skus.order_by('-addtime')
    context = {
        'classes': classes,
        'skus': skus,
        'cate_id': cate_id,
        'order': order
    }
    return render(request, 'commodity/category.html', context=context)


@check_login  # 校区选择
def village(request):
    return render(request, 'commodity/village.html')
