from django.shortcuts import render
from django_redis import get_redis_connection

from commodity.models import CommoditySkuModel
from order.helper import get_user_sku
from user.helps import check_login
from user.models import UserAddress


@check_login  # 全部订单
def allorder(request):
    return render(request, 'order/allorder.html')


@check_login  # 确认订单
def tureorder(request):
    skus = get_user_sku(request)
    context = {
        'skus': skus
    }

    return render(request, 'order/tureorder.html', context=context)


@check_login  # 订单详情
def orderdetail(request):
    return render(request, 'order/orderdetail.html')


@check_login  # 提交订单
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
