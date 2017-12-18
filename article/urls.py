from django.conf.urls import url
from .views import IndexView, ArticleDetailView, ArticleListView, ArticleDetailRedirectView


urlpatterns = [
    # 首页
    url(r'^$', IndexView.as_view(), name='index'),
    # 详细页
    url(r'^detail/(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    # 列表页
    url(r'^all/$', ArticleListView.as_view(), name='article-list'),

    url(r'^redirect_detail/(?P<pk>[-\w]+)/$', ArticleDetailRedirectView.as_view(), name='redirect-detail'),
    ]

