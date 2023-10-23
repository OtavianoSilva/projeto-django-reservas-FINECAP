from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Empresa
from reservas.models import Reserva
from stands.models import Stand

class HomePage(TemplateView):
    template_name ="home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_reservas'] = Reserva.objects.count()
        context['num_stands'] = Stand.objects.count()
        return context

class EmpresaStatus(ListView):
    model = Empresa
    paginate_by = 1
    template_name = 'main/empresa_status.html'