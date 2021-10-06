from django.db import models


class CarroMoto(models):
    id_carro=models.IntegerField(primary_key=True)
    nombre=models.CharField()
    marca
