from django.db import models
from stands.models import Stand
from main.models import Empresa

class Reserva(models.Model):

    class Meta:
        app_label = 'reservas'

    cnpj = models.CharField(max_length=18)
    nome_empresa = models.CharField(max_length=160)
    categoria_empresa = models.CharField(max_length=160)
    quitado = models.BooleanField()
    data_reserva = models.DateTimeField(auto_now_add=True)

    stand = models.OneToOneField(Stand, on_delete=models.CASCADE, default=0)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=1)
    
    def __str__(self) -> str:
        return self.nome_empresa
    
    def save(self, *args, **kwargs):
        super(Reserva, self).save(*args, **kwargs)

        obj = Empresa.objects.get(id=self.empresa.id)

        obj.estoque =  int(obj.estoque) - 1
        obj.save()
        if self.quitado:
            obj.faturamento += float(obj.faturamento) + self.stand.valor
            obj.save()

