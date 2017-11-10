# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20171109_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('ad_name', models.CharField(max_length=30)),
                ('ad_image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'banner',
            },
        ),
    ]
