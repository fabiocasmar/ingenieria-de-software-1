# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time, date

from estacionamientos.forms import SageForm

###################################################################
# ESTACIONAMIENTO_SAGE_FORM
###################################################################

class SageFormTestCase(TestCase):

    # malicia
    def test_form_vacio(self):
        form_data = {}
        form = SageForm(data = form_data)
        self.assertFalse(form.is_valid())

	# malicia
    def test_deduccion_char(self):
        form_data = {'porcentaje': 'hola'}
        form = SageForm(data = form_data)
        self.assertFalse(form.is_valid())

    # TDD
    def test_deduccion_correcta(self):
        form_data = {'porcentaje': 0.00}
        form = SageForm(data = form_data)
        self.assertTrue(form.is_valid())    