from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    
    # Custom apps
    url(r'^', include('blog.urls')),
    url(r'^', include('gammaworks.urls')),
    url(r'^', include('gallery.urls')),
)
