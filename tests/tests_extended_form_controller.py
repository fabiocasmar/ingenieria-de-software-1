# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time

from estacionamientos.controller import HorarioEstacionamiento
        
######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
######################################################################

class ExtendedFormControllerTestCase(TestCase):
    
    # TDD
    def test_HorariosValidos(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        self.assertTrue(HorarioEstacionamiento(HoraInicio, HoraFin))

    # malicia
    def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 11, minute = 0, second = 0)
        self.assertFalse(HorarioEstacionamiento(HoraInicio, HoraFin))

    # caso borde
    def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 12, minute = 0, second = 0)
        self.assertFalse(HorarioEstacionamiento(HoraInicio, HoraFin))

    # caso borde
    def test_Limite_HorarioValido_Apertura_Cierre(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 12, minute = 0, second = 1)
        self.assertTrue(HorarioEstacionamiento(HoraInicio, HoraFin))

    # caso esquina
    def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
        HoraInicio = time(hour = 0, minute = 0, second = 0)
        HoraFin = time(hour = 23, minute = 59, second = 59)
        self.assertTrue(HorarioEstacionamiento(HoraInicio, HoraFin))