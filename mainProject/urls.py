"""mainProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin,auth
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import login_view,register_view,logout_view,profileedit
#from comments.views import commentView
from comments.views import comment_delete
urlpatterns = [

    url(r'^admin/', admin.site.urls),
      url(r'^', include('bored.urls', namespace="bored")),
      url(r'^', include('bored.api.urls', namespace="bored-api")),
       url(r'^comments', include('comments.api.urls', namespace="comments-api")),
 url(r'^ckeditor/', include('ckeditor_uploader.urls')),
  url(r'^accounts/', include('allauth.urls')),
url(r'^profile/profile-edit/', profileedit,name='profile_edit'),
 url(r'^(?P<id>\d+)/deletecomment/(?P<id1>\d+)',comment_delete,name='comments'),
 url(r'^accounts/login/', login_view,name='login'),
 url(r'^register/', register_view,name='register'),
  url(r'^accounts/logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)