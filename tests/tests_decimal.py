# -*- coding: utf-8 -*-

from django.test import TestCase

from decimal import Decimal

from datetime import (
    datetime,
    time
)

from estacionamientos.models import (
    TarifaMinuto,
    TarifaHora,
    TarifaHorayFraccion,
    TarifaFinDeSemana,
    TarifaHoraPico
)
        


###################################################################
# Casos de prueba de tipos de tarifa
###################################################################

class DecimalTestCase(TestCase):

    # Casos de decimales

    def test_tarifa_hora_decimal(self):
        rate=TarifaHora(tarifa=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,0)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, Decimal('0.9'))

    def test_tarifa_minuto_decimal(self):
        rate=TarifaMinuto(tarifa=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,30)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, Decimal('1.05'))

    def test_tarifa_hora_y_fraccion_decimal(self):
        rate=TarifaHorayFraccion(tarifa=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,17,25)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, Decimal('0.75'))
        
    def test_tarifa_pico_decimal(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=0.1,tarifa2=0.3,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,15)
        finReserva = datetime(2015,1,1,20)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,Decimal('1.10'))
        
    def test_tarifa_fin_de_semana_decimal(self):
        tarifa = TarifaFinDeSemana(tarifa=0.1,tarifa2=0.3)
        inicioReserva = datetime(2015,3,6,22)
        finReserva = datetime(2015,3,7,3)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,Decimal('1.10'))