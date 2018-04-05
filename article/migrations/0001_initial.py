# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('last_seen', models.DateTimeField(verbose_name='last seen', auto_now_add=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=1000)),
                ('view_count', models.IntegerField(default=0)),
                ('content', DjangoUeditor.models.UEditorField()),
                ('remark', models.CharField(max_length=1000, blank=True, default='no remark')),
                ('short_note', models.CharField(max_length=1000, blank=True, default='no short note')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('typename', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('content', DjangoUeditor.models.UEditorField()),
                ('user_name', models.CharField(max_length=50, default='匿名')),
                ('user_e_mail', models.EmailField(max_length=254, blank=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='article.Article')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
            },
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('tag_name', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(blank=True, related_name='tag2article', to='article.TagType'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(related_name='type2article', to='article.ArticleType'),
        ),
    ]
