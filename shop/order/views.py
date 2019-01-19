from django.shortcuts import render


# 全部订单
def allorder(request):
    return render(request, 'order/allorder.html')
