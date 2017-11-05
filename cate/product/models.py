from django.db import models

# Create your models here.

class ProductManager(models.Manager):

    class Meta(object):
        abstract = True


class ProductModel(models.Model):
    zh_name = models.CharField(max_length=30)
    en_name = models.CharField(max_length=30, null=True)
    image = models.ImageField()
    price = models.IntegerField()

    objects = ProductManager()

    class Meta(object):
        db_table = 'product'
