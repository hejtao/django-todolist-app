# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20180715_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='expire_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
