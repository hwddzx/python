from django.shortcuts import render


# 全部订单
def allorder(request):
    return render(request, 'order/allorder.html')


# 确认订单
def tureorder(request):
    return render(request, 'order/tureorder.html')


# 订单详情
def orderdetail(request):
    return render(request, 'order/orderdetail.html')