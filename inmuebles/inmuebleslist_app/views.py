from django.shortcuts import render
from django.http import JsonResponse
# models
from inmuebleslist_app.models import Inmueble
# Create your views here.

def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    data = {
        'inmuebles': list(inmuebles.values())
    }
    return JsonResponse(data)