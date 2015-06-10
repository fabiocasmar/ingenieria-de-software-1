# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import PagoForm

###################################################################
# Pago Tarjeta de Credito Form
###################################################################
class PagoTarjetaDeCreditoFormTestCase(TestCase):

    # borde
    def test_PagoTarjetaForm_Vacio(self):
        form_data = {}
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_PagoTarjetaForm_UnCampo(self):
        form_data = {
            'nombre': 'Pedro',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_DosCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_TresCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CuatroCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CincoCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_SeisCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '24277100',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PagoTarjetaForm_NombreInvalidoDigitos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_NombreInvalidoSimbolos(self):
        form_data = {
            'nombre': 'Pedro*',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_PagoTarjetaForm_NombreInvalidoEspacio(self):
        form_data = {
            'nombre': ' Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PagoTarjetaForm_ApellidoInvalidoDigitos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez1',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_ApellidoInvalidoSimbolos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': '¡Perez!',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())
    
       
    #borde
    def test_PagoTarjetaForm_ApellidoInvalidoEspacio(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': ' Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CedulaTipoInvalido(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'J',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CedulaInvalida(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': 'V12345',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_Limite_Superior_Cedula(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '999999999',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertTrue(form.is_valid())
    
    #borde
    def test_Limite_Inferior_Cedula(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '0',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PagoTarjetaForm_TipoTarjetaInvalido(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'American',
            'tarjeta': '1234',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_TarjetaInvalido(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': 'ab12345',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PagoTarjetaForm_DosCamposErroneos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'foo',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PagoTarjetaForm_CuatroCamposErroneos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'foo',
            'cedula': '12345sda6789',
            'tarjetaTipo': 'American',
            'tarjeta': '1234',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PagoTarjetaForm_TodosCamposErroneos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez2',
            'cedulaTipo': 'foo',
            'cedula': '12345678as9',
            'tarjetaTipo': 'American',
            'tarjeta': 'prueba',
        }
        form = PagoForm(data = form_data)
        self.assertFalse(form.is_valid())
