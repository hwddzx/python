from django.contrib import admin

from order.models import Transport, Order, Payment, OrderGoods


@admin.register(Transport)
class CommodityClassModelAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(Order)
class CommodityClassModelAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(Payment)
class CommodityClassModelAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(OrderGoods)
class CommodityClassModelAdmin(admin.ModelAdmin):
    list_per_page = 10
