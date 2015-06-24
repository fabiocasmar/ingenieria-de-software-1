# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time,date

from estacionamientos.forms import ReservaCIForm, CambiarReservaForm

###################################################################
#             ESTACIONAMIENTO_MOVER_RESERVA_FORM
###################################################################

class MoverReservaFormTestCase(TestCase):
	# malicia
	def test_MoverReserva_vacia(self):
		form_data = {}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_UnCampo_ID(self):
		form_data = {'reserva_id' : 1}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_UnCampo_CI(self):
		form_data = {'cedula': 'V-34567890'}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# TDD
	def test_MoverReserva_TodosBien(self):
		form_data = {'reserva_id' : 1
					,'cedula' : 'V-34567890'
					}
		form = ReservaCIForm(data = form_data)
		self.assertTrue(form.is_valid())

	# malicia
	def test_MoverReserva_TodosMal(self):
		form_data = {'reserva_id' : 'susa'
					,'cedula' : 234567
					}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_Todosllenos_UnCampoMal_ID(self):
		form_data = {'reserva_id' : 'susa'
					,'cedula' : 'V-234567'
					}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_Todosllenos_UnCampoMal_CI(self):
		form_data = {'reserva_id' : 1
					,'cedula' : 12345678
					}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_Todosllenos_ID_invalido(self):
		form_data = {'reserva_id' : 0
					,'cedula' : 'V-12345678'
					}
		form = ReservaCIForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_TodosCamposVacios(self):
		form_data = {}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# TDD
	def test_MoverReserva_TodosCamposllenosBien(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertTrue(form.is_valid())

	# malicia
	def test_MoverReserva_UnCampo_inicio1(self):
		form_data = {'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}	
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_UnCampo_inicio0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_1': time(hour = 18, minute = 0),
 					 'final_0': date(year=2015,month=2,day=27)
        			}	
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_UnCampo_final1(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_UnCampo_final0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_1': time(hour = 18, minute = 0),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# esquina
	def test_MoverReserva_DosCampos_finales(self):
		form_data = {'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# esquina
	def test_MoverReserva_DosCampos_inicios(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# esquina
	def test_MoverReserva_Doscampos_inicioFinal0(self):
		form_data = {'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# esquina
	def test_MoverReserva_DosCampos_inicioFinal1(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_1': time(hour = 18, minute = 0)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# esquina
	def test_MoverReserva_DosCampos_inicio0Final1(self):
		form_data = {'final_1': time(hour = 18, minute = 0),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# esquina
	def test_MoverReserva_DosCampos_final0Inicio1(self):
		form_data = {'inicio_1': date(year=2015,month=2,day=27),
					 'final_0': time(hour = 18, minute = 0)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_TresCampos_inicio1Final1Final0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_TresCampos_inicio1Final1Inicio0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_1': time(hour = 18, minute = 0),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_TresCampos_final1Final0Inicio0(self):
		form_data = {'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_TresCampos_inicio1Final0Inicio0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_TodosCamposllenosMal(self):
		form_data = {'inicio_1': 'susa',
					 'final_1': 'time(hour = 18, minute = 70)',
					 'final_0': 'manania',
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# borde
	def test_MoverReserva_UnCampollenoMal_inicio1(self):
		form_data = {'inicio_1': 'susa',
					 'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# borde
	def test_MoverReserva_UnCampollenoMal_final1(self):
		form_data = {'inicio_1': time(hour = 15, minute = 30),
					 'final_1': 'susa',
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# borde
	def test_MoverReserva_UnCampollenoMal_final0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 30),
					 'final_1': time(hour = 18, minute = 0),
					 'final_0': 'manania',
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# borde
	def test_MoverReserva_UnCampollenoMal_inicio0(self):
		form_data = {'inicio_1': time(hour = 15, minute = 30),
					 'final_1': time(hour = 18, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_DosCamposllenosMal_inicio1Final1(self):
		form_data = {'inicio_1': 'susa',
					 'final_1': 'hola',
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_DosCamposllenosMal_inicio1Final0(self):
		form_data = {'inicio_1': 'susa',
					 'final_1': time(hour = 12, minute = 0),
					 'final_0': 'hola',
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_DosCamposllenosMal_inicio1inicio0(self):
		form_data = {'inicio_1': 'susa',
					 'final_1': time(hour = 12, minute = 0),
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_DosCamposllenosMal_final1Final0(self):
		form_data = {'inicio_1': time(hour = 12, minute = 30),
					 'final_1': 'hola',
					 'final_0': 'manania',
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_DosCamposllenosMal_final1Inicio0(self):
		form_data = {'inicio_1': time(hour = 12, minute = 30),
					 'final_1': 'hola',
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_DosCamposllenosMal_final0Inicio0(self):
		form_data = {'inicio_1': time(hour = 12, minute = 30),
					 'final_1': time(hour = 12, minute = 32),
					 'final_0': 'manania',
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_tresCamposllenosMal_inicio1Final1Final0(self):
		form_data = {'inicio_1': date(year=2015,month=2,day=27),
					 'final_1': 'hola',
					 'final_0': 'manania',
					 'inicio_0': date(year=2015,month=2,day=27)
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_tresCamposllenosMal_inicio1Final1Inicio0(self):
		form_data = {'inicio_1': date(year=2015,month=2,day=27),
					 'final_1': 'hola',
					 'final_0': date(year=2015,month=2,day=27),
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_tresCamposllenosMal_final1Final0Inicio0(self):
		form_data = {'inicio_1': time(hour = 22, minute = 23),
					 'final_1': 'hola',
					 'final_0': 'manania',
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())

	# malicia
	def test_MoverReserva_tresCamposllenosMal_inicio1Final0Inicio0(self):
		form_data = {'inicio_1': 'susa',
					 'final_1': time(hour = 23, minute = 56),
					 'final_0': 'manania',
					 'inicio_0': 'hoy'
					}
		form = CambiarReservaForm(data = form_data)
		self.assertFalse(form.is_valid())








