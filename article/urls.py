from django.conf.urls import url
from .views import IndexView, ArticleDetailView


urlpatterns = [
    # 首页
    url(r'^$', IndexView.as_view(), name='index'),
    # 详细页
    url(r'^(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail')
    ]

