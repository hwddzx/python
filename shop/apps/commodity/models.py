from django.db import models


# 商品分类表
class CommodityClassModel(models.Model):
    classname = models.CharField(verbose_name='分类名', max_length=20)
    classintro = models.TextField(verbose_name='分类简介')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommodityClassModel"
        # 后台管理
        verbose_name = "商品分类表"


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
        verbose_name = "商品单位表"


# 商品SPU表
class CommoditySpuModel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    detail = models.TextField(verbose_name='详情')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommoditySpuModel"
        # 后台管理
        verbose_name = "商品SPU表"


# 商品SKU表
class CommoditySkuModel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=50)
    intro = models.TextField(verbose_name='简介')
    price = models.DecimalField(verbose_name='价格', decimal_places=2, max_digits=10)
    unit = models.ForeignKey(to='commodity.CommodityUnitModel',
                             verbose_name='单位')
    num = models.PositiveIntegerField(verbose_name='库存')
    sellnum = models.PositiveIntegerField(verbose_name='销量')
    logo = models.ImageField(verbose_name='logo地址')
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
        verbose_name = "商品SKU表"


# 商品相册表
class CommodityPictureModel(models.Model):
    picture = models.ImageField(verbose_name='图片地址')
    sku_id = models.ForeignKey(to='commodity.CommoditySkuModel',
                               verbose_name='商品SKU_ID')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        # 设置表名
        db_table = "CommodityPictureModel"
        # 后台管理
        verbose_name = "商品相册表"
