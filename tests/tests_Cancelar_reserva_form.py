# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import CancelarReservaForm

###################################################################
#             ESTACIONAMIENTO_CANCELAR_RESERVA_FORM
###################################################################

class CancelarReservaFormTestCase(TestCase):
	# malicia
	def test_CancelarReserva_vacia(self):
		form_data = {}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_CancelarReserva_UnCampo_CI(self):
		form_data = {'cedula': 'V-24287498'}
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
		form_data = {'cedula': 'V-24287497',
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
		form_data = {'cedula': 'V-24287434',
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
		form_data = {'cedula': 'V-24287434',
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

	#caso borde
	def test_CancelarReserva_TresCampos_CI_numeroPago_ID(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 12,
					 'billetera_id': 1
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_TresCampos_CI_numeroPago_PIN(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 12,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_TresCampos_numeroPago_ID_PIN(self):
		form_data = {'numero_pago' : 12,
					 'billetera_id': 1,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_TresCampos_CI_ID_PIN(self):
		form_data = {'cedula': 'V-24287434',
					 'billetera_id': 1,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#TDD
	def test_CancelarReserva_TodosCamposBien_CI_Extranjera(self):
		form_data = {'cedula': 'E-24287434',
					 'numero_pago' : 12,
					 'billetera_id': 1,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertTrue(form.is_valid())

	#TDD
	def test_CancelarReserva_TodosCamposBien_CI_Venezolana(self):
		form_data = {'cedula': 'V-287434',
					 'numero_pago' : 12,
					 'billetera_id': 1,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertTrue(form.is_valid())

	#malicia
	def test_CancelarReserva_TodosCamposMal(self):
		form_data = {'cedula': 24287434,
					 'numero_pago' : 0,
					 'billetera_id': 'e1',
					 'pin': '1s'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_1CampoMal_CI(self):
		form_data = {'cedula': None,
					 'numero_pago' : 12,
					 'billetera_id': 1,
					 'pin': '1se3'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_1CampoMal_numeroPago(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 0,
					 'billetera_id': 1,
					 'pin': '1s2w'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_1CampoMal_ID(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 11,
					 'billetera_id': 'e1',
					 'pin': '1sd4'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_1CampoMal_PIN(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 12,
					 'billetera_id': 1,
					 'pin': '1s'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_2CamposMal_CI_numeroPago(self):
		form_data = {'cedula': 2678897,
					 'numero_pago' : 0,
					 'billetera_id': 1,
					 'pin': '1se2'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_2CamposMal_ID_PIN(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 12,
					 'billetera_id': 'e1',
					 'pin': '1s'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_2CamposMal_CI_PIN(self):
		form_data = {'cedula': None,
					 'numero_pago' : 12,
					 'billetera_id': 1,
					 'pin': '1s'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_2CamposMal_numeroPago_ID(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 0,
					 'billetera_id': 'e1',
					 'pin': '112s'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_2CamposMal_CI_ID(self):
		form_data = {'cedula': None,
					 'numero_pago' : 12,
					 'billetera_id': 'e1',
					 'pin': '1sed'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_2CamposMal_numeroPago_PIN(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 0,
					 'billetera_id': 1,
					 'pin': '7ujn3ergs'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_3CamposMal_CI_numeroPago_ID(self):
		form_data = {'cedula': None,
					 'numero_pago' : 0,
					 'billetera_id': 'e1',
					 'pin': '1234fs'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_3CamposMal_numeroPago_ID_PIN(self):
		form_data = {'cedula': 'V-24287434',
					 'numero_pago' : 0,
					 'billetera_id': 'e1',
					 'pin': '1s'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_3CamposMal_CI_ID_PIN(self):
		form_data = {'cedula': None,
					 'numero_pago' : 13,
					 'billetera_id': 'e1',
					 'pin': '1s7890ol'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_CancelarReserva_Llenos_3CamposMal_CI_numeroPago_PIN(self):
		form_data = {'cedula': None,
					 'numero_pago' : 0,
					 'billetera_id': 1,
					 'pin': '1s7890ol'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_CancelarReserva_PIN_4caracteres(self):
		form_data = {'cedula': 'V-23456789',
					 'numero_pago' : 14,
					 'billetera_id': 1,
					 'pin': '1s78'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertTrue(form.is_valid())

	#caso borde
	def test_CancelarReserva_PIN_6caracteres(self):
		form_data = {'cedula': 'V-23456789',
					 'numero_pago' : 14,
					 'billetera_id': 1,
					 'pin': '1s7er8'
					}
		form = CancelarReservaForm(data = form_data)
		self.assertTrue(form.is_valid())
