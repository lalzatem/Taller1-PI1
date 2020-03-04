from rest_framework import viewsets
from .models import Hygrometer
from .serializers import HygrometerSerializer

class HygrometerViewSet(viewsets.ModelViewSet):
    queryset = Hygrometer.objects.all().order_by('-created')
    serializer_class = HygrometerSerializer