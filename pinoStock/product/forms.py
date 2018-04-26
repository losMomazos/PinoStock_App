from django import forms

class ContactForm(forms.Form):
	def __init__(self, arg):
		super(ContactForm, self).__init__()
		self.arg = arg
