from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('empresa/status', EmpresaStatus.as_view(), name='empresa-status'),
]