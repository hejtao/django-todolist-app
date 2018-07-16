# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='add_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='pri',
            field=models.IntegerField(),
        ),
    ]
