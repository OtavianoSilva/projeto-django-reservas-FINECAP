from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nome", "estoque", "faturamento"]
admin.site.register(Empresa, EmpresaAdmin)