from django.views import generic
from . import models
from django.views.generic.edit import FormView
from blog.forms import ContactForm
from blog.models import ContactUs

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

class Contact(FormView):
	model=ContactUs
	template_name = 'contact.html'
	form_class = ContactForm
	success_url = '/thanks/'
	def form_valid(self, form):
		form.save()
		return super(Contact, self).form_valid(form)