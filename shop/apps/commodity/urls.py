from django.conf.urls import url

from commodity.views import detail, index, tidings, recharge, speed, list_detail, city, category, village

urlpatterns = [
    url(r'^detail/(\d+)/$', detail, name='商品详情'),
    url(r'^index/$', index, name='首页'),
    url(r'^tidings/$', tidings, name='消息中心'),
    url(r'^recharge/$', recharge, name='充值'),
    url(r'^speed/$', speed, name='零食飞速'),
    url(r'^list_detail/$', list_detail, name='店铺详情'),
    url(r'^city/$', city, name='选择城市'),
    url(r'^category/(?P<cate_id>\d?)_?(?P<order>\d*)$', category, name='超市'),
    url(r'^village/$', village, name='校区选择'),
]
