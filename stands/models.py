from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=160)
    cumprimento = models.IntegerField()
    largura = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.localizacao}"