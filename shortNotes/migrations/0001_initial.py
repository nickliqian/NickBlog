# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('last_seen', models.DateTimeField(verbose_name='last seen', auto_now_add=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('content', models.TextField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '短笔记',
                'ordering': ['id'],
                'verbose_name_plural': '短笔记',
            },
        ),
        migrations.CreateModel(
            name='ShortNotesModuleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('type_name', models.CharField(unique=True, max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '归档',
                'ordering': ['id'],
                'verbose_name_plural': '归档',
            },
        ),
        migrations.CreateModel(
            name='ShortNotesType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('type_name', models.CharField(unique=True, max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '短笔记类型',
                'ordering': ['id'],
                'verbose_name_plural': '短笔记类型',
            },
        ),
        migrations.AddField(
            model_name='shortnotes',
            name='content_type',
            field=models.ForeignKey(to='shortNotes.ShortNotesType', related_name='type2short_notes'),
        ),
        migrations.AddField(
            model_name='shortnotes',
            name='module_type',
            field=models.ForeignKey(to='shortNotes.ShortNotesModuleType', related_name='module2short_notes'),
        ),
    ]
