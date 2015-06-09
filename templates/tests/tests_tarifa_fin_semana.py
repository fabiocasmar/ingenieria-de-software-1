# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import (
    datetime,
    timedelta
)

from estacionamientos.models import TarifaFinDeSemana

###################################################################
# Tarifa diferenciada para fines de semana
###################################################################

class FinDeSemanaTestCase(TestCase):
    # Bordes:   6 * 11
    # Esquinas: 2
    # Malicia:  2 * 10

    # Semana 2015-03-(09..15):
    # Lu Ma Mi Ju Vi Sá Do
    # 09 10 11 12 13 14 15
    # Semana 2015-03-(16..15):
    # Lu Ma Mi Ju Vi Sá Do
    # 16 17 18 19 20 21 22
    def test_tarifa_fin_de_semana_n_horas_desde_la_medianoche_antes_del_lunes(self): #(11) bordes
        for n in range(11):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            inicioReserva = datetime(2015,3,9,0,0) #medianoche domingo-lunes
            finReserva = inicioReserva + timedelta(hours=n+1) # n+1 horas más tarde
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor,2*(n+1))

    def test_tarifa_fin_de_semana_n_horas_hasta_la_medianoche_antes_del_sabado(self): #(11) bordes
        for n in range(11):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            finReserva = datetime(2015,3,14,0,0) #medianoche viernes-sábado
            inicioReserva = finReserva - timedelta(hours=n+1) # n+1 horas más temprano
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor,2*(n+1))

    def test_tarifa_fin_de_semana_n_horas_desde_la_medianoche_antes_del_sabado(self): #(11) bordes
        for n in range(11):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            inicioReserva = datetime(2015,3,14,0,0) #medianoche viernes-sábado
            finReserva = inicioReserva + timedelta(hours=n+1) # n+1 horas más tarde
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor,5*(n+1))

    def test_tarifa_fin_de_semana_n_horas_hasta_la_medianoche_antes_del_lunes(self): #(11) bordes
        for n in range(11):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            finReserva = datetime(2015,3,9,0,0) #medianoche domingo-lunes
            inicioReserva = finReserva - timedelta(hours=n+1) # n+1 horas más temprano
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor,5*(n+1))

    def test_tarifa_fin_de_semana_semana_de_trabajo_completa(self): #esquina
        tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
        inicioReserva = datetime(2015,3,9,0,0) #medianoche domingo-lunes
        finReserva = datetime(2015,3,14,0,0) #medianoche viernes-sábado
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,2*24*5)

    def test_tarifa_fin_de_semana_fin_de_semana_completo(self): #esquina
        tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
        inicioReserva = datetime(2015,3,14,0,0) #medianoche viernes-sábado
        finReserva = datetime(2015,3,16,0,0) #medianoche domingo-lunes
        valor = tarifa.calcularPrecio(inicioReserva,finReserva)
        self.assertEqual(valor,5*24*2)

    def test_tarifa_fin_de_semana_n_horas_domingo_lunes(self): #(11) bordes
        for n in range(11):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            inicioReserva = datetime(2015,3,15,14,0) + timedelta(hours=n) #domingo en la tarde
            finReserva = inicioReserva + timedelta(hours=10) # diez horas más tarde
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor, 5*(10-n) + 2*n)

    def test_tarifa_fin_de_semana_n_horas_viernes_sabado(self): #(11) bordes
        for n in range(11):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            inicioReserva = datetime(2015,3,13,14,0) + timedelta(hours=n) #viernes en la tarde
            finReserva = inicioReserva + timedelta(hours=10) # diez horas más tarde
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor, 2*(10-n) + 5*n)

    def test_tarifa_fin_de_semana_n_horas_domingo_lunes_empezando_a_un_cuarto_de_hora(self): #(10) malicia
        for n in range(10):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            inicioReserva = datetime(2015,3,15,14,15) + timedelta(hours=n) #domingo en la tarde
            finReserva = inicioReserva + timedelta(hours=10) # diez horas más tarde
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor, 5*(9.75-n) + 2*(n+.25))

    def test_tarifa_fin_de_semana_n_horas_viernes_sabado_empezando_a_un_cuarto_de_hora(self): #(10) malicia
        for n in range(10):
            tarifa = TarifaFinDeSemana(tarifa=2,tarifa2=5)
            inicioReserva = datetime(2015,3,13,14,15) + timedelta(hours=n) #viernes en la tarde
            finReserva = inicioReserva + timedelta(hours=10) # diez horas más tarde
            valor = tarifa.calcularPrecio(inicioReserva,finReserva)
            self.assertEqual(valor, 2*(9.75-n) + 5*(n+.25))
