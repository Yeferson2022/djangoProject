from rest_framework.viewsets import ModelViewSet

from carro_moto.models import CarroMotoModel
from carro_moto.serializers import CarroMotoSerializer


class CarroMotoViewsSet(ModelViewSet):
    queryset = CarroMotoModel.objects.all()
    serializer_class = CarroMotoSerializer
