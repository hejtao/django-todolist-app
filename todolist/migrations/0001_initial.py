# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('complete', models.BooleanField(default=False)),
                ('pri', models.IntegerField(default=1)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
