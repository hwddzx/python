from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django_redis import get_redis_connection

from commodity.models import CommoditySkuModel
from shopping_cart.helper import json_msg, get_cart_count
from user.helps import check_login


# 购物车
@check_login
def shopcart(request):
    # 接收用户ID
    user_id = request.session.get('ID')
    # 连接redis
    r = get_redis_connection()
    # 准备键
    cart_key = f"cart_{user_id}"
    # 查找出来得到一个数据全为二进制的字典
    data = r.hgetall(cart_key)
    # 创建一个空列表保存model对象
    skus = []
    for key in data:
        skus.append(CommoditySkuModel.objects.get(pk=int(key)))
    context = {
        'skus': skus
    }
    return render(request, 'shopping_cart/shopcart.html', context=context)


# 操作购物车,添加购物车数据
class AddCartView(View):
    """
        1. 需要接受的参数
            sku_id  count  从session中获取用户id
        2. 判断参数合法性
            a. 判断为整数
            b. 验证数据库中存在商品
            c. 验证库存是否充足
        3. 操作数据库
            将购物车数据保存到Redis
            存储的时候采用的数据类型为hash
            key : cart_user_id
            field : sku_id
            value : count
    """

    @method_decorator(check_login)
    def post(self, request):
        # 1. 接受参数
        user_id = request.session.get('ID')
        sku_id = request.POST.get('sku_id')
        # print(sku_id)
        count = request.POST.get('count')
        # 2. 判断参数合法性
        # a. 判断为整数
        try:
            sku_id = int(sku_id)
            count = int(count)
        except:
            return JsonResponse(json_msg(1, "参数错误!"))
        # b. 验证数据库中示是否存在商品
        try:
            goods_sku = CommoditySkuModel.objects.get(pk=sku_id)
        except CommoditySkuModel.DoesNotExist:
            return JsonResponse(json_msg(2, "商品不存在!"))
        # c. 验证库存是否充足
        if goods_sku.num < count:
            return JsonResponse(json_msg(3, "库存不足!"))
        # 2.操作数据
        # 连接Redis
        r = get_redis_connection()
        # 处理购物车的key
        cart_key = f"cart_{user_id}"
        # 获取购物车中已经存在的数量加上需要添加的与库存进行比较
        old_count = r.hget(cart_key, sku_id)  # 获取出来的是二进制
        if old_count is None:
            old_count = 0
        else:
            old_count = int(old_count)
        if goods_sku.num < old_count + count:
            return JsonResponse(json_msg(3, '库存不足!'))
        # 将商品添加到购物车
        r.hincrby(cart_key, sku_id, count)
        # 获取购物车中的总数量
        cart_count = get_cart_count(request)
        # 3.合成响应
        return JsonResponse(json_msg(0, "添加购物车成功!", data=cart_count))
