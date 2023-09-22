from django.contrib import admin
from django.urls import path
from core.views import ReservaFormView, ReservaListView, ReservaDetailView, ReservaTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ReservaTemplateView.as_view(), name="home"),
    path("cria-reserva", ReservaFormView.as_view(), name="cria_reserva"),
    path("reservas", ReservaListView.as_view(), name="reservas"),
    path("reservas/<pk>", ReservaDetailView.remove, name="reservas_remove"),
    path("reservas/detail/<pk>", ReservaDetailView.as_view(), name="detail"),
]
