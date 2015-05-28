# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import PropietarioForm

###################################################################
#                    Propietario FORM
###################################################################

class PropietarioAllFormTestCase(TestCase):

	# malicia
    def test_PropietarioForm_CamposVacios(self):
        form_data = {}
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_PropietarioForm_UnCampoNecesario(self):
        form_data = {
            'cedula': '12345678',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PropietarioForm_DosCamposNecesarios(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PropietarioForm_TresCamposNecesarios(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #malicia
    def test_PropietarioForm_agregar_telefono(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '04141231234',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PropietarioForm_CuatroCampos(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '04141231234',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #malicia
    def test_PropietarioForm_agregar_email(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PropietarioForm_TodosLosCampos(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #malicia
    def test_PropietarioForm_cedula_invalida(self):
        form_data = {
            'cedula': 'abc123',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PropietarioForm_nombre_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': ' Pedro123',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PropietarioForm_nombre_letras_especiales(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Óscar Añe Müller',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())


    #borde
    def test_PropietarioForm_apellido_letras_especiales(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Oscar',
            'apellido': 'Pérez Éveret Ürlaub',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PropietarioForm_nombre_acento(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Óscar',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #malicia
    def test_PropietarioForm_nombre_simbolo_especial(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro!',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PropietarioForm_apellido_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': '123Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PropietarioForm_apellido_simbolo_especial(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez!',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PropietarioForm_nombre_espacio_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro ',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PropietarioForm_apellido_espacio_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez ',
            'telefono': '04141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PropietarioForm_telefono_tam_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '0414123123',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PropietarioForm_telefono_formato_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '02141231234',
            'email': 'pedroperez@sage.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PropietarioForm_Correo_Electronico_invalido(self):
        form_data = {
            'cedula': '12345678',
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'telefono': '04141231234',
            'email': 'pedroperez@sa@ge.com',
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())