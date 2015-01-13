from django.conf.urls import patterns, url
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^gallery/$', views.Gallery.as_view(), name="gallery"),
)
