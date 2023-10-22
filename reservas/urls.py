from django.urls import path
from .views import *


urlpatterns = [
    path('cria_reserva', ReservaFormView.as_view(), name='cria_reserva'),
    path('reservas/list', ReservaListView.as_view(), name='reservas-list'),
    path('reservas/detail/<pk>', ReservaDetailView.as_view(), name='reservas-detail'),
    path('reservas/detail/<pk>/delete', ReservaDeleteView.as_view(), name='reservas-delete'),
    path("reservas/detail/<pk>/update", ReservaUpdateView.as_view(), name='reservas-update'),
]