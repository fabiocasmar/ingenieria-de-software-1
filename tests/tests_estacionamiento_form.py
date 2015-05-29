# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.models import Propietario

from estacionamientos.forms import EstacionamientoForm

###################################################################
#                    ESTACIONAMIENTO_ALL FORM
###################################################################

class EstacionamientoAllFormTestCase(TestCase):

    # malicia
    def test_campos_vacios(self):
        form_data = {}
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_solo_un_campo_necesario(self):
        form_data = {
            'propietario': '1234567'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_dos_campos_necesarios(self):
        form_data = {
            'propietario': '12345678',
            'nombre': 'Orinoco'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_tres_campos_necesarios(self):
        form_data = {
            'propietario': '1234567',
            'nombre': 'Orinoco',
            'direccion': 'Caracas'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_todos_los_campos_necesarios(self):
        form_data = {
            'propietario': '1234356',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_propietario_invalido_letras_en_campo(self):
        form_data = {
            'propietario': 'Pedro123',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_propietario_invalido_simbolos_especiales(self):
        form_data = {
            'propietario': 'Pedro!',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_RIF_tamano_invalido(self):
        form_data = {
            'propietario': '1234567',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-1234567'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_RIF_formato_invalido(self):
        form_data = {
            'propietario': '1234455',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'Kaa123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_agregar_telefonos(self):
        form_data = {
            'propietario': '1234546',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789',
            'telefono_1': '02129322878',
            'telefono_2': '04149322878',
            'telefono_3': '04129322878'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_formato_invalido_telefono(self):
        form_data = {
            'propietario': '1234567a',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789',
            'telefono_1': '02193228782'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_tamano_invalido_telefono(self):
        form_data = {
            'propietario': '123456a',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789',
            'telefono_1': '021235261667'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_agregar_correos_electronicos(self):
        form_data = {
            'propietario': '123456',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789',
            'telefono_1': '02129322878',
            'telefono_2': '04149322878',
            'telefono_3': '04129322878',
            'email_1': 'adminsitrador@admin.com',
            'email_2': 'usua_rio@users.com'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_correo_electronico_invalido(self):
        form_data = {
            'propietario': '1234567a',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V-123456789',
            'telefono_1': '02129322878',
            'telefono_2': '04149322878',
            'telefono_3': '04129322878',
            'email_1': 'adminsitrador@a@dmin.com'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertFalse(form.is_valid())
