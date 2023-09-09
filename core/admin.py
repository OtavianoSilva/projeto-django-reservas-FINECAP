from django.contrib import admin
from .models import Stand, Reserva

class StandAdmin(admin.ModelAdmin):
    list_display = ["localizacao", "valor"]
admin.site.register(Stand, StandAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ["cnpj", "nome_empresa", "categoria_empresa", "quitado"]
admin.site.register(Reserva, ReservaAdmin)
