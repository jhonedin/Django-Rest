# from django.shortcuts import render
# from django.http import JsonResponse
# # models
# from inmuebleslist_app.models import Inmueble
# # Create your views here.

# # Obtener todos los datos de inmueble
# def inmueble_list(request):
#     inmuebles = Inmueble.objects.all()
#     data = {
#         'inmuebles': list(inmuebles.values())
#     }
#     return JsonResponse(data)

# # Busqueda por Id en inmueble
# def inmueble_detalle(request,pk):
#     inmueble = Inmueble.objects.get(pk=pk)
#     data = {
#         'direccion' : inmueble.direccion,
#         'pais' : inmueble.pais,
#         'descripcion' : inmueble.descripcion,
#         'imagen' : inmueble.imagen,
#         'active' : inmueble.active,
#     }
#     return JsonResponse(data)