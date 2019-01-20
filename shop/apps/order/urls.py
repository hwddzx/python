from django.conf.urls import url

from order.views import allorder, tureorder, orderdetail

urlpatterns = [
    url(r'^allorder/$', allorder, name='全部订单'),
    url(r'^tureorder/$', tureorder, name='确认订单'),
    url(r'^orderdetail/$', orderdetail, name='订单详情'),
]
