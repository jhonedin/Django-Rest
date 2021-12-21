# Django 
from django.urls import path
from django.urls.resolvers import URLPattern
# Views
from inmuebleslist_app.views import inmueble_list

urlpatterns = [
    path('list/', inmueble_list, name='inmueble_list'),
]