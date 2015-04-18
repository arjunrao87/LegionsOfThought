from django.views import generic
from . import models
from main.models import ContactUs
from django.views.generic.edit import FormView
from main.forms import ContactForm

class Blog(generic.TemplateView):
    template_name = "blog.html"

class Home(generic.TemplateView):
    template_name = "home.html"

class About(generic.TemplateView):
    template_name = "about.html"

class Thanks(generic.TemplateView):
    template_name = "thanks.html"

class Contact(FormView):
	model=ContactUs
	template_name = 'contact.html'
	form_class = ContactForm
	success_url = '/phanks/'
	def get_success_url( self ):
		return reverse("phanks")
	def form_valid(self, form):
		print "about to save form ";
		form.save()
		return super(Contact, self).form_valid(form)
		