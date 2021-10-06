from rest_framework.serializers import ModelSerializer

from carro_moto.models import CarroMotoModel



class CarroMotoSerializer(ModelSerializer):
    class Meta:
        model = CarroMotoModel
        fields ='__all__'