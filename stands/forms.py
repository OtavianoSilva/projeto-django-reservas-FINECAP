from django.forms import ModelForm
from .models import Stand

class StandModelForm(ModelForm):
    class Meta:
        model = Stand
        fields = ['localizacao', 'cumprimento', 'largura', 'valor']