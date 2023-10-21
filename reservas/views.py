from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, TemplateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from .forms import ReservaModelFrom
from .models import Reserva
from stands.models import Stand

class HomePage(TemplateView):
    template_name ="home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_reservas'] = Reserva.objects.count()
        context['num_stands'] = Stand.objects.count()
        return context

class ReservaTemplateView(TemplateView):
    template_name = "reservas/reservas_home.html"

class ReservaFormView(FormView):
    template_name = "reservas/reservaform.html"
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
    paginate_by = 6
    template_name = "reservas/reservalist.html"

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "reservas/detail.html"
    
class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reservas/confirm_delete.html'
    context_object_name = "object"
    success_url = reverse_lazy("reservas")
    success_message = "Reserva deletada com sucesso! :)"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReservaDeleteView, self).delete(request, *args, **kwargs)

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ["cnpj", "nome_empresa", "categoria_empresa", "quitado", "stand"]
    template_name = "reservas/reserva_update_form.html"
    template_name_suffix = "_update_form"
    context_object_name = "object"

    def get_success_url(self):
        messages.success(self.request, "Reserva atualizada com sucesso! :)")
        return reverse('detail', kwargs={'pk': self.object.pk})