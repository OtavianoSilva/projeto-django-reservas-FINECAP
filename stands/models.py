from django.db import models
from main.models import Empresa

class Stand(models.Model):

    class Meta:
        app_label = 'stands'

    localizacao = models.CharField(max_length=160)
    cumprimento = models.IntegerField()
    largura = models.IntegerField()
    valor = models.IntegerField()
    esta_reservado = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='media')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.localizacao}"
    
    def save(self, *args, **kwargs):
        super(Stand, self).save(*args, **kwargs)
        if not self.esta_reservado:
            self.empresa.estoque += 1
            self.empresa.save()
        