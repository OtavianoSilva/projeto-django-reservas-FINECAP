from django.contrib import admin
from reservas.views import HomePage
from django.urls import path, include

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('reservas/', include('reservas.urls')),
    path('stands/', include('stands.urls')),
    path('admin/', admin.site.urls),
]
