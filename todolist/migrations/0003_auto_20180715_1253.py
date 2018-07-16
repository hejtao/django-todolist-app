# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20180715_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='pri',
            field=models.IntegerField(default=1),
        ),
    ]
