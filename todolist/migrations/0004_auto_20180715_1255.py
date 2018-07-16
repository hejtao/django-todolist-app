# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20180715_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
