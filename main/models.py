from django.db import models

class Empresa(models.Model):
    nome = models.TextField(max_length=160)
    estoque = models.PositiveIntegerField(default=0)
    faturamento = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.id}'