from django.shortcuts import render


# 购物车
def shopcart(request):  # ^shopcart/$
    return render(request, 'shopping_cart/shopcart.html')


