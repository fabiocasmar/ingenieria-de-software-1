# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import datetime

from estacionamientos.models import TarifaHorayFraccion
        


###################################################################
# TARIFA HORA Y FRACCION
###################################################################

class TarifaHoraFraccionTestCase(TestCase):

    #Pruebas para tarifa de hora y fraccion

    def test_tarifa_hora_y_fraccion_una_hora(self):
        initial_time = datetime(2015,2,18,13,0)
        final_time = datetime(2015,2,18,14,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)

    def test_tarifa_hora_y_fraccion_una_dos_horas(self):
        initial_time = datetime(2015,2,18,13,0)
        final_time = datetime(2015,2,18,15,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),4)

    def test_tarifa_hora_y_fraccion_media_hora(self):
        initial_time = datetime(2015,2,18,13,15)
        final_time = datetime(2015,2,18,13,45)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)

    def test_tarifa_hora_y_fraccion_una_hora_mas_media_hora(self):
        initial_time = datetime(2015,2,18,13,0)
        final_time = datetime(2015,2,18,14,30)
        rate = TarifaHorayFraccion(tarifa = 20)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),30)

    def test_tarifa_hora_y_fraccion_una_hora_fraccion_15_minutos(self):
        initial_time = datetime(2015,2,18,19,0)
        final_time = datetime(2015,2,18,20,15)
        rate = TarifaHorayFraccion(tarifa = 1)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1.5)

    def test_tarifa_hora_y_fraccion_una_hora_mas_media_hora_mas_1_minuto(self):
        initial_time = datetime(2015,2,18,15,15)
        final_time = datetime(2015,2,18,16,46)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),4)
        
    def test_tarifa_hora_y_fraccion_un_dia(self): # Normal
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),48)

    def test_tarifa_hora_y_fraccion_un_dia_menos_un_minuto(self): # Borde
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,18,23,59)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),48)

    def test_tarifa_hora_y_fraccion_un_dia_mas_un_minuto(self): # Borde
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,1)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)

    def test_tarifa_hora_y_fraccion_un_dia_mas_media_hora(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,30)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)

    def test_tarifa_hora_y_fraccion_un_dia_mas_media_hora_mas_un_minuto(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,31)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),50)

    def test_tarifa_hora_y_fraccion_un_dia_antes_de_la_medianoche_mas_un_minuto(self):
        initial_time = datetime(2015,2,18,23,59)
        final_time = datetime(2015,2,20,0,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)

    def test_tarifa_hora_y_fraccion_un_dia_treinta_minutos_antes_de_la_medianoche_mas_treinta_minutos(self):
        initial_time = datetime(2015,2,18,23,30)
        final_time = datetime(2015,2,20,0,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)

    def test_tarifa_hora_y_fraccion_un_dia_treinta_minutes_antes_de_la_medianoche_mas_treinta_y_un_minutos(self):
        initial_time = datetime(2015,2,18,23,30)
        final_time = datetime(2015,2,20,0,1)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),50)

    def test_tarifa_hora_y_fraccion_dos_dias(self):
        initial_time = datetime(2015,2,18,6,30)
        final_time = datetime(2015,2,20,6,30)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),96)

    def test_tarifa_hora_y_fraccion_dos_dias_mas_un_minuto(self):
        initial_time = datetime(2015,2,18,6,30)
        final_time = datetime(2015,2,20,6,31)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),97)

    def test_tarifa_hora_y_fraccion_siete_dias(self): # Esquina
        initial_time = datetime(2015,2,18,6,30)
        final_time = datetime(2015,2,25,6,30)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),7*24*2)
