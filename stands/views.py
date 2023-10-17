from django.shortcuts import render
from django.views.generic import TemplateView

class StandTemplateView(TemplateView):
    template_name = 'stand_home.html'