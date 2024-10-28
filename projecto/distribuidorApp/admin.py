from django.contrib import admin
from distribuidorApp.models import Distribuidor

class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ['telefono', 'email', 'ciudad', 'fechaDespacho', 'fechaRecepcion']
# Register your models here.
admin.site.register(Distribuidor, DistribuidorAdmin)