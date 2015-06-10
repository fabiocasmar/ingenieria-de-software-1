# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time,datetime
from estacionamientos.controller import consumir_saldo
from estacionamientos.models import (
                                        Usuario,
                                        Billetera
                                    )

###################################################################
#                 ESTACIONAMIENTO VISTA DISPONIBLE                #
###################################################################

class consumirSaldoTestCase(TestCase):

	def crear_usuario(self):
		usuario = Usuario(
			nombre = "nom",
			apellido = "apell",
			cedula = "2345678",
			)
		usuario.save()
		return usuario

	def crear_billetera(self):
		billetera = Billetera(
			usuario = self.crear_usuario(),
			saldo = 1000.00,
			pin = '1234ab'
		)
		billetera.save()
		return billetera

	# TDD
	def test_consumirSaldo_MontoConsumoSinDecimales(self):
		b = self.crear_billetera()
		consumo = consumir_saldo(b.id, '1234ab', 15)
		b_aux = Billetera.objects.get(id = b.id)
		saldo = b_aux.saldo
		self.assertTrue(consumo)
		self.assertEqual(saldo, b.saldo-15)

	# Borde
	def test_consumirSaldo_MontoConsumoIgualASaldo(self):
		b = self.crear_billetera()
		consumo = consumir_saldo(b.id, '1234ab', 1000)
		b_aux = Billetera.objects.get(id = b.id)
		saldo = b_aux.saldo
		self.assertTrue(consumo)

	# TDD
	def test_consumirSaldo_MontoConsumoUnDecimal(self):
		b = self.crear_billetera()
		consumo = consumir_saldo(b.id, '1234ab', 15.30)
		b_aux = Billetera.objects.get(id = b.id)
		saldo = b_aux.saldo
		self.assertTrue(consumo)

	# TDD
	def test_consumirSaldo_MontoConsumoDosDecimales(self):
		b = self.crear_billetera()
		consumo = consumir_saldo(b.id, '1234ab', 65.18)
		b_aux = Billetera.objects.get(id = b.id)
		saldo = b_aux.saldo
		self.assertTrue(consumo)

	# Malicia
	def test_consumirSaldo_MontoConsumoTresDecimales(self):
		b = self.crear_billetera()
		consumo = consumir_saldo(b.id, '1234ab', 9.876)
		b_aux = Billetera.objects.get(id = b.id)
		saldo = b_aux.saldo
		self.assertTrue(consumo)

	# Malicia
	def test_consumirSaldo_MontoConsumoMayorASaldo(self):
		b = self.crear_billetera()
		consumo = consumir_saldo(b.id, '1234ab', 1000.01)
		b_aux = Billetera.objects.get(id = b.id)
		saldo = b_aux.saldo
		self.assertEqual(saldo, float(consumo))

	# Malicia
	def test_consumirSaldo_billeteraInexistente(self):
		consumo = consumir_saldo(0, '1234ab', 15.00)
		self.assertFalse(consumo)

	# Malicia
	def test_consumirSaldo_PinIncorrecto(self):
		consumo = consumir_saldo(0, '2241', 15.00)
		self.assertFalse(consumo)