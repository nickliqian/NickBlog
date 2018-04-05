# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='signature',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user_job',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user_site',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
