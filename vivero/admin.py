from django.contrib import admin

from vivero.models import *

# Register your models here.
admin.site.register(Productor)
admin.site.register(Finca)
admin.site.register(Vivero)
admin.site.register(Labor)
admin.site.register(ProductoControlHongo)
admin.site.register(ProductoControlPlaga)
admin.site.register(ProductoControlFertilizante)
admin.site.register(LaborProductoControl)