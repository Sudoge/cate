from django.db import models
from common.basemodel import BaseModel


# Create your models here.

class ProductManager(models.Manager):

    def __init__(self):
        super(ProductManager, self).__init__()

    def get_new_food(self):
        """返回最近更新过的美食"""
        return self.all().order_by('-update_time')[:6]

    def higher_rate(self):
        return self.all().order_by('-click_rate')[:9]

    class Meta(object):
        abstract = True


class BannerManager(models.Manager):
    '''横幅广告管理器'''
    def get_new_banner(self):
        return self.all().order_by('-update_time')[:3]


class ProductModel(BaseModel):
    '''美食模型'''
    # 美食中文名
    zh_name = models.CharField(max_length=30)
    # 美食英文名
    en_name = models.CharField(max_length=30, null=True)
    # 美食图片
    image = models.ImageField()
    # 美食价格
    price = models.IntegerField()
    # 美食点击量
    click_rate = models.IntegerField(default=0)

    objects = ProductManager()

    class Meta(object):
        db_table = 'product'


class BannerModel(BaseModel):
    '''横幅广告模型'''
    ad_name = models.CharField(max_length=30)
    ad_image = models.ImageField()

    objects = BannerManager()

    class Meta(object):
        db_table = 'banner'


