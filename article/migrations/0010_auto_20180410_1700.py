# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_remove_article_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletype',
            name='typename',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tagtype',
            name='tag_name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
