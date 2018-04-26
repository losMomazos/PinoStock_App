from django.contrib import admin

from .models import Cpu,Gpu,MotherBoard
# Register your models here.
admin.site.register(Cpu)
admin.site.register(Gpu)
admin.site.register(MotherBoard)
