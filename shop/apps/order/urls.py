from django.conf.urls import url

from order.views import allorder, orderdetail, Pay, Tureorder, Orders

urlpatterns = [
    url(r'^allorder/$', allorder, name='全部订单'),
    url(r'^orderdetail/$', orderdetail, name='订单详情'),
    url(r'^order/$', Orders.as_view(), name='提交订单'),
    url(r'^pay/$', Pay.as_view(), name='完成支付'),
    url(r'^tureorder/$', Tureorder.as_view(), name='确认订单'),
]
