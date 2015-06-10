# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time,datetime
from estacionamientos.controller import cancelacion
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
			cedula = 242768,
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
			estacionamiento = self.crear_Estacionamiento(),
			inicioReserva = datetime(hoy.year,hoy.month,hoy.day,15),
			finalReserva = datetime(hoy.year,hoy.month,hoy.day,17),
			HoraApertura = time(hour = 12, minute = 0, second = 0),
			HoraCierre = time(hour = 18, minute = 0, second = 0),
			 )
		reserva.save()
		return reserva

	def crear_Pago(self):
		pago = Pago(
			nombre = "NombreT",
			apellido = "apellidoT",
			cedulaTipo = 'V',
			cedula = 24277100,
			tarjetaTipo = 'Vista',
			tarjeta = 1234567890123456,
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
			pin = '1234ab'
		)
		billetera.save()
		return billetera

