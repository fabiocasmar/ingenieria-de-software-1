# -*- coding: utf-8 -*-

from django.test import TestCase

from xmlrpc.client import MAXINT

from estacionamientos.forms import CambiarPinForm

###################################################################
# 				ESTACIONAMIENTO_CAMBIAR_PIN_FORM
###################################################################

class CambiarPinFormTestCase(TestCase):
	# malicia
	def test_CambioPin_vacio(self):
		form_data = {}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_UnCampo_ID(self):
		form_data = {'billetera_id': 11}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_UnCampo_PIN(self):
		form_data = {'pin': '123d'}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_UnCampo_NuevoPIN(self):
		form_data = {'nuevoPin': '123e'}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_UnCampo_NuevoPIN2(self):
		form_data = {'nuevoPin2': '123e'}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_DosCampos_ID_PIN(self):
		form_data = {'billetera_id': 11,
					 'pin' : '123d'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_DosCampos_ID_NuevoPIN(self):
		form_data = {'billetera_id': 11,
					 'nuevoPin' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_DosCampos_ID_NuevoPIN2(self):
		form_data = {'billetera_id': 11,
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_DosCampos_PIN_nuevoPin(self):
		form_data = {'pin' : '123d',
					 'nuevoPin' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_DosCampos_PIN_nuevoPin2(self):
		form_data = {'pin' : '123d',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_DosCampos_nuevoPin_nuevoPin2(self):
		form_data = {'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_TresCampos_ID_PIN_nuevoPin(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_TresCampos_ID_PIN_nuevoPin2(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_TresCampos_PIN_nuevoPin_nuevoPin2(self):
		form_data = {'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_TresCampos_ID_nuevoPin_nuevoPin2(self):
		form_data = {'billetera_id' : 11,
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# TDD
	def test_CambiarPin_TodosCamposBien(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())

	# malicia
	def test_CambiarPin_TodosCamposMal(self):
		form_data = {'billetera_id' : 'kl',
					 'pin' : '123d3456',
					 'nuevoPin' : '23456789',
					 'nuevoPin2' : '123epklom'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_1CampoMal_ID(self):
		form_data = {'billetera_id' : 'kl',
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_1CampoMal_PIN(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d1111111',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_1CampoMal_nuevoPin(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '23456789',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_1CampoMal_nuevoPin2(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '12312567890'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_2CamposMal_ID_PIN(self):
		form_data = {'billetera_id' : 'kl',
					 'pin' : '23456789',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_2CamposMal_ID_nuevoPin(self):
		form_data = {'billetera_id' : 'kl',
					 'pin' : '123d',
					 'nuevoPin' : '123e345678',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_2CamposMal_ID_nuevoPin2(self):
		form_data = {'billetera_id' : 'kl',
					 'pin' : '123d23455',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '1234566889'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_2CamposMal_PIN_nuevoPin(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '23456789',
					 'nuevoPin' : '123e12ws',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_2CamposMal_PIN_nuevoPin2(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '23456789',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '23456ed789'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_2CamposMal_nuevoPin_nuevoPin(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e12ws',
					 'nuevoPin2' : '123dfghjke'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_3CamposMal_ID_PIN_nuevoPin(self):
		form_data = {'billetera_id' : '123',
					 'pin' : '12345689',
					 'nuevoPin' : '123e12ws',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_3CamposMal_ID_PIN_nuevoPin2(self):
		form_data = {'billetera_id' : '123',
					 'pin' : '12345689',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e12ws'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_3CamposMal_ID_nuevoPin_nuevoPin2(self):
		form_data = {'billetera_id' : '123',
					 'pin' : '123d',
					 'nuevoPin' : '12334567890m',
					 'nuevoPin2' : '123e12ws'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_TodosLlenos_3CamposMal_PIN_nuevoPin_nuevoPin2(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '12345689',
					 'nuevoPin' : '123wedfe',
					 'nuevoPin2' : '123e12ws'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# TDD
	def test_CambiarPin_Pin4caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_CambiarPin_nuevoPin4caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_CambiarPin_nuevoPin2_4caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_CambiarPin_Pin6caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123def',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_CambiarPin_nuevoPin6caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123efg',
					 'nuevoPin2' : '123efg'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_CambiarPin_nuevoPin2_6caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123efg',
					 'nuevoPin2' : '123efg'
					}
		form = CambiarPinForm(data = form_data)
		self.assertTrue(form.is_valid())


	# caso borde
	def test_CambiarPin_Pin3caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_nuevosPin_3caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123',
					 'nuevoPin2' : '123'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_Pin7caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123defg',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CambiarPin_nuevosPin_7caracteres(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123efgh',
					 'nuevoPin2' : '123efgh'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_ID_cero(self):
		form_data = {'billetera_id' : 0,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123e'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_CambiarPin_nuevosPin_Diferentes(self):
		form_data = {'billetera_id' : 11,
					 'pin' : '123d',
					 'nuevoPin' : '123e',
					 'nuevoPin2' : '123efgh'
					}
		form = CambiarPinForm(data = form_data)
		self.assertFalse(form.is_valid())


