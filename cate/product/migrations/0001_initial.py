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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('zh_name', models.CharField(max_length=30)),
                ('en_name', models.CharField(null=True, max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
