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
	def test_RecargarSaldo_UnCampo_Apellido(self):
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

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_apellido(self):
		form_data = {'nombre': 'Susana',
					 'apellido' : 'Del Valle'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_CI(self):
		form_data = {'nombre': 'Susana',
					 'cedula' : 'V-23653456'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_tarjetaTipo(self):
		form_data = {'nombre': 'Susana',
					 'tarjetaTipo' : 'Vista'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_tarjeta(self):
		form_data = {'nombre': 'Susana',
					 'tarjeta' : 0111111222233334
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_ID(self):
		form_data = {'nombre': 'Susana',
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_PIN(self):
		form_data = {'nombre': 'Susana',
					 'pin' : 'a456'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_nombre_monto(self):
		form_data = {'nombre': 'Susana',
					 'monto' : 23.09
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_apellido_CI(self):
		form_data = {'apellido': 'Roma',
					 'cedula' : 'V-23653456'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_apellido_tarjetaTipo(self):
		form_data = {'apellido': 'Roma',
					 'tarjetaTipo' : 'Mister'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_apellido_tarjeta(self):
		form_data = {'apellido': 'Roma',
					 'tarjeta' : 1234567890654312
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_apellido_ID(self):
		form_data = {'apellido': 'Roma',
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_apellido_PIN(self):
		form_data = {'apellido': 'Roma',
					 'pin' : 'a2341'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_apellido_monto(self):
		form_data = {'apellido': 'Roma',
					 'monto' : 12.08
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_CI_tarjetaTipo(self):
		form_data = {'cedula': 'V-23638870',
					 'tarjetaTipo' : 'Xpress'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_CI_tarjeta(self):
		form_data = {'cedula': 'V-23638870',
					 'tarjeta' : 1987654321123456
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_CI_ID(self):
		form_data = {'cedula': 'V-23638870',
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_CI_PIN(self):
		form_data = {'cedula': 'V-23638870',
					 'pin' : 'p098'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_CI_monto(self):
		form_data = {'cedula': 'V-23638870',
					 'monto' : 98.9
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjetaTipo_tarjeta(self):
		form_data = {'tarjetaTipo' : 'Xpress',
					 'tarjeta' : 1234567890124356
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjetaTipo_ID(self):
		form_data = {'tarjetaTipo' : 'Xpress',
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjetaTipo_PIN(self):
		form_data = {'tarjetaTipo' : 'Xpress',
					 'pin' : 'jumn'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjetaTipo_monto(self):
		form_data = {'tarjetaTipo' : 'Xpress',
					 'monto' : 5
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjeta_ID(self):
		form_data = {'tarjeta' : 1234567890124356,
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjeta_PIN(self):
		form_data = {'tarjeta' : 1234567890124356,
					 'pin' : 'hj87'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_DosCampos_tarjeta_monto(self):
		form_data = {'tarjeta' : 1234567890124356,
					 'monto' : 1.9
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_TresCampos_nombre_apellido_ci(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-24222692'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_TresCampos_nombre_apellido_tarjetaTipo(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'tarjetaTipo' : 'Vista'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_TresCampos_nombre_apellido_tarjeta(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'tarjeta' : 1234567890012345
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_TresCampos_nombre_apellido_ID(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_TresCampos_nombre_apellido_PIN(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'tarjeta' : 'dfgh'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_TresCampos_nombre_apellido_monto(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'monto' : 12.09
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CuatroCampos_nombre_apellido_cedula_tarjetaTipo(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CuatroCampos_nombre_apellido_cedula_tarjeta(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjeta' : 1234567890123456
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CuatroCampos_nombre_apellido_cedula_ID(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CuatroCampos_nombre_apellido_cedula_PIN(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'uj89'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CuatroCampos_nombre_apellido_cedula_monto(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'monto' : 567.9
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CincoCampos_nombre_apellido_cedula_tarjetaTipo_tarjeta(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'tarjeta' : 1234567891234567
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CincoCampos_nombre_apellido_cedula_tarjetaTipo_ID(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'billetera_id' : 12
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CincoCampos_nombre_apellido_cedula_tarjetaTipo_PIN(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'pin' : 'er13'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_CincoCampos_nombre_apellido_cedula_tarjetaTipo_monto(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'monto' : 123
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_SeisCampos_nombre_apellido_cedula_tarjetaTipo_tarjeta_ID(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'tarjeta' : 1234567891234567,
					 'billetera_id' : 1
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_SeisCampos_nombre_apellido_cedula_tarjetaTipo_tarjeta_PIN(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'tarjeta' : 1234567891234567,
					 'pin' : '45gt'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_SeisCampos_nombre_apellido_cedula_tarjetaTipo_tarjeta_monto(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'tarjeta' : 1234567891234567,
					 'monto' : 100.9
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_SieteCampos_nombre_apellido_cedula_tarjetaTipo_tarjeta_ID_PIN(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'tarjeta' : 1234567891234567,
					 'billetera_id' : 1,
					 'pin' : '09ol'
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#caso borde
	def test_RecargarSaldo_SieteCampos_nombre_apellido_cedula_tarjetaTipo_tarjeta_ID_monto(self):
		form_data = {'nombre': 'Nelson',
					 'apellido' : 'Saturno',
					 'cedula' : 'V-23638870',
					 'tarjetaTipo' : 'Mister',
					 'tarjeta' : 1234567891234567,
					 'billetera_id' : 1,
					 'monto' : 45
					}
		form = RecargaForm(data = form_data)
		self.assertFalse(form.is_valid())

	#TDD
	def test_RecargarSaldo_CamposBien(self):
		form_data = {'nombre' : 'Marisela',
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
		form_data = {'nombre' : 'Marisela',
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
		
