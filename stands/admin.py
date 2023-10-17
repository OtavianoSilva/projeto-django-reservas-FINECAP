from django.contrib import admin
from .models import Stand

class StandAdmin(admin.ModelAdmin):
    list_display = ["localizacao", "cumprimento", "largura" ,"valor"]
admin.site.register(Stand, StandAdmin)
