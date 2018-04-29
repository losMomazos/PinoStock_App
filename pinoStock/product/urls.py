from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^product/new', views.new_product, name="new_product"),
	url(r'^product/consultar', views.question, name="question"),
	url(r'^busqueda', views.realizar_busqueda, name="realizar_busqueda"),
	url(r'^resultados', views.resultado_buscar,name="resultados")
]