from django.conf.urls import url

from django.views.generic.base import TemplateView
from bored.api import views


urlpatterns = [
    url(r'^api$', views.ContentsListAPIView.as_view(), name='list'),
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # url(r'^about$', views.AboutView.as_view(), name='about'),
    # url(r'^front$', views.FrontView.as_view(), name='front'),
    # url(r'^profile$', views.ProfileView.as_view(), name='profile'),
    url(r'^api/create$', views.ContentsCreateAPIView.as_view(), name='Create'),
    url(r'^api/update/(?P<pk>\d+)/$', views.ContentsUpdateAPIView.as_view(), name='update'),
    url(r'^api/delete/(?P<pk>\d+)/$', views.ContentsDeleteAPIView.as_view(), name='delete'),
    url(r'^api/(?P<pk>\d+)/$', views.ContentsDetailsAPIView.as_view(),name='detail'),
    # url(r'^profile/(?P<id>\d+)/$', views.profile_detail,name='profile_detail'),
]