from django.conf.urls import url
from django.contrib import admin

from .views import (
    # comment_thread,
    ContentsDetailsAPIView,
    ContentsListAPIView

    )

urlpatterns = [
    url(r'^(?P<id>\d+)/$', ContentsDetailsAPIView.as_view(), name='thred'),
    url(r'^$', ContentsListAPIView.as_view(), name='list'),
    # url(r'^(?P<id>\d+)/deletecomment/$', comment_delete, name='delete'),
]