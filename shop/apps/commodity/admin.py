from django.contrib import admin

from commodity.models import CommodityClassModel, CommodityUnitModel, CommoditySpuModel, CommoditySkuModel, \
    CommodityPictureModel, BannerModel, ActivityModel, ActivityZoneModel


# 对模型进行管理(管理显示结构)
@admin.register(CommodityClassModel)
class CommodityClassModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['classname', 'classintro', 'addtime', 'updatetime', 'is_delete']


@admin.register(CommodityUnitModel)
class CommodityUnitModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['unitname', 'addtime', 'updatetime', 'is_delete']
    # 指定显示的列


@admin.register(CommoditySpuModel)
class CommoditySpuModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['id', 'name', 'detail', 'addtime', 'updatetime', 'is_delete']


class CommodityPictureModelInline(admin.TabularInline):
    model = CommodityPictureModel
    extra = 2


@admin.register(CommoditySkuModel)
class CommoditySkuModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['name', 'intro', 'price', 'unit', 'num', 'sellnum', 'logo', 'is_putaway', 'class_id', 'spu_id',
                    'addtime', 'updatetime', 'is_delete']
    inlines = [
        CommodityPictureModelInline,
    ]


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['name', 'img_url', 'order', 'Commodity_sku', 'addtime', 'updatetime', 'is_delete']


@admin.register(ActivityModel)
class ActivityModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['title', 'img_url', 'url_site', 'addtime', 'updatetime', 'is_delete']


@admin.register(ActivityZoneModel)
class ActivityZoneModelAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['title', 'brief', 'order', 'is_on_sale', 'addtime', 'updatetime', 'is_delete']
