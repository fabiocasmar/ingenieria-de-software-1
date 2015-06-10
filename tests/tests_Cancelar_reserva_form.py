# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import CancelarReservaForm

###################################################################
# ESTACIONAMIENTO_RECARGA_FORM
###################################################################

class CancelarReservaFormTestCase(TestCase):
	# malicia
	def test_CancelarReserva_vacia(self):
		form_data = {}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CancelarReserva_UnCampo_CI(self):
		form_data = {'Cédula': 'V-24287498'}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CancelarReserva_UnCampo_numeroPago(self):
		form_data = {'numero_pago': 123}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CancelarReserva_UnCampo_ID(self):
		form_data = {'billetera_id': 1}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CancelarReserva_UnCampo_PIN(self):
		form_data = {'pin': '12es'}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_DosCampos_CI_numeroPago(self):
		form_data = {'Cédula': 'V-24287497',
					 'numero_pago' : 12
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_DosCampos_ID_PIN(self):
		form_data = {'billetera_id': 1,
					 'pin' : '1es2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_DosCampos_CI_PIN(self):
		form_data = {'Cédula': 'V-24287434',
					 'pin' : '1es2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_DosCampos_numeroPago_ID(self):
		form_data = {'numero_pago' : 12,
					 'billetera_id': 1
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_DosCampos_CI_ID(self):
		form_data = {'Cédula': 'V-24287434',
					 'billetera_id': 1
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_DosCampos_numeroPago_PIN(self):
		form_data = {'numero_pago' : 12,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())