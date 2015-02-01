from django.conf.urls import patterns, url
from . import views, feed
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name="home"),
    url(r'^blog/$', views.BlogIndex.as_view(), name="blog"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^about/$', views.About.as_view(), name="about"),
    url(r'^contact/$', views.Contact.as_view(), name="contact"),
)
