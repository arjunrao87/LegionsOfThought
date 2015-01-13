from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns(
    '',
    url(r'^gamma/$', views.GammaWorks.as_view(), name="gammaworks"),
)
