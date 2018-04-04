# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180404_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cover_img',
        ),
    ]
