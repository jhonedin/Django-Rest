from rest_framework.response import Response
from rest_framework.decorators import api_view
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer

@api_view(['GET','POST']) # el decorador indica que se soporta metodos get y post para consultar y escribir datos
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializers = InmuebleSerializer(inmuebles, many=True)
        return Response(serializers.data)
    
    if request.method == 'POST': # si llegan datos del cliente por metodo post
        de_serializer = InmuebleSerializer(data=request.data) # se deserializan los datos que llegan en formato json
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data) # si es valido devuelve al cliente la data deserializada
        else:
            return Response(de_serializer.errors) # si no es correcto devuelve al cliente error

@api_view()
def inmueble_detalle(request, pk):
    inmueble = Inmueble.objects.get(pk=pk)
    serializers = InmuebleSerializer(inmueble)
    return Response(serializers.data)