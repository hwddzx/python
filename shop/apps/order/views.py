from django.http import Http404
from django.shortcuts import render, redirect
from django_redis import get_redis_connection

from commodity.models import CommoditySkuModel
from order.helper import get_user_sku
from order.models import Transport
from user.helps import check_login
from user.models import UserAddress


@check_login  # 全部订单
def allorder(request):
    return render(request, 'order/allorder.html')


@check_login  # 确认订单
def tureorder(request):
    # 获取用户id,查询地址信息
    user_id = request.session.get('ID')
    address = UserAddress.objects.filter(user=user_id).order_by('-is_default').first()
    transports = Transport.objects.all().order_by('price')
    # skus = get_user_sku(request)
    # 获取商品id
    sku_ids = request.GET.getlist('sku_ids')
    # 准备空列表用来装商品
    skus = []
    # 准备商品总计
    total_price = 0
    # 准备redis
    r = get_redis_connection()
    cart_key = "cart_{}".format(user_id)
    # 遍历
    for sku_id in sku_ids:
        # 商品信息
        try:
            sku = CommoditySkuModel.objects.get(pk=sku_id)
        except CommoditySkuModel.DoesNotExist:
            # 商品不存在,跳转到购物车
            # raise Http404('购物车商品不存在')
            return redirect('shopping_cart:购物车')
        # 获取对应商品的数量
        count = r.hget(cart_key, sku_id)
        count = int(count)
        sku.count = count
        # 装商品
        skus.append(sku)
        total_price += sku.price * count
    context = {
        'skus': skus,
        'address': address,
        'total_price': total_price,
        'transports': transports
    }
    return render(request, 'order/tureorder.html', context=context)


@check_login  # 订单详情
def orderdetail(request):
    return render(request, 'order/orderdetail.html')


@check_login  # 确认支付
def order(request):
    # 获取用户id,查询地址信息
    user_id = request.session.get('ID')
    address = UserAddress.objects.get(user=user_id, is_default=True)
    skus = get_user_sku(request)
    context = {
        'skus': skus,
        'address': address
    }
    return render(request, 'order/order.html', context=context)


@check_login  # 完成支付
def pay(request):
    return render(request, 'order/pay.html')
