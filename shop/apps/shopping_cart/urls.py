from django.conf.urls import url

from shopping_cart.views import shopcart, AddCartView

urlpatterns = [
    url(r'^shopcart/$', shopcart, name='购物车'),
    url(r'^AddCartView/$', AddCartView.as_view(), name='添加购物车'),
]
