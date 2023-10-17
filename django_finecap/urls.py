from django.contrib import admin
from reservas.views import ReservaTemplateView
from django.urls import path, include

urlpatterns = [
    path('', ReservaTemplateView.as_view()),
    path('reservas/', include('reservas.urls')),
    path('admin/', admin.site.urls),
]
