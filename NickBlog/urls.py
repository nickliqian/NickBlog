"""NickBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from article.search_views import MySearchView
from article.views import IndexView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # article
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^index/', include("article.urls", namespace="index")),
    url(r'^article/', include("article.urls", namespace="article")),
    # search
    url(r'^search/', MySearchView(), name='haystack_search'),
    url('^account/', include('django.contrib.auth.urls')),
    url('^account/', include('account.urls', namespace='account')),
    # QA system
    url(r'^qa/', include('qa.urls')),
]

# debug 添加到全局url
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)

if 'silk' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^silk/', include('silk.urls', namespace='silk'))
    ]