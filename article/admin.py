from django.contrib import admin
from article.models import Article, ArticleType, Comment, TagType


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'article_type', 'created')
    filter_horizontal = ('article_tag',)


class ArticelTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'isDelete')


class TagTypeAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'isDelete')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user_name', 'user_name', 'created')


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticelTypeAdmin)
admin.site.register(TagType, TagTypeAdmin)
admin.site.register(Comment, CommentAdmin)
