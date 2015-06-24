# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time,datetime
from estacionamientos.controller import crear_cancelacion, cancelacion
from estacionamientos.models import (
                                        Pago,
                                        Reserva,
                                        Estacionamiento,
                                        Usuario,
                                        Billetera,
                                        Propietario
                                    )

class cancelacionTestCase(TestCase):

	def crear_Propietario(self):
		propietario = Propietario(
			nombre = "Nom",
			apellido = "Apell",
			cedula = 'V-242768',
			 )
		propietario.save()
		return propietario

	def crear_Estacionamiento(self):
		estacionamiento = Estacionamiento(
			propietario = self.crear_Propietario(),
			nombre = "nom_Est",
			direccion = "dir",
			rif = "J-987654321",
			 )
		estacionamiento.save()
		return estacionamiento

	def crear_Reserva(self):
		hoy = datetime.now()
		reserva = Reserva(
			nombre = 'nomRes',
			apellido = 'apelRes',
			cedula = 'V-289074',
			estacionamiento = self.crear_Estacionamiento(),
			inicioReserva = datetime(2015,7,12,13,40),
			finalReserva = datetime(2015,7,12,18,40),
			tipo_puesto = 'Particular'
			)
		reserva.save()
		return reserva

	def crear_Pago(self):
		pago = Pago(
			fechaTransaccion = datetime.now(),
			cedula = "V-2345678",
			tarjetaTipo = 'Vista',
			reserva = self.crear_Reserva(),
			monto = 10.08,
			 )
		pago.save()
		return pago

	def crear_usuario(self):
		usuario = Usuario(
			nombre = "nom",
			apellido = "apell",
			cedula = "V-2345678",
			)
		usuario.save()
		return usuario

	def crear_billetera(self):
		billetera = Billetera(
			usuario = self.crear_usuario(),
			saldo = 1000.00,
			pin = '1234ab',
		)
		billetera.save()
		return billetera

	#TDD
	def test_billeteraExistente(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		Reserva_cancelada = cancelacion(p.cedula, b.pin, b.id, p.id)
		self.assertTrue(Reserva_cancelada[0])

	#malicia
	def test_billeteraNOExistente(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		Reserva_cancelada = cancelacion(p.cedula, b.pin, 67, p.id)
		self.assertFalse(Reserva_cancelada[0])

	#TDD
	def test_pagoExistente(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		Reserva_cancelada = cancelacion(p.cedula, b.pin, b.id, p.id)
		self.assertTrue(Reserva_cancelada[0])

	#malicia
	def test_pagoNOExistente(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		Reserva_cancelada = cancelacion(p.cedula, b.pin, b.id, 0)
		self.assertFalse(Reserva_cancelada[0])

	#TDD
	def test_pinValido(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		pin = '1234ab'
		Reserva_cancelada = cancelacion(p.cedula, pin, b.id, p.id)
		self.assertEqual(b.pin, pin)

	#malicia
	def test_pinInvalido(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		pin = '1234f'
		Reserva_cancelada = cancelacion(p.cedula, pin, b.id, p.id)
		self.assertNotEqual(b.pin, pin)

	#TDD
	def test_pagoIDValido(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		pago_id = p.id
		Reserva_cancelada = cancelacion(p.cedula, b.pin, b.id, pago_id)
		self.assertEqual(p.id, pago_id)

	#malicia
	def test_pagoIDInvalido(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		pago_id = 0
		Reserva_cancelada = cancelacion(p.cedula, b.pin, b.id, pago_id)
		self.assertNotEqual(p.id, pago_id)

	#TDD
	def test_CancelacionPosible(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		Reserva_cancelada = cancelacion(p.cedula, b.pin, b.id, p.id)
		self.assertTrue(Reserva_cancelada[0])

	#TDD
	def test_SeHaceLaCancelacion(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		self.assertTrue(crear_cancelacion(b.id, p.id))

	#malicia
	def test_NOSeHaceLaCancelacion_porBilletera(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		cancelacion = crear_cancelacion(87, p.id)
		self.assertFalse(cancelacion[0])

	#malicia
	def test_NOSeHaceLaCancelacion_porPago(self):
		b = self.crear_billetera()
		p = self.crear_Pago()
		cancelacion = crear_cancelacion(b.id, 87)
		self.assertFalse(cancelacion[0])

