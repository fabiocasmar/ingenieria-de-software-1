# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import (
    datetime,
    time,
    timedelta,
)

from estacionamientos.controller import marzullo

from estacionamientos.models import (
    Estacionamiento,
    Propietario,
    Reserva,
    Puestos
)

###############################################################################
# Marzullo
###############################################################################

class MarzulloTestCase(TestCase):
    '''
        Bordes:   7
        Esquinas: 6
        Malicia:  5

        Es importante definir el dominio de los datos que recibe Marzullo:

          cap. del est. +----------------------+
                        |                      |
                        |                      |
                        |                      |
                /\      |                      |
        cant. vehiculos |                      |
                \/      |                      |
                        |                      |
                        |                      |
                        |                      |
                      0 +----------------------+
                        |       <reserva>      |
                        |                      hora de cierre
                        |
                        hora de apertura

        Para los casos de prueba, manejamos un estacionamiento con apertura
        a las 6am y cierre a las 6pm, con capacidades que var�an en cada caso.
        De esta forma, el dominio se vuelve:

          cap. del est. +--+--+--+--+--+--+--+--+--+--+--+--+
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                /\      |  |  |  |  |  |  |  |  |  |  |  |  |
        cant. vehiculos |  |  |  |  |  |  |  |  |  |  |  |  |
                \/      |  |  |  |  |  |  |  |  |  |  |  |  |
                        |  |  |  |  |zz|zz|zz|zz|zz|zz|  |  |
                        |  |  |  |yy|yy|yy|yy|  |  |  |  |  |
                        |xx|xx|xx|xx|xx|  |  |  |  |  |  |  |
                      0 +--+--+--+--+--+--+--+--+--+--+--+--+
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                        06 07 08 09 10 11 12 13 14 15 16 17 18

        Donde las series de xs, ys y zs representan tres reservaciones,
        X, Y y Z, que van, respectivamente, de 6am a 11am, de 9am a 1pm, y de
        10am a 4pm. Podemos ver que la reservaci�n X constituye un caso borde
        para Marzullo, puesto que su inicio coincide exactamente con la hora en
        la que abre el estacionamiento. Si decimos adem�s que la capacidad
        del estacionamiento es 3, este caso se convierte en una esquina, puesto
        que el borde count=capacidad se alcanza entre las horas 10am y 11am.
    '''
    def crear_propietario(self):
        prop = Propietario(
            nombre = "nom",
            apellido = "apell",
            cedula = "041414141111",
            telefono = "041414141112",
            email = "hola@gmail.com",
            )
        prop.save()
        return prop

    def crear_estacionamiento(self, puestos,hora_apertura=time(0,0),hora_cierre=time(23,59)):
        
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            telefono1 = "041414141111",
            telefono2 = "041414141112",
            telefono3 = "04141414111",
            email1 = "hola@gmail.com",
            email2 = "hola@gmail.com",
            rif = "rif",
            capacidad = puestos,
            apertura       = hora_apertura,
            cierre         = hora_cierre,
        )
        e.save()
        return e

    def testOneReservationMax(self): #borde, ocupaci�n = capacidad
        n = 1
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testOneReservationEarly(self): #borde, inicio = aprtura
        n = 2
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,6), datetime(2015,1,20,10)))

    def testOneReservationLate(self): #borde, fin = cierre
        n = 2
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,15), datetime(2015,1,20,18)))

    def testOneReservationFullDay(self): #esquina, inicio = aprtura y fin = cierre
        n = 1
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,6), datetime(2015,1,20,18)))

    def testSmallestReservation(self): #borde, fin - inicio = 1hora
        n = 1
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,8), datetime(2015,1,20,9)))

    def testAllSmallestReservations(self): #malicia, fin - inicio = 1hora, doce veces
        n = 1
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        for i in range(12):
            Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 6+i), finalReserva = datetime(2015, 1, 20, 7+i), tipo_puesto = 'Particular').save()
        for i in range(12):
            self.assertFalse(marzullo(e.id, 'Particular',datetime(2015,1,20,6+i), datetime(2015,1,20,7+i)))

    def testFullPlusOne(self): #malicia, fin - inicio = 1hora, doce veces + una reserva FullDay
        n = 1
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        for i in range(12):
            Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 6+i), finalReserva = datetime(2015, 1, 20, 7+i), tipo_puesto = 'Particular').save()
        self.assertFalse(marzullo(e.id, 'Particular',datetime(2015, 1, 20, 6), datetime(2015, 1, 20, 18)))

    def testNoSpotParking(self): #borde, capacidad = 0
        n = 0
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertFalse(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testTenSpotsOneReservation(self): #malicia
        n = 10
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testAddTwoReservation(self): #esquina, dos reservaciones con fin = cierre estac.
        n = 10
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 9), finalReserva = datetime(2015, 1, 20, 18), tipo_puesto = 'Particular').save()
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,12), datetime(2015,1,20,18)))

    def testAddTwoReservation2(self): #esquina, dos reservaciones con incio = apertura estac.
        n = 10
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,6), datetime(2015,1,20,14)))

    def testAddThreeReservations(self): #malicia, reserva cubre todo el horario, y ocupaci�n = capacidad
        n = 3
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,6), datetime(2015,1,20,18)))

    def testFiveSpotsFiveReservation(self): #borde, ocupaci�n = capacidad
        n = 5
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,10), datetime(2015,1,20,18)))

    def testFiveSpotsSixReservation(self): #borde, ocupacion = capacidad antes de intentar hacer reservas nuevas
        n = 5
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        self.assertFalse(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,18)))
        self.assertFalse(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testFiveSpotsSixReservationNoOverlapping(self): #Dos esquinas, 1. count = capacidad, inicio=apertura
                                                        #              2. count = capacidad, fin=cierre
        n = 5
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17), tipo_puesto = 'Particular').save()
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,6), datetime(2015,1,20,10)))
        #La reserva de arriba NO se concreta, puesto que s�lo se verific� si era v�lida, sin agregar su objeto
        self.assertFalse(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,18)))
        #De todos modos, la segunda falla, porque count = capacidad+1 a partir de las 12m

    def testManyReservationsMaxOverlapping(self): #esquina, count = capacidad en una hora (10am - 11am), algunas reservas tienen inicio = apertura
        n = 10
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  7), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  8), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  7), finalReserva=datetime(2015, 1, 20, 11), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  8), finalReserva=datetime(2015, 1, 20, 12), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 13), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20,  9), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15), tipo_puesto = 'Particular').save()
        self.assertTrue(marzullo(e.id, 'Particular',datetime(2015,1,20,10), datetime(2015,1,20,15)))

    def testManyReservationsOneOverlap(self): #malicia, count = (capacidad+1) en la hora (9am - 10am), algunas reservas tienen inicio = apertura
        n = 10
        p = Puestos(particular = n,
                    moto = n,
                    carga = n,
                    discapacitado = n)
        p.save()
        e = self.crear_estacionamiento(p)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 7), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 8), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 9), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 7), finalReserva=datetime(2015, 1, 20, 11), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 8), finalReserva=datetime(2015, 1, 20, 12), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 9), finalReserva=datetime(2015, 1, 20, 13), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20,  9), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10), tipo_puesto = 'Particular').save()
        self.assertFalse(marzullo(e.id, 'Particular',datetime(2015,1,20,9), datetime(2015,1,20,10)))
