# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_note',
            field=models.TextField(max_length=1000, blank=True, default='no short note'),
        ),
    ]
