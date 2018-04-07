from django.conf.urls import url
from .views import IndexView, ArticleDetailView, ArticleListView, ArticleDetailRedirectView, ArticleTagView, ArticleTypeView


urlpatterns = [
    # 首页
    url(r'^$', IndexView.as_view(), name='index'),
    # 详细页
    url(r'^detail/(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    # 列表页
    url(r'^all/$', ArticleListView.as_view(), name='article-list'),
    # 标签页
    url(r'^tag/(?P<tag>.*)/$', ArticleTagView.as_view(), name='article-tag'),
    # 分类页
    url(r'^type/(?P<type>.*)/$', ArticleTypeView.as_view(), name='article-type'),
    # 详细页评论跳转
    url(r'^redirect_detail/(?P<pk>[-\w]+)/$', ArticleDetailRedirectView.as_view(), name='redirect-detail'),
]

