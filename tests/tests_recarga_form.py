# -*- coding: utf-8 -*-

from django.test import TestCase

from xmlrpc.client import MAXINT

from estacionamientos.forms import RecargaForm

###################################################################
# ESTACIONAMIENTO_RECARGA_FORM
###################################################################

class RecargaFormTestCase(TestCase):
	# malicia
	def test_Recarga_vacia(self):
		form_data = {}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# caso borde
	def test_RecargarSaldo_UnCampo_ID(self):
		form_data = {'billetera_id': 11}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_PIN(self):
		form_data = {'pin': '19u1t'}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_MONTO(self):
		form_data = {'monto': 345.08}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_Nombre(self):
		form_data = {'nombre': 'Marisela'}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_APELLIDO(self):
		form_data = {'apellido': 'Del Valle'}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_CI(self):
		form_data = {'cedula' : 'V-23638870'}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_TARJETATIPO(self):
		form_data = {'tarjetaTipo': 'Vista'}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_UnCampo_TARJETA(self):
		form_data = {'tarjeta': 1111111111111111}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_ID_PIN(self):
		form_data = {'billetera_id': 11,
					 'pin' : '19u1t'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_ID_MONTO(self):
		form_data = {'billetera_id': 11,
					 'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_PIN_MONTO(self):
		form_data = {'pin': '19u1t',
					 'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#TDD
	def test_RecargarSaldo_CamposBien(self):
		form_data = {	'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 11,
					 	'pin': '19u1t',
					 	'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertTrue(form.is_valid())

	#caso borde
	def test_RecargarSaldo_ID_Invalido(self):
		form_data = {	'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 'susa',
					 	'pin': '19u1t',
					 	'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_ID_0(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 0,
					 'pin': '19u1t',
					 'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_PIN_Invalido_Mas_digitos(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 11,
						 'pin': '4519u1t',
						 'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_PIN_Invalido_Menos_digitos(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '45t',
					 'monto' : 345.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_MONTO_Invalido(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 11,
						 'pin': '19u1t',
						 'monto' : -345
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_NOMBRE_Invalido(self):
		form_data = {'nombre' : 'Marisela1',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 11,
						 'pin': '19u1t',
						 'monto' : 345
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_APELLIDO_Invalido(self):
		form_data = {'nombre' : 'Marisela1',
						'apellido' : 'Del Valle1',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 11,
						 'pin': '19u1t',
						 'monto' : 345
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_TARJETATIPO_Invalido(self):
		form_data = {'nombre' : 'Marisela1',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vis',
						'tarjeta' : 1111111111111111,
						'billetera_id' : 11,
						 'pin': '19u1t',
						 'monto' : 345
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())
	#malicia
	def test_RecargarSaldo_TARJETA_Invalido(self):
		form_data = {'nombre' : 'Marisela1',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111,
						'billetera_id' : 11,
						 'pin': '19u1t',
						 'monto' : 345
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_MONTO_Invalido_Decimal(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19u1t',
					 'monto' : -0.03
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_MONTO_Invalido_NoNumeros(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19u1t',
					 'monto' : 'a'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_CamposMAl(self):
		form_data = {'nombre' : 'Marisela1',
						'apellido' : 'Del1Valle',
						'cedula' : '23638870',
						'tarjetaTipo' : None,
						'tarjeta' : 11111111111111,
					'billetera_id' : None,
					 'pin': '19u1345gt',
					 'monto' : -8
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_DosCamposMAl_PIN_MONTO(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19u1312d',
					 'monto' : -8
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_DosCamposMAl_PIN_ID(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : None,
					 'pin': '19u1389o',
					 'monto' : 8.00
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#malicia
	def test_RecargarSaldo_DosCamposMAl_MONTO_ID(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : None,
					 'pin': '19u1',
					 'monto' : -8.00
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#borde
	def test_RecargarSaldo_MONTO_PIN_Extremos(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19u11d',
					 'monto' : MAXINT
					}
		form = RecargaForm(data = form_data)
		self.assertTrue(form.is_valid())

	#borde 
	def test_RecargarSaldo_MONTO_ExtremosMinDecimal(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19ud',
					 'monto' : 0.01
					}
		form = RecargaForm(data = form_data)
		self.assertTrue(form.is_valid())

	#borde
	def test_RecargarSaldo_MONTO_ExtremosMin(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19ud',
					 'monto' : 0
					}
		form = RecargaForm(data = form_data)
		self.assertTrue(form.is_valid())

	# TDD
	def test_Recarga_3Decimales(self):
		form_data = {'nombre' : 'Marisela',
						'apellido' : 'Del Valle',
						'cedula' : 'V-23638870',
						'tarjetaTipo' : 'Vista',
						'tarjeta' : 1111111111111111,
					'billetera_id' : 11,
					 'pin': '19ud',
					 'monto' : 9.012
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())
		
