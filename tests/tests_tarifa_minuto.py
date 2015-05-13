# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import datetime

from estacionamientos.models import TarifaMinuto
        


###################################################################
# TARIFA POR MINUTO
###################################################################

class TarifaMinutoTestCase(TestCase):

    # Pruebas para la tarifa por minuto

    def test_tarifa_minuto_un_minuto(self): # Borde
        initial_time = datetime(2015,2,18,15,1)
        final_time = datetime(2015,2,18,15,2)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1)

    def test_tarifa_minuto_dos_minutos(self): # TDD
        initial_time = datetime(2015,2,18,15,1)
        final_time = datetime(2015,2,18,15,3)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)

    def test_tarifa_minuto_una_hora(self): # Borde
        initial_time = datetime(2015,2,18,15,0)
        final_time = datetime(2015,2,18,16,0)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),60)


    def test_tarifa_minuto_un_dia_menos_un_minuto(self): # Borde
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,18,23,59)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1439)

    def test_tarifa_minuto_un_dia(self): # Borde
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,0)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1440)

    def test_tarifa_minuto_un_dia_mas_un_minuto(self): # TDD
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,1)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1441)

    def test_tarifa_minuto_un_dia_antes_de_la_medianoche_mas_un_minuto(self): # Borde
        initial_time = datetime(2015,2,18,23,59)
        final_time = datetime(2015,2,20,0,0)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1441)

    def test_tarifa_minuto_siete_dias(self): # Esquina
        initial_time = datetime(2015,2,18,23,59)
        final_time = datetime(2015,2,25,23,59)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),7*24*60)