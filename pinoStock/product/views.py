from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import MotherBoard
# Create your views here.
def hello_world(request):
	motherboard  = MotherBoard.objects.order_by('id')

	template = loader.get_template('motherboard.html')

	context = {
		'motherboard':motherboard
	}
	return HttpResponse(template.render(context,request))
	#return render(request,'motherboard.html')