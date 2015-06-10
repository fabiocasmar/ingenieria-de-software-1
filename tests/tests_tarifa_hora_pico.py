# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import (
    datetime,
    time
)

from estacionamientos.models import TarifaHoraPico

###################################################################
# Tarifa por minuto con hora pico
###################################################################

class HoraPicoTestCase(TestCase):

    def test_tarifa_hora_pico_valle_de_una_hora(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=120,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,4)
        finReserva = datetime(2015,1,1,5)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,60)

    def test_tarifa_hora_pico_valle_valle_por_media_hora(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=120,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,4,30)
        finReserva = datetime(2015,1,1,5)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,30)

    def test_tarifa_hora_pico_valle_valle_por_cuarto_de_hora(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=120,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,4,45)
        finReserva = datetime(2015,1,1,5)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,15)

    def test_tarifa_hora_pico_valle_pico_por_una_hora(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=120,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,7)
        finReserva = datetime(2015,1,1,8)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,120)

    def test_tarifa_hora_pico_valle_pico_por_media(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,7,30)
        finReserva = datetime(2015,1,1,8)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,50)

    def test_tarifa_hora_pico_valle_pico_por_15_minutos(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,7,45)
        finReserva = datetime(2015,1,1,8)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,25)

    def test_tarifa_hora_pico_valle_una_hora_mitad_y_mitad(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,5,30)
        finReserva = datetime(2015,1,1,6,30)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,80)

    def test_tarifa_hora_pico_valle_una_hora_15_minutos_y_3_cuartos_de_hora(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,5,45)
        finReserva = datetime(2015,1,1,6,45)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,90)

    def test_tarifa_hora_pico_valle_dos_horas_diferentes_dias(self):
        inicio = time(0,0)
        fin = time(12,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,23)
        finReserva = datetime(2015,1,2,1)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,160)

    ###################
    #      Bordes
    ###################

    def test_tarifa_hora_pico_valle_borde_inferior_de_valle(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,5)
        finReserva = datetime(2015,1,1,6)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,60)

    def test_tarifa_hora_pico_valle_borde_superior_de_pico(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,18)
        finReserva = datetime(2015,1,1,19)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,60)

    def test_tarifa_hora_pico_valle_borde_inferior_de_pico(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,6)
        finReserva = datetime(2015,1,1,7)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,100)

    def test_tarifa_hora_pico_valle_pico_debajo_de_un_borde(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=100,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,17)
        finReserva = datetime(2015,1,1,18)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,100)

    def test_tarifa_hora_pico_valle_valle_de_un_minuto(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=120,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,5,59)
        finReserva = datetime(2015,1,1,6,59)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,119)

    def test_tarifa_hora_pico_valle_pico_de_un_minuto(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa=60,tarifa2=120,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,5,1)
        finReserva = datetime(2015,1,1,6,1)
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,61)
