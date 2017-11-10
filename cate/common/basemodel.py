from django.db import models


class BaseModel(models.Model):
    '''在这个类里面定义一些所有模型类都需要的字段'''
    # 数据创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 数据更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 逻辑删除字段
    is_delete = models.BooleanField(default=False)

    class Meta(object):
        abstract = True