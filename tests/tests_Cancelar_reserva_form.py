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
