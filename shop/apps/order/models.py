from django.db import models


class Transport(models.Model):
    """运输方式"""
    name = models.CharField(max_length=50, verbose_name='运输方式')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='运费')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "运输方式管理"
