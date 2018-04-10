from django.conf.urls import url
from .views import ShortNotesListView

urlpatterns = [
    # 首页
    url(r'^list$', ShortNotesListView.as_view(), name='shortNotesList'),
    # 详细页
]

