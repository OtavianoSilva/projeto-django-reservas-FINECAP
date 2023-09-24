from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from .forms import ReservaModelFrom
from .models import Reserva

class ReservaTemplateView(TemplateView):
    template_name = "home.html"

class ReservaFormView(FormView):
    template_name = "reservaform.html"
    form_class = ReservaModelFrom
    success_url = "cria_reserva"

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, "Reserva salva com sucesso! :)")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Falha ao salvar a reserva! :(")
        return super().form_invalid(form)

class ReservaListView(ListView):
    model = Reserva
    template_name = "reservalist.html"

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "detail.html"
    
class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'confirm_delete.html'
    context_object_name = "object"
    success_url = reverse_lazy("reservas")
