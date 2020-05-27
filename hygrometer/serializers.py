from rest_framework import serializers
from .models import Hygrometer

class HygrometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hygrometer
        fields = ('id', 'type', 'value','latitud','longitud','tipo_de_terreno')