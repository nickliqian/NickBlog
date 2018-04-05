# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180405_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.NullBooleanField(choices=[(True, '男'), (False, '女'), (None, '保密')]),
        ),
    ]
