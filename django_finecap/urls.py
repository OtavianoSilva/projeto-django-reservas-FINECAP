from django.contrib import admin
from django.urls import path
from core.views import ReservaFormView, ReservaListView, ReservaDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ReservaFormView.as_view(), name="cria_reserva"),
    path("reservas", ReservaListView.as_view(), name="reservas"),
    path("reservas/<pk>", ReservaDetailView.remove, name="reservas_remove"),
    path("reservas/detail/<pk>", ReservaDetailView.as_view(), name="detail"),
]
