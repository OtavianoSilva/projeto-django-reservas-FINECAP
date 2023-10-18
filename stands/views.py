from django.shortcuts import render
from .models import Stand
from django.urls import reverse_lazy, reverse
from.forms import StandModelForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DeleteView, FormView
from django.views.generic.edit import DeleteView

class StandTemplateView(TemplateView):
    template_name = 'stand_home.html'

class StandListView(ListView):
    model = Stand
    paginate_by = 6
    template_name = 'standlist.html'

class StandDetailView(DeleteView):
    model = Stand
    template_name = 'standdetail.html'

class StandFormView(FormView):
    template_name = 'standform.html'
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
    template_name = 'stand_confirm_delete.html'
    context_object_name = "object"
    success_url = reverse_lazy("stands")
    success_message = "Stand deletado com sucesso! :)"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StandDeleteView, self).delete(request, *args, **kwargs)