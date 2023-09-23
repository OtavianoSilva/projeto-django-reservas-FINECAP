from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=160)
    valor = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.localizacao}"
    

class Reserva(models.Model):
    cnpj = models.CharField(max_length=18)
    nome_empresa = models.CharField(max_length=160)
    categoria_empresa = models.CharField(max_length=160)
    quitado = models.BooleanField()

    stand = models.OneToOneField(Stand, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nome_empresa
    