from django.conf.urls import url

from commodity.views import detail, index

urlpatterns = [
    url(r'^detail/$', detail, name='商品详情'),
    url(r'^index/$', index, name='首页'),
]
