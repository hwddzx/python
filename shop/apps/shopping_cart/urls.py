from django.conf.urls import url

from shopping_cart.views import shopcart

urlpatterns = [
    url(r'^shopcart/$', shopcart,name='购物车'),
]