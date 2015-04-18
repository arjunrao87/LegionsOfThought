from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name="home"),
    url(r'^about/$', views.About.as_view(), name="about"),
    url(r'^blog/$', views.Blog.as_view(), name="blog"),
    url(r'^contact/$', views.Contact.as_view(), name="contact"),
    url(r'^thanks/$', views.Thanks.as_view(), name="thanks"),
)
