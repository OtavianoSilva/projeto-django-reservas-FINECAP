from django.forms import ModelForm
from .models import Reserva

class ReservaModelFrom(ModelForm):
    class Meta:
        model = Reserva
        teste = 'teste'
        fields = ["cnpj", "nome_empresa", "categoria_empresa", "quitado", "stand"]