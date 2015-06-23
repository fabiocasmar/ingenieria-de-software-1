# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.controller import cambiar_pin
from estacionamientos.models import (
                                        Billetera,
                                        Usuario
                                    )

###################################################################
#             BILLETERA CAMBIAR PIN
###################################################################

class cambiarPinTestCase(TestCase):
	def crear_usuario(self):
		usua = Usuario(
			nombre = "nom",
			apellido = "apel",
			cedula = "24256878",
			)
		usua.save()
		return usua

	# TDD
	def test_CambioPin(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = cambiar_pin(b.id,'1234')
		self.assertTrue(resp)

	# malicia
	def test_CambioPin_IDInvalido(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = cambiar_pin(12345,'1234')
		self.assertFalse(resp)

	# TDD
	def test_CambioPin_IDCorrecto(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = cambiar_pin(b.id,'1234')
		self.assertTrue(resp)

	# malicia
	def test_CambioPin_PinNoMatch(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = cambiar_pin(b.id,'1235')
		self.assertFalse(resp)

	# TDD
	def test_CambioPin_PinValido(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = cambiar_pin(b.id,'1234')
		self.assertTrue(resp)

	# malicia
	def test_CambioPin_PinInvalido(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = cambiar_pin(b.id,'124')
		self.assertFalse(resp)



