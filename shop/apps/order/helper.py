from django_redis import get_redis_connection

from commodity.models import CommoditySkuModel


# 连接redis获取用户购物车信息
def get_user_sku(request):
    # 接收用户id
    user_id = request.session.get('ID')
    # 连接redis
    r = get_redis_connection()
    # 准备键
    cart_key = f"cart_{user_id}"
    data = r.hgetall(cart_key)
    # 创建一个空列表保存model对象
    skus = []
    for key in data:
        sku = CommoditySkuModel.objects.get(pk=int(key))
        sku.count = data[key]
        skus.append(sku)
    return skus
