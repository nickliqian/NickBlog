from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.http import Http404
from django.utils import timezone

from article.models import Article


class IndexView(TemplateView):
    template_name = "article/index.html"

    @staticmethod
    def newest_article():
        try:
            four_articles = Article.objects.all().order_by('-id')[:4]
            objs1 = four_articles[0:2]
            objs2 = four_articles[2:4]
        except IndexError:
            raise Http404
        return [objs1, objs2]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['objss'] = self.newest_article()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class ArticleDetailView(DetailView):

    model = Article
    template_name = "article/detail.html"

    def get_context_data(self, **kwargs):
        obj = self.object
        obj.view_count += 1
        obj.save()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
