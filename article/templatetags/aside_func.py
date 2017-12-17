from django import template
from article.models import Article, TagType


register = template.Library()


def get_top_view():
    top_view_objs = Article.objects.all().order_by('-view_count')[:6]
    return top_view_objs


def get_guesses():
    top_view_objs = Article.objects.all().order_by('view_count')[:6]
    return top_view_objs


def get_all_tags():
    all_tags = TagType.objects.all().order_by('-id')
    return all_tags


@register.inclusion_tag('article/aside.html')
def aside_tag():

    context = {
        "get_top_view": get_top_view(),
        "get_guesses": get_guesses(),
        "get_all_tags": get_all_tags(),
    }

    return context
