from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.contrib import messages
from .forms import ReservaModelFrom
from .models import Reserva

class ReservaTemplateView(TemplateView):
    template_name = "home.html"

class ReservaFormView(FormView):
    template_name = "reservaform.html"
    form_class = ReservaModelFrom
    success_url = "/"

    def form_valid(self, form) -> HttpResponse:
        form.save(commit=True)
        messages.success(self.request, "Reserva salva com sucesso! :)")
        return super().form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        messages.error(self.request, "Falha ao salvar a reserva! :(")
        return super().form_invalid(form)
    
class ReservaListView(ListView):
    model = Reserva
    template_name = "reservalist.html"

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "detail.html"
    
    def remove(self, pk=None) -> HttpResponse:
        obj = Reserva.objects.get(id=pk)
        obj.delete()
        messages.success(self, "Reserva Removida com sucesso! :)")
        return redirect("reservas")
