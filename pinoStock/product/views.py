from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,redirect
from .forms import ProductForm,Searcher
from .models import Gpu,Cpu,MotherBoard
from django.views.generic import TemplateView

def new_product(request):
    if request.method == 'POST':
    	form = ProductForm(request.POST)
    	if form.is_valid():
    		product = form.save() 
    		product.save()
    		return HttpResponseRedirect('/')
    else:
    	form = ProductForm()

    template = loader.get_template('new_product.html')
    context = {
    	'form': form
    }
    return HttpResponse(template.render(context, request))

def question(request):
	obj = Gpu.objects.all()
	for g in obj :
		g_nombre = g.name
		g_category = g.category
	context = {
		"obj":obj,
		"g_nombre":g_nombre,
		"g_category":g_category
	}
	return render(request,"consulta.html",context)

def realizar_busqueda(request):
	form_buscar = Searcher(request.POST)
	obj_gpu = Gpu.objects.all()
	if form_buscar.is_valid():
		datos = form_buscar.cleaned_data
		dato_pieza = datos.get("pieza")
		dato_nombre = datos.get("nombre")
		if dato_pieza=="da":
			return render(request,"buscador.html",context)		
		for g in obj_gpu :
			g_nombre = g.name

	context = {
		'form':form_buscar,
		'obj_gpu':obj_gpu,
		'datos':form_buscar.cleaned_data,

	}		
	return render(request,"buscador.html",context)

def resultado_buscar(request):
	buscar = request.POST['buscalo']
	array_gpu = Gpu.objects.filter(category__contains=buscar)
	array_cpu = Cpu.objects.filter(name__contains=buscar)
	array_motherBoard = MotherBoard.objects.filter(category__contains=buscar)
	print(array_cpu)
	diccionario = {
		'array_cpu':array_cpu,
		'array_gpu':array_gpu,
		'array_motherBoard':array_motherBoard,
	}
	return render(request,"resultados.html",diccionario)

# datos= form_contacto.cleaned_data
#nombre = datos.get("nombre")
#opinion = datos.get("mensaje")