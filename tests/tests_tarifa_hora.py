# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import datetime

from estacionamientos.models import TarifaHora
        


###################################################################
# Casos de prueba de tipos de tarifa
###################################################################

class TarifaHoraTestCase(TestCase):

    # Pruebas para la clase tarifa hora

    def test_tarifa_hora_una_hora(self): # TDD
        rate = TarifaHora(tarifa = 800)
        initial_datetime = datetime(2015,2,18,13,0)
        final_datetime = datetime(2015,2,18,14,0)
        value = rate.calcularPrecio(initial_datetime, final_datetime)
        self.assertEquals(value, 800)

    def test_tarifa_hora_mas_de_una_hora(self): # TDD
        rate = TarifaHora(tarifa = 800)
        initial_datetime = datetime(2015,2,18,6,8)
        final_datetime = datetime(2015,2,18,7,9)
        value = rate.calcularPrecio(initial_datetime, final_datetime)
        self.assertEquals(value, 1600)

    def test_tarifa_hora_menos_de_una_hora(self): # Borde
        rate = TarifaHora(tarifa = 800)
        initial_datetime = datetime(2015,2,18,11,0)
        final_datetime = datetime(2015,2,18,11,15)
        value = rate.calcularPrecio(initial_datetime, final_datetime)
        self.assertEquals(value, 800)

    def test_tarifa_hora_dia_completo_menos_un_minuto(self): # Borde
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,18,23,59)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 24)

    def test_tarifa_hora_dia_completo(self): # Borde
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,19,0,0)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 24)

    def test_dia_completo_mas_un_minuto(self):
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,19,0,1)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 25)

    def test_tarifa_hora_siete_dias(self):
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,25,0,0)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 24*7)