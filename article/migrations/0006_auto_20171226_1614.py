# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment_userofcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_e_mail',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
    ]
