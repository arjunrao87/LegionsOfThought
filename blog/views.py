from django.views import generic
from . import models


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog.html"
    paginate_by = 10

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class Home(generic.TemplateView):
    template_name = "home.html"

class About(generic.TemplateView):
    template_name = "about.html"

class Contact(generic.TemplateView):
    template_name = "contact.html"