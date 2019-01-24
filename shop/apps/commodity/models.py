from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# 商品分类表
class CommodityClassModel(models.Model):
    classname = models.CharField(verbose_name='分类名', max_length=20)
    classintro = models.TextField(verbose_name='分类简介')
    order = models.SmallIntegerField(default=0, verbose_name='排序')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommodityClassModel"
        # 后台管理
        verbose_name_plural = "商品分类管理"

    def __str__(self):
        return self.classname


# 商品单位表
class CommodityUnitModel(models.Model):
    unitname = models.CharField(verbose_name='单位名称', max_length=100)
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommodityUnitModel"
        # 后台管理
        verbose_name_plural = "商品单位管理"

    def __str__(self):
        return self.unitname


# 商品SPU表
class CommoditySpuModel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    detail = RichTextUploadingField(verbose_name='详情')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommoditySpuModel"
        # 后台管理
        verbose_name_plural = "商品SPU管理"

    def __str__(self):
        return self.name


# 商品SKU表
class CommoditySkuModel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=50)
    intro = models.TextField(verbose_name='简介')
    price = models.DecimalField(verbose_name='价格', decimal_places=2, max_digits=10)
    unit = models.ForeignKey(to='commodity.CommodityUnitModel',
                             verbose_name='单位')
    num = models.PositiveIntegerField(verbose_name='库存')
    sellnum = models.PositiveIntegerField(verbose_name='销量')
    logo = models.ImageField(upload_to='head/%Y%m/%d', verbose_name='logo地址')
    is_putaway = models.BooleanField(verbose_name='是否上架')
    class_id = models.ForeignKey(to='commodity.CommodityClassModel',
                                 verbose_name='商品分类ID')
    spu_id = models.ForeignKey(to='commodity.CommoditySpuModel',
                               verbose_name='商品SPU_ID')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommoditySkuModel"
        # 后台管理
        verbose_name_plural = "商品SKU管理"

    def __str__(self):
        return self.name


# 商品相册表
class CommodityPictureModel(models.Model):
    picture = models.ImageField(upload_to='head/%Y%m/%d', verbose_name='图片地址')
    sku_id = models.ForeignKey(to='commodity.CommoditySkuModel',
                               verbose_name='商品SKU_ID')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommodityPictureModel"
        # 后台管理
        verbose_name_plural = "商品相册管理"


# 首页轮播
class BannerModel(models.Model):
    name = models.CharField(verbose_name='轮播活动名', max_length=150)
    img_url = models.ImageField(verbose_name='轮播图片地址', upload_to='banner/%Y%m/%d')
    order = models.SmallIntegerField(verbose_name='排序ID', default=0)
    Commodity_sku = models.ForeignKey(to='commodity.CommoditySkuModel', verbose_name='商品SKU')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        verbose_name = "首页轮播管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 首页活动
class ActivityModel(models.Model):
    title = models.CharField(verbose_name='活动名称', max_length=150)
    img_url = models.ImageField(verbose_name='活动图片地址', upload_to='activity/%Y%m/%d')
    url_site = models.URLField(verbose_name='活动的url地址', max_length=200)
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "活动管理"
        verbose_name_plural = verbose_name


# 首页活动专区
class ActivityZoneModel(models.Model):
    title = models.CharField(verbose_name='活动专区名称', max_length=150)
    brief = models.CharField(verbose_name="活动专区的简介", max_length=200, null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="排序", default=0)
    is_on_sale = models.BooleanField(verbose_name="是否上线", default=False)
    goods_sku = models.ManyToManyField(to="commodity.CommoditySkuModel", verbose_name="商品")
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "首页活动管理"
        verbose_name_plural = verbose_name
