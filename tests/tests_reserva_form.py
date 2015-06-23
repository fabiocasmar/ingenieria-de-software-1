# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time, date

from estacionamientos.forms import ReservaForm

###################################################################
# ESTACIONAMIENTO_RESERVA_FORM
###################################################################

class ReservaFormTestCase(TestCase):
    
    # malicia
    def test_estacionamiento_reserva_vacio(self):
        form_data = {}
        form = ReservaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_EstacionamientoReserva_UnCampo(self):
        form_data = {'inicio_1': time(hour = 6, minute = 0),
                     'final_1': time(hour = 15, minute = 0),
                     'final_0': date(year=2015,month=2,day=27)
        }
        form = ReservaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # TDD
    def test_EstacionamientoReserva_TodosCamposBien(self):
        form_data = {'nombre': 'Marisela',
                     'apellido': 'Del Valle',
                     'cedula': 'V-23638870',
                     'tipo_puesto':'Particular',
                     'inicio_1': time(hour=6, minute=0),
                     'final_1' : time(hour=15, minute=0),
                     'final_0' : date(year=2015, month=2, day=27),
                     'inicio_0': date(year=2015, month=2, day=27)
                    }
        form = ReservaForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_EstacionamientoReserva_InicioString(self):
        form_data = {'inicio_1': 'teruel',
                     'tipo_puesto':'Particular',
                     'final_1': time(hour = 15, minute = 0),
                     'final_0': date(year=2015,month=2,day=27),
                     'inicio_0': date(year=2015,month=2,day=27)
        }
        form = ReservaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_EstacionamientoReserva_FinString(self):
        form_data = {'inicio_1': time(hour = 6, minute = 0),
                     'final_1': 'Reinoza',
                     'tipo_puesto':'Particular',
                     'final_0': date(year=2015,month=2,day=27),
                     'inicio_0': date(year=2015,month=2,day=27)
        }
        form = ReservaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_EstacionamientoReserva_InicioNone(self):
        form_data = {'inicio_1': None,
                     'final_1': time(hour = 15, minute = 0),
                     'final_0': date(year=2015,month=2,day=27),
                     'inicio_0': date(year=2015,month=2,day=27),
                     'tipo_puesto':'Particular'
        }
        form = ReservaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_EstacionamientoReserva_finalNone(self):
        form_data = {'inicio_1': time(hour = 6, minute = 0),
                     'final_1': time(hour = 15, minute = 0),
                     'final_0': None,
                     'inicio_0': date(year=2015,month=2,day=27),
                     'tipo_puesto':'Particular'
        }
        form = ReservaForm(data = form_data)
        self.assertFalse(form.is_valid())