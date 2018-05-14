from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name='product'
urlpatterns=[
	url(r'^$',views.hello_world),
	url(r'^product/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
	#path('product/<int:id_product>',views.detail,name="detail"),
]