from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from article.models import Article, Comment
from mylib.myforms import CommentForm


class IndexView(TemplateView):
    template_name = "article/index.html"

    # 构造首页显示的对象
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


# timezone.now() -> 2017-12-16 16:10:46.836409+00:00
class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/detail.html"

    def comment(self):
        comment_list = Comment.objects.filter(article__pk=self.object.id)
        comment_count = len(comment_list)
        return comment_list, comment_count

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        obj = self.object
        # 记录被浏览次数
        obj.view_count += 1
        obj.save()
        context['article_comment'], context['comment_count'] = self.comment()
        comment_form = CommentForm()
        context['form'] = comment_form
        return context


class ArticleDetailRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article:article-detail'

    def get_redirect_url(self, *args, **kwargs):
        return super(ArticleDetailRedirectView, self).get_redirect_url(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        # 判断登陆状态
        if not request.user.is_authenticated():
            # 判断是否有article参数
            if not request.POST.get('article'):
                return redirect('/account/login/?next=/article/detail/%s/' % request.POST.get('article'))
            else:
                return redirect('/')
        else:
            form = CommentForm(request.POST)
            # 验证数据完整性
            if form.is_valid():
                form.save()

            return self.get(request, *args, **kwargs)


class ArticleListView(ListView):
    model = Article
    template_name = "article/list.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['comment_count'] = Comment.objects.count()
        return context
