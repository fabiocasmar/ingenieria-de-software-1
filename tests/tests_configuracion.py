# -*- coding: utf-8 -*- 

from django.test import TestCase

from estacionamientos.controller import  guardar_configuracion
from estacionamientos.models import (
                                        Sage
                                    )

###################################################################
#             CONFIGURAR SAGE VISTA DISPONIBLE
###################################################################

class CongiguracionSageTestCase(TestCase):

	# TDD
	def test_configuracion_nueva(self):
		sePuede = guardar_configuracion (1.00)
		self.assertTrue(sePuede[0])

	# Malicia
	def test_sobreescribir_configuracion(self):
		sage =Sage(
			deduccion = 0.00
		)
		sage.save()
		sePuede = guardar_configuracion (1.00)
		self.assertTrue(sePuede[0])

	# Borde
	def test_deduccion_maxima(self):
		sePuede = guardar_configuracion (10.00)
		self.assertTrue(sePuede[0])

	# Borde
	def test_deduccion_minima(self):
		sePuede = guardar_configuracion (0.00)
		self.assertTrue(sePuede[0])

	# Malicia
	def test_deduccion_erronea(self):
		sePuede = guardar_configuracion (10.01)
		self.assertFalse(sePuede[0])

	# Malicia
	def test_deduccion_erronea(self):
		sePuede = guardar_configuracion (-0.01)
		self.assertFalse(sePuede[0])	
