import os
from datetime import datetime
import random
from time import sleep

from alipay import AliPay
from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django_redis import get_redis_connection

from commodity.models import CommoditySkuModel
from order.helper import get_user_sku, get_alipay
from order.models import Transport, Order, OrderGoods, Payment
from shopping_cart.helper import json_msg
from user.helps import check_login
from user.models import UserAddress, User


@check_login  # 全部订单
def allorder(request):
    return render(request, 'order/allorder.html')


class Tureorder(View):
    """确认订单"""

    @method_decorator(check_login)
    def get(self, request):
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
            try:
                count = r.hget(cart_key, sku_id)
                count = int(count)
            except:
                return redirect("shopping_cart:购物车")
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

    @method_decorator(check_login)
    def post(self, request):
        """
        保存订单数据
        1. 订单基本信息表 和 订单商品表
        """
        # 1. 接收参数
        transport_id = request.POST.get('transport')
        sku_ids = request.POST.getlist('sku_ids')
        address_id = request.POST.get('address')

        # 接收用户id
        user_id = request.session.get('ID')
        user = User.objects.get(pk=user_id)

        # 验证数据合法性
        try:
            transport_id = int(transport_id)
            address_id = int(address_id)
            sku_ids = [int(i) for i in sku_ids]
        except:
            return JsonResponse(json_msg(2, '参数错误'))
        # 验证收货地址和运输方式存在
        try:
            address = UserAddress.objects.get(pk=address_id)
        except UserAddress.DoesNotExist:
            return JsonResponse(json_msg(3, '收货地址不存在!'))

        try:
            transport = Transport.objects.get(pk=transport_id)
        except Transport.DoesNotExist:
            return JsonResponse(json_msg(4, '运输方式不存在!'))

        # 2. 操作数据
        # 操作订单基本信息表
        order_sn = "{}{}{}".format(datetime.now().strftime("%Y%m%d%H%M%S"), user_id, random.randrange(10000, 99999))
        address_info = "{}{}{}-{}".format(address.province, address.city, address.area, address.brief)
        order = Order.objects.create(
            user=user,
            order_sn=order_sn,
            transport_price=transport.price,
            transport=transport.name,
            username=address.username,
            phone=address.phone,
            address=address_info
        )

        # 操作订单商品表
        # 操作redis
        r = get_redis_connection()
        cart_key = "cart_{}".format(user_id)
        # 准备变量保存商品总金额
        goods_total_price = 0
        for sku_id in sku_ids:
            # 获取商品对象
            try:
                goods_sku = CommoditySkuModel.objects.get(pk=sku_id, is_delete=False, is_putaway=True)
            except CommoditySkuModel.DoesNotExist:
                return JsonResponse(json_msg(5, '商品不存在'))
            # 获取购物车中商品的数量
            try:
                count = r.hget(cart_key, sku_id)
                count = int(count)
            except:
                return JsonResponse(json_msg(6, '购物车中数量不存在'))
            # 判断库存是否充足
            if goods_sku.num < count:
                return JsonResponse(json_msg(7, '库存不足!'))
            # 保存订单商品表
            order_goods = OrderGoods.objects.create(
                order=order,
                goods_sku=goods_sku,
                price=goods_sku.price,
                count=count
            )
            # 添加商品总金额
            goods_total_price += goods_sku.price * count
            # 扣除库存,销量增加
            goods_sku.num -= count
            goods_sku.sellnum += count
            goods_sku.save()

        # 反过头来操作订单基本信息表 商品总金额和订单总金额
        order_price = goods_total_price + transport.price
        order.total_price = goods_total_price
        order.order_price = order_price
        order.save()
        # 清空reds中的购物车数据(对应sku_id)
        r.hdel(cart_key, *sku_ids)
        # 3. 合成响应
        return JsonResponse(json_msg(0, '创建订单成功', data=order_sn))


@check_login  # 订单详情
def orderdetail(request):
    return render(request, 'order/orderdetail.html')


class Orders(View):
    """确认支付"""

    @method_decorator(check_login)
    def get(self, request):
        # 获取用户id,查询地址信息
        order_sn = request.GET.get('order_sn')
        user_id = request.session.get('ID')
        order = Order.objects.get(order_sn=order_sn, user_id=user_id)
        payments = Payment.objects.filter(is_delete=False)
        context = {
            'order': order,
            'payments': payments
        }
        return render(request, 'order/order.html', context=context)

    @method_decorator(check_login)
    def post(self, request):
        # 参数接收
        payment = request.POST.get('payment')
        order_sn = request.POST.get('order_sn')
        user_id = request.session.get('ID')
        # 判断参数合法性
        try:
            payment = int(payment)
        except:
            return JsonResponse(json_msg(1, '参数错误'))
        # 支付方式是否存在
        try:
            payment = Payment.objects.get(pk=payment)
        except payment.DoesNotExist:
            return JsonResponse(json_msg(2, '支付方式不存在'))
        # 判断订单是否是自己的,并且是一个未支付的订单
        try:
            order = Order.objects.get(user_id=user_id, order_sn=order_sn, order_status=0)
        except order.DoesNotExist:
            return JsonResponse(json_msg(3, "订单不满足要求"))
        # 判断用户是否需要使用支付宝支付
        if payment.name == "支付宝支付":
            # 构造支付请求对象
            alipay = get_alipay()

            # 构造请求地址
            order_string = alipay.api_alipay_trade_wap_pay(
                out_trade_no=order.order_sn,  # 订单编号
                total_amount=str(order.order_price),  # 订单金额
                subject="葫芦娃杂货店订单",  # 订单描述
                return_url="http://127.0.0.1:8000/order/pay/",  # 同步通知地址
                notify_url=None  # 异步通知地址 重要
            )

            # 拼接地址
            url = "https://openapi.alipaydev.com/gateway.do?" + order_string

            # 通过json返回请求地址
            return JsonResponse(json_msg(0, "创建支付地址成功", data=url))
        else:
            return JsonResponse(json_msg(4, "该支付方式暂不支支持"))


class Pay(View):
    """展示支付结果"""

    def get(self, request):
        # 查询订单是否交易成功
        # 构造支付请求对象
        alipay = get_alipay()

        # 获取订单编号
        order_sn = request.GET.get('out_trade_no')
        total_amount = request.GET.get('total_amount')

        # check order status
        paid = False
        for i in range(10):
            # 根据订单编号查询
            result = alipay.api_alipay_trade_query(out_trade_no=order_sn)
            # print(result)
            if result.get("trade_status", "") == "TRADE_SUCCESS":
                # 支付成功
                paid = True
                break

            # 继续执行
            # check every 3s, and 10 times in all
            sleep(3)
            print("not paid...")

        # 判断支付是否成功
        context = {
            'order_sn': order_sn,
            'total_amount': total_amount,
        }
        if paid is False:
            # 支付失败
            context['result'] = "支付失败"
        else:
            # 支付成功
            context['result'] = "支付成功"

        return render(request, "order/pay.html", context=context)
