from django.urls import path
from .views import StandTemplateView


urlpatterns = [
    path('home', StandTemplateView.as_view(), name='stands_home')
]