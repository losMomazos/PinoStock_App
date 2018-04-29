from django import forms
from .models import Gpu

class ProductForm(forms.ModelForm):
	class Meta:
		model = Gpu
		fields = '__all__'

class Searcher(forms.Form):
	pieza = forms.CharField(max_length=255, required=True,label="Pieza : ",widget=(forms.TextInput(attrs={"value":""})))
	nombre = forms.CharField(max_length=255, required=True,label="Nombre : ",widget=(forms.TextInput(attrs={"value":""})))
		
			
