# -*- coding: utf-8 -*-

from django.test import TestCase

from xmlrpc.client import MAXINT

from estacionamientos.forms import MovimientosForm

###################################################################
# ESTACIONAMIENTO_MOVIMIENTOS_FORM
###################################################################

class MovimientosFormTestCase(TestCase):
	# malicia
	def test_Movimientos_vacia(self):
		form_data = {}
		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_Movimientos_UnCampo_ID(self):
		form_data = {'billetera_id': 11}
		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_Movimientos_UnCampo_PIN(self):
		form_data = {'pin': '19u1t'}
		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())

	#TDD
	def test_Movimientos_CamposBien(self):
		form_data = {
					 'billetera_id' : 11,
				 	 'pin': '19u1t'
				}
		form = MovimientosForm(data = form_data)
		self.assertTrue(form.is_valid())

	#caso borde
	def test_Movimientos_ID_Invalido(self):
		form_data = {
					 'billetera_id' : 'susa',
				 	 'pin': '19u1t'
					}
		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_Movimientos_ID_0(self):
		form_data = {
					 'billetera_id' : 0,
					 'pin': '19u1t',
					}

		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_Movimientos_PIN_Invalido_Mas_digitos(self):
		form_data = {
					 'billetera_id' : 11,
					 'pin': '4519u1t'
					}
		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_Movimientos_PIN_Invalido_Menos_digitos(self):
		form_data = {
					 'billetera_id' : 11,
					 'pin': '45t',
					}
		form = MovimientosForm(data = form_data)
		self.assertFalse(form.is_valid())
