from django.contrib import admin
from .models import Stand

class StandAdmin(admin.ModelAdmin):
    list_display = ["localizacao", "cumprimento", "largura" ,"valor", "esta_reservado", "empresa"]
admin.site.register(Stand, StandAdmin)
