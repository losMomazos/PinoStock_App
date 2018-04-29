from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from product import views,urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('product.urls'))

]
