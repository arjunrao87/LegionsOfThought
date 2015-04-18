from django import forms

class ContactForm(forms.Form):
	name = forms.CharField( max_length=100 )
	email = forms.CharField( max_length=100 )
	phone = forms.CharField( max_length=100 )
	message = forms.CharField( max_length=250 )
