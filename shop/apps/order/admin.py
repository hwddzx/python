from django.contrib import admin

from order.models import Transport


@admin.register(Transport)
class CommodityClassModelAdmin(admin.ModelAdmin):
    list_per_page = 10
