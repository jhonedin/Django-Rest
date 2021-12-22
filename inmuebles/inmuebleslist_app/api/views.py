from rest_framework.response import Response
from rest_framework.decorators import api_view
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer

@api_view() # por defecto es un metodo GET tambien se puede escribir asi, api_view('GET')
def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    serializers = InmuebleSerializer(inmuebles, many=True)
    return Response(serializers.data)

@api_view()
def inmueble_detalle(request, pk):
    inmueble = Inmueble.objects.get(pk=pk)
    serializers = InmuebleSerializer(inmueble)
    return Response(serializers.data)