# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.controller import recargar_saldo
from estacionamientos.models import (
                                        Billetera,
                                        Usuario
                                    )

###################################################################
#             BILLETERA RECARGAR SALDO VISTA DISPONIBLE
###################################################################

class recargarSaldoTestCase(TestCase):

	def crear_usuario(self):
		usua = Usuario(
			nombre = "nom",
			apellido = "apel",
			cedula = "24256878",
			)
		usua.save()
		return usua

	# TDD
	def test_primera_recarga(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = recargar_saldo(b.id,'1234',0)
		billetera = Billetera.objects.get(id=b.id)
		saldo = float(billetera.saldo)
		self.assertEqual(saldo, float(resp))

	# Malicia
	def test_PinRecarga_distinto(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = recargar_saldo(b.id,'1234jk',3)
		self.assertFalse(resp)

	# TDD
	def test_Una_Recarga(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = recargar_saldo(b.id,'1234',3)
		billetera = Billetera.objects.get(id=b.id)
		saldo = float(billetera.saldo)
		self.assertEqual(saldo, float(resp))

	# TDD
	def test_Recarga_Decimal(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = recargar_saldo(b.id,'1234',9.0)
		billetera = Billetera.objects.get(id=b.id)
		saldo = float(billetera.saldo)
		self.assertEqual(saldo, float(resp))

	# borde
	def test_Muchas_Recargas(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		resp = recargar_saldo(b.id,'1234',3)
		resp2 = recargar_saldo(b.id,'1234',4)
		resp3 = recargar_saldo(b.id,'1234',5.85)
		resp4 = recargar_saldo(b.id,'1234',3.00)
		billetera = Billetera.objects.get(id=b.id)
		saldo = float(billetera.saldo)
		self.assertEqual(saldo, float(15.85))

	# Malicia
	def test_ID_inexistente(self):
		b = Billetera(
			usuario = self.crear_usuario(),
			saldo = 0.00,
			pin = '1234'
		)
		b.save()
		recarga = recargar_saldo(6,'1234',78)
		self.assertFalse(recarga)

