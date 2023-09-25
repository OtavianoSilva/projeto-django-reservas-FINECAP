from django.contrib import admin
from django.urls import path
from core.views import ReservaFormView, ReservaListView, ReservaDetailView, ReservaTemplateView, ReservaDeleteView, ReservaUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReservaTemplateView.as_view(), name='home'),
    path('cria_reserva', ReservaFormView.as_view(), name='cria_reserva'),
    path('reservas', ReservaListView.as_view(), name='reservas'),
    path('reservas/detail/<pk>', ReservaDetailView.as_view(), name='detail'),
    path('reservas/detail/<pk>/delete', ReservaDeleteView.as_view(), name='reserva_delete'),
    path("reservas/detail/<pk>/update", ReservaUpdateView.as_view(), name='reserva_update'),
]
