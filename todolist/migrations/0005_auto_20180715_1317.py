# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20180715_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='add_date',
            new_name='expire_date',
        ),
    ]
