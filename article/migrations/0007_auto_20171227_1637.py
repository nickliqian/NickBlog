# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20171226_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章', 'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '文章评论', 'verbose_name_plural': '文章评论', 'ordering': ['id']},
        ),
    ]
