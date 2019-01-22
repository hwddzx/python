from django.conf.urls import url

from order.views import allorder, tureorder, orderdetail, order, pay

urlpatterns = [
    url(r'^allorder/$', allorder, name='全部订单'),
    url(r'^tureorder/$', tureorder, name='确认订单'),
    url(r'^orderdetail/$', orderdetail, name='订单详情'),
    url(r'^order/$', order, name='提交订单'),
    url(r'^pay/$', pay, name='完成支付'),
]
