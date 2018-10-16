

from django.conf.urls import url
from django.contrib import admin

from .views import (
    # comment_thread,
    comment_delete

    )

urlpatterns = [
    # url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    url(r'^(?P<id>\d+)/deletecomment/$', comment_delete, name='delete'),
]