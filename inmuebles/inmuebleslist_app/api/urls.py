# Django 
from django.urls import path
# Views
from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle

urlpatterns = [
    path('list/', inmueble_list, name='inmueble_list'),
    path('<int:pk>', inmueble_detalle, name='inmueble_detalle'),
]