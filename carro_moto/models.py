from django.db import models


class CarroMotoModel(models.Model):
    id_carro = models.AutoField(primary_key=True, )
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=49)

    class Meta:
        db_table = 'carromoto'
