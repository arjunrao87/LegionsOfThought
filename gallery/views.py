from django.views import generic
from . import models

class Gallery(generic.TemplateView):
    template_name = "gallery.html"