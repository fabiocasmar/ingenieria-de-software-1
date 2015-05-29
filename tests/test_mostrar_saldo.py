# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.controller import mostrar_saldo
from estacionamientos.models import (
                                        Billetera,
                                        Usuario
                                    )

###################################################################
#             BILLETERA MOSTRAR SALDO VISTA DISPONIBLE
###################################################################

class mostrarSaldoTestCase(TestCase):

	def crear_usuario(self):
		usu = Usuario(
			nombre = "nom",
			apellido = "apell",
			cedula = "2345678",
			telefono = "041414141112",
			email = "holakase@gmail.com",
			)
		usu.save()
		return usu

	# TDD
	def test_billetera_nueva(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0,
			pin = 1234
		)
		b.save()
		sePuede = mostrar_saldo (1,'1234')
		self.assertTrue(b.saldo == 0)

	# Malicia
	def test_Pin_distinto(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0,
			pin = 1234
		)
		b.save()
		sePuede = mostrar_saldo (1,'1234jk')
		self.assertFalse(sePuede)

	# TDD
	def test_2billetera_1usuario(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 23,
			pin = 1234
		)
		b.save()
		b2 = Billetera(
			usuario = self.crear_usuario(),
			saldo = 25,
			pin = '1234l'
		)
		b2.save()

		sePuede = mostrar_saldo (1,'1234')
		sePuede2 = mostrar_saldo (2,'1234l')
		self.assertFalse(b.saldo == b2.saldo)

	# TDD
	def test_2billetera_2usuarios_mismoPin(self):
		usu = Usuario(
		nombre = "nombre",
		apellido = "apell",
		cedula = "2345678",
		telefono = "041414141112",
		email = "holakase@gmail.com",
		)

		usu.save()

		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 23,
			pin = 1234
		)

		usua = Usuario(
		nombre = "nom",
		apellido = "apell",
		cedula = "2345678",
		telefono = "041414141112",
		email = "holakase@gmail.com",
		)
        
		usua.save()

		b2 = Billetera(
			usuario = self.crear_usuario(),
			saldo = 25,
			pin = 1234
		)

		b.save()
		b2.save()

		sePuede = mostrar_saldo (1,'1234')
		sePuede2 = mostrar_saldo (2,'1234')
		self.assertFalse(b.saldo == b2.saldo)