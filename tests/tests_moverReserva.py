# -*- coding: utf-8 -*-

from django.test import TestCase
from datetime import time,datetime

from estacionamientos.controller import chequear_mover_reserva, nuevo_monto_reserva, mover_reserva
from estacionamientos.models import (
                                        Pago,
                                        Reserva,
                                        Estacionamiento,
                                        Usuario,
                                        Billetera,
                                        Propietario,
                                        Reembolso
                                    )

class moverReservaTestCase(TestCase):

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
			cedula = 'V-2345678',
			estacionamiento = self.crear_Estacionamiento(),
			inicioReserva = datetime(2015,7,12,13,40),
			finalReserva = datetime(2015,7,12,18,40),
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

	def crear_Reserva2(self):
		hoy = datetime.now()
		reserva2 = Reserva(
			nombre = 'nomRes2',
			apellido = 'apelRes2',
			cedula = 'V-2345678',
			estacionamiento = self.crear_Estacionamiento(),
			inicioReserva = datetime(2015,7,12,15,40),
			finalReserva = datetime(2015,7,12,23,40),
			)
		reserva2.save()
		return reserva2

	def crear_Pago2(self):
		pago2 = Pago(
			fechaTransaccion = datetime.now(),
			cedula = "V-2345678",
			tarjetaTipo = 'Vista',
			reserva = self.crear_Reserva2(),
			monto = 12.08,
			 )
		pago2.save()
		return pago2

	def crear_Reserva3(self):
		hoy = datetime.now()
		reserva3 = Reserva(
			nombre = 'nomRes3',
			apellido = 'apelRes3',
			cedula = 'V-2345678',
			estacionamiento = self.crear_Estacionamiento(),
			inicioReserva = datetime(2015,7,12,13,40),
			finalReserva = datetime(2015,7,12,15,40),
			)
		reserva3.save()
		return reserva3

	def crear_Pago3(self):
		pago3 = Pago(
			fechaTransaccion = datetime.now(),
			cedula = "V-2345678",
			tarjetaTipo = 'Vista',
			reserva = self.crear_Reserva3(),
			monto = 8.08,
			 )
		pago3.save()
		return pago3


	def crear_Reserva4(self):
		hoy = datetime.now()
		reserva4 = Reserva(
			nombre = 'nomRes4',
			apellido = 'apelRes4',
			cedula = 'V-2345678',
			estacionamiento = self.crear_Estacionamiento(),
			inicioReserva = datetime(2015,7,12,14,40),
			finalReserva = datetime(2015,7,12,19,40),
			)
		reserva4.save()
		return reserva4

	def crear_Pago4(self):
		pago4 = Pago(
			fechaTransaccion = datetime.now(),
			cedula = "V-2345678",
			tarjetaTipo = 'Vista',
			reserva = self.crear_Reserva4(),
			monto = 10.08,
			 )
		pago4.save()
		return pago4


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

	# malicia
	def test_MoverReserva_cedulaInexistente(self):
		p = self.crear_Pago()
		Reserva_movida = chequear_mover_reserva('V-987654', p.id)
		self.assertFalse(Reserva_movida)

	# TDD
	def test_MoverReserva_cedulaExistente(self):
		p = self.crear_Pago()
		Reserva_movida = chequear_mover_reserva(p.cedula, p.id)
		self.assertTrue(Reserva_movida)

	# malicia
	def test_MoverReserva_ReservaIDInexistente(self):
		p = self.crear_Pago()
		Reserva_movida = chequear_mover_reserva(p.cedula, 678)
		self.assertFalse(Reserva_movida)

	# TDD
	def test_MoverReserva_ReservaIDExistente(self):
		p = self.crear_Pago()
		Reserva_movida = chequear_mover_reserva(p.cedula, p.id)
		self.assertTrue(Reserva_movida)

	# TDD
	def test_MoverReserva_MontoNuevoMenorAMontoViejo(self):
		p = self.crear_Pago()
		p3 = self.crear_Pago3()
		MontoReserva = nuevo_monto_reserva(p.monto, p3.monto)
		self.assertTrue(MontoReserva[0])

	# TDD
	def test_MoverReserva_MontoNuevoMayorAMontoViejo(self):
		p = self.crear_Pago()
		p2 = self.crear_Pago2()
		MontoReserva = nuevo_monto_reserva(p.monto, p2.monto)
		self.assertFalse(MontoReserva[0])

	# TDD
	def test_MoverReserva_MontoNuevoIgualAMontoViejo(self):
		p = self.crear_Pago()
		p4 = self.crear_Pago4()
		MontoReserva = nuevo_monto_reserva(p.monto, p4.monto)
		self.assertEqual(MontoReserva[0], -1)

	# TDD
	def test_MoverReserva_CalculoMontoNuevoMenorAMontoViejo(self):
		p = self.crear_Pago()
		p3 = self.crear_Pago3()
		MontoReserva = nuevo_monto_reserva(p.monto, p3.monto)
		self.assertEqual(MontoReserva[1], 2)

	# TDD
	def test_MoverReserva_CalculoMontoNuevoMayorAMontoViejo(self):
		p = self.crear_Pago()
		p2 = self.crear_Pago2()
		MontoReserva = nuevo_monto_reserva(p.monto, p2.monto)
		self.assertEqual(MontoReserva[1], 2)

	# TDD
	def test_MoverReserva_CalculoMontoNuevoIgualAMontoViejo(self):
		p = self.crear_Pago()
		p4 = self.crear_Pago4()
		MontoReserva = nuevo_monto_reserva(p.monto, p4.monto)
		self.assertEqual(MontoReserva[1], 0)