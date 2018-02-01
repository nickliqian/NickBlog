from django.conf.urls import url
from apiModel import views


urlpatterns = [
    # 状态
    url(r'^$', views.api_index, name='apiIndex'),
]

