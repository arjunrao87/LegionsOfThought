from django.views import generic
from . import models

from django.views.generic.edit import FormView


class GammaWorks(generic.TemplateView):
    template_name = "gamma.html"
		