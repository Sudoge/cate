# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('zh_name', models.CharField(max_length=30)),
                ('en_name', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('click_rate', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
