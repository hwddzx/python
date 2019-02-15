import os

from alipay import AliPay
from django.conf import settings
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


def get_alipay():
    # 构造支付请求
    app_private_key_string = open(os.path.join(settings.BASE_DIR, "utils/alipay/user_private_key.txt")).read()
    alipay_public_key_string = open(os.path.join(settings.BASE_DIR, 'utils/alipay/alipay_public_key.txt')).read()

    # 初始化对象
    alipay = AliPay(
        appid="2016092400582435",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False
    )

    return alipay
