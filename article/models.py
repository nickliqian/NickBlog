from django.db import models
from DjangoUeditor.models import UEditorField
from mylib.mixin import TimeStampMixin, LastSeenMixin


# 文章模型
class Article(TimeStampMixin, LastSeenMixin, models.Model):
    # 标题
    title = models.CharField(max_length=255, unique=True)
    # 作者
    author = models.CharField(max_length=1000, blank=False)
    # 作品类型
    article_type = models.ForeignKey('ArticleType', related_name="type2article")
    # 标签
    article_tag = models.ManyToManyField('TagType', related_name="tag2article", blank=True)
    # 浏览量
    view_count = models.IntegerField(default=0)
    # 文章正文
    content = UEditorField(height=300, width=1000, blank=False, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    # 说明
    remark = models.CharField(max_length=1000, default='no remark', blank=True)
    # 摘要
    short_note = models.TextField(max_length=1000, default='no short note', blank=True)
    # 是否删除
    isDelete = models.BooleanField(default=False)
    # 封面图片 height_field=None, width_field=None
    cover_img = models.ImageField(upload_to='uploads/coverImg', blank=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.article_type)

    def get_obsolute_url(self):

        return 'article:article-detail'

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    # 文章类型模型


class ArticleType(TimeStampMixin, models.Model):
    # 类型名称
    typename = models.CharField(max_length=50)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'


# 文章标签模型
class TagType(TimeStampMixin, models.Model):
    # 标签名称
    tag_name = models.CharField(max_length=50)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'


class Comment(TimeStampMixin, models.Model):
    # 对应的文章
    article = models.ForeignKey('Article', blank=False, related_name='article2comment')
    # 留言内容
    content = UEditorField(height=300, width=1000, blank=False, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    # 用户名
    user_name = models.CharField(max_length=50, default="匿名")
    # E-mail
    user_e_mail = models.EmailField(max_length=254, blank=True)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}".format(self.created, self.article, self.user_name)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = '文章评论'
