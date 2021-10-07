from rest_framework.serializers import ModelSerializer

from Empresa.models import EmpresaModel

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = EmpresaModel
        fields= '__all__'