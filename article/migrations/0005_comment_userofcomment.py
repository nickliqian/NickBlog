# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20171219_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='userOfComment',
            field=models.ForeignKey(null=True, related_name='comment2account', to=settings.AUTH_USER_MODEL),
        ),
    ]
