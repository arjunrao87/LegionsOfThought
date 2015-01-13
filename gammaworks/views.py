from django.views import generic
from . import models

class GammaWorks(generic.TemplateView):
    template_name = "gamma.html"