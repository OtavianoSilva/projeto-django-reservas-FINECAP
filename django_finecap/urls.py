from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('reservas/', include('reservas.urls')),
    path('admin/', admin.site.urls),
]
