from django.conf.urls import url

from user.views import member, step, about, login, reg, forgetpassword, records, integral, integralexchange, \
    integralrecords, yhq, ygq, collect, collect_edit, infor, gladdress, saftystep, money, job, recommend, myrecommend, \
    message

urlpatterns = [
    url(r'^$', member, name='个人中心'),
    url(r'^login/$', login, name='登录'),
    url(r'^reg/$', reg, name='注册'),
    url(r'^step/$', step, name='系统设置'),
    url(r'^about/$', about, name='关于我们'),
    url(r'^forgetpassword/$', forgetpassword, name='忘记密码'),
    url(r'^records/$', records, name='账户余额'),
    url(r'^integral/$', integral, name='积分'),
    url(r'^integralexchange/$', integralexchange, name='积分兑换'),
    url(r'^integralrecords/$', integralrecords, name='兑换记录'),
    url(r'^yhq/$', yhq, name='优惠券'),
    url(r'^ygq/$', ygq, name='已过期'),
    url(r'^collect/$', collect, name='我的收藏'),
    url(r'^collect_edit/$', collect_edit, name='编辑收藏'),
    url(r'^infor/$', infor, name='个人资料'),
    url(r'^gladdress/$', gladdress, name='收货地址'),
    url(r'^saftystep/$', saftystep, name='安全设置'),
    url(r'^money/$', money, name='我的钱包'),
    url(r'^job/$', job, name='我要兼职'),
    url(r'^recommend/$', recommend, name='推荐有奖'),
    url(r'^myrecommend/$', myrecommend, name='我的推荐'),
    url(r'^message/$', message, name='我的动态'),
]
