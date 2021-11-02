from django.db import models


class Carros(models.Model):# Essa class define o modelo do formulario q aparerece no form.html
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()