from django.db import models
from mylib.mixin import TimeStampMixin, LastSeenMixin


# 文章模型
class ShortNotes(TimeStampMixin, LastSeenMixin, models.Model):
    # 标题
    title = models.CharField(max_length=255, unique=True)
    # 短笔记类型
    content_type = models.ForeignKey('ShortNotesType', related_name="type2short_notes")
    # 归档
    module_type = models.ForeignKey('ShortNotesModuleType', related_name="module2short_notes")
    # 笔记内容
    content = models.TextField()
    # 是否删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.title, self.content_type)

    # def get_obsolute_url(self):
    #     return 'article:article-detail'

    class Meta:
        verbose_name = '短笔记'
        verbose_name_plural = '短笔记'
        # 指定默认排序规则
        ordering = ['id']


class ShortNotesType(TimeStampMixin, models.Model):

    # 标签名称
    type_name = models.CharField(max_length=50, unique=True)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '短笔记类型'
        verbose_name_plural = '短笔记类型'
        # 指定默认排序规则
        ordering = ['id']


class ShortNotesModuleType(TimeStampMixin, models.Model):

    # 标签名称
    type_name = models.CharField(max_length=50, unique=True)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '归档'
        verbose_name_plural = '归档'
        # 指定默认排序规则
        ordering = ['id']