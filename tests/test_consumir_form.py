# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import (
        ConsumirForm
)

###################################################################
#                          ConsumirBilletera Form                 #
###################################################################

class ConsumirBilleteraFormTestCase(TestCase):

	# Borde
	def test_ConsumirBilletera_FormVacio(self):
		form_data = {}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_FormUnCampo_Id(self):
		form_data = {
			'billetera_id': 42
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_FormUnCampo_PIN(self):
		form_data = {
			'pin': '04235'
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_FormUnCampo_Monto(self):
		form_data = {
			'monto': 20.50
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_FormDosCampo_Id_PIN(self):
		form_data = {
			'billetera_id': 5,
			'pin': 'cv123'
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_FormDosCampo_Id_Monto(self):
		form_data = {
			'billetera_id': 5,
			'monto': 123.10
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_FormDosCampo_PIN_Monto(self):
		form_data = {
			'pin': '222s',
			'monto': 123.10
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# TDD
	def test_ConsumirBilletera_FormTodosLosCampos(self):
		form_data = {
			'billetera_id': 1,
			'pin': 'xy59',
			'monto': 3.00
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_ConsumirBilletera_Form_MontoSinDecimales(self):
		form_data = {
			'billetera_id': 155,
			'pin': 'lalala',
			'monto': 132
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# Borde
	def test_ConsumirBilletera_Form_MontoTresDecimales(self):
		form_data = {
			'billetera_id': 155,
			'pin': 'lalala',
			'monto': 132.333
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	# Borde
	def test_ConsumirBilletera_Form_IdCero(self):
		form_data = {
			'billetera_id': 0,
			'pin': 'xy59',
			'monto': 30
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Malicia
	def test_ConsumirBilletera_Form_IdInvalidoLetrasNumeros(self):
		form_data = {
			'billetera_id': 'id123',
			'pin': 'xy59',
			'monto': 100
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Malicia
	def test_ConsumirBilletera_Form_IdInvalidoLetras(self):
		form_data = {
			'billetera_id': 'billetera',
			'pin': 'xy59',
			'monto': 130
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_Form_PinMasCorto(self):
		form_data = {
			'billetera_id': 103,
			'pin': 'bcvn',
			'monto': 30.56
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# Borde
	def test_ConsumirBilletera_Form_PinMasLargo(self):
		form_data = {
			'billetera_id': 33,
			'pin': 'z1092z',
			'monto': 98.4
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# Borde
	def test_ConsumirBilletera_Form_PinMasCortoMenos1(self):
		form_data = {
			'billetera_id': 405,
			'pin': 'xyz',
			'monto': 3.50
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_Form_PinMasLargoMas1(self):
		form_data = {
			'billetera_id': 223,
			'pin': '0987aab',
			'monto': 42.10
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())

	# Borde
	def test_ConsumirBilletera_Form_PinConSimbolos(self):
		form_data = {
			'billetera_id': 22,
			'pin': '$zy5@',
			'monto': 37.98
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# Borde
	def test_MontoEnteroMasGrandeRepresentable(self):
		form_data = {
			'billetera_id': 909,
			'pin': '123ab',
			'monto': 2**32 - 1
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# Borde
	def test_MontoEnteroMasGrandeRepresentableMas1(self):
		form_data = {
			'billetera_id': 'billetera',
			'pin': '456dfg',
			'monto': 2**32 + 1
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())


	# Borde
	def test_ConsumirBilletera_Form_MontoCero(self):
		form_data = {
			'billetera_id': 666,
			'pin': 'pin22',
			'monto': 0.00
		}
		form = ConsumirForm(data = form_data)
		self.assertTrue(form.is_valid())

	# Malicia
	def test_ConsumirBilletera_Form_MontoNegativo(self):
		form_data = {
			'billetera_id': 666,
			'pin': 'mmmzs',
			'monto': -0.01
		}
		form = ConsumirForm(data = form_data)
		self.assertFalse(form.is_valid())