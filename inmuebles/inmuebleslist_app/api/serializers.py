from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    # se crea a nivel de metodos una funcion que valida los datos que llegan desde el cliente para registrar en la base de datos
    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data) # ** indica que se devuelven todos los parametros de validated_data