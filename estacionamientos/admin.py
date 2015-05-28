# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, Reserva, Pago, TarifaMinuto,\
    TarifaHorayFraccion, TarifaHora, Propietario

admin.site.register(Estacionamiento)
admin.site.register(Propietario)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(TarifaHora)
admin.site.register(TarifaMinuto)
admin.site.register(TarifaHorayFraccion)