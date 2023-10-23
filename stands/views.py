from django.shortcuts import render
from .models import Stand
from django.urls import reverse_lazy, reverse
from.forms import StandModelForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DeleteView, FormView, UpdateView
from django.views.generic.edit import DeleteView

class StandTemplateView(TemplateView):
    template_name = 'stand/stand_home.html'

class StandListView(ListView):
    model = Stand
    paginate_by = 6
    template_name = 'stand/standlist.html'

class StandCardListView(ListView):
    model = Stand
    paginate_by = 6
    template_name = 'stand/standcardlist.html'

class StandDetailView(DeleteView):
    model = Stand
    template_name = 'stand/standdetail.html'

class StandFormView(FormView):
    template_name = 'stand/standform.html'
    form_class = StandModelForm
    success_url = 'cria_stand'

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, "Stand salva com sucesso! :)")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Falha ao salvar o stand! :(")
        return super().form_invalid(form)
    
class StandDeleteView(DeleteView):
    model = Stand
    template_name = 'stand/stand_confirm_delete.html'
    context_object_name = "object"
    success_url = reverse_lazy("stands")
    success_message = "Stand deletado com sucesso! :)"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StandDeleteView, self).delete(request, *args, **kwargs)
    
class StandUpdateView(UpdateView):
    model = Stand
    fields = ["localizacao", "cumprimento", "largura", "esta_reservado", "valor"]
    template_name = 'stand/stand_update_form.html'
    template_name_suffix = "_update_form"
    context_object_name = "object"

    def get_success_url(self):
        messages.success(self.request, "Stand atualizado com sucesso! :)")
        return reverse('stands_detail', kwargs={'pk': self.object.pk})