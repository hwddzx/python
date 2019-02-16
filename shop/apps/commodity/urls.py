from django.conf.urls import url
# 视图缓存
from django.views.decorators.cache import cache_page

from commodity.views import detail, index, tidings, recharge, speed, list_detail, city, category, village

urlpatterns = [
    url(r'^detail/(\d+)/$', detail, name='商品详情'),
    url(r'^index/$', cache_page(3600)(index), name='首页'),
    url(r'^tidings/$', tidings, name='消息中心'),
    url(r'^recharge/$', recharge, name='充值'),
    url(r'^speed/$', speed, name='零食飞速'),
    url(r'^list_detail/$', list_detail, name='店铺详情'),
    url(r'^city/$', city, name='选择城市'),
    url(r'^category/(?P<cate_id>\d?)_?(?P<order>\d*)$', cache_page(3600)(category), name='超市'),
    url(r'^village/$', village, name='校区选择'),
]
