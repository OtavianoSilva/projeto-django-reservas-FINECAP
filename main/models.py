from django.db import models

class Empresa(models.Model):
    nome = models.TextField(max_length=160)
    estoque = models.PositiveIntegerField(default=0)
    faturamento = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        return self.nome