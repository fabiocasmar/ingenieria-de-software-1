# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time, date

from estacionamientos.forms import SaldoForm

###################################################################
# ESTACIONAMIENTO_RESERVA_FORM
###################################################################

class SaldoFormTestCase(TestCase):

    # malicia
    def test_Saldo_vacio(self):
        form_data = {}
        form = SaldoForm(data = form_data)
        self.assertFalse(form.is_valid())

	# caso borde
    def test_ConsultarSaldo_UnCampo_ID(self):
        form_data = {'billetera_id': 10}
        form = SaldoForm(data = form_data)
        self.assertFalse(form.is_valid())

	# caso borde
    def test_ConsultarSaldo_UnCampo_Pin(self):
        form_data = {'pin': '2345p'}
        form = SaldoForm(data = form_data)
        self.assertFalse(form.is_valid())

	# caso malicia
    def test_ConsultarSaldo_ID_Invalido(self):
        form_data = {'billetera_id': 'susa',
        			 'pin' : 1234
        			}
        form = SaldoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # TDD
    def test_ConsultarSaldo_CamposBien(self):
        form_data = {'billetera_id': 1,
                     'pin' : 2345
          			}
        form = SaldoForm(data = form_data)
        self.assertTrue(form.is_valid())