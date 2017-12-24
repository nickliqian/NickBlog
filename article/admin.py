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
    list_display = ('article', 'userOfComment', 'created', 'show_content')

    # 非转义模式显示评论
    def show_content(self, obj):
        if not obj.content:
            return None
        return obj.content
    show_content.short_description = 'Content'
    show_content.allow_tags = True


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticelTypeAdmin)
admin.site.register(TagType, TagTypeAdmin)
admin.site.register(Comment, CommentAdmin)
