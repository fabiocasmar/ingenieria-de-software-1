# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import datetime

from estacionamientos.controller import marzullo

from estacionamientos.models import (
    Estacionamiento,
    Reserva
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
    def crear_estacionamiento(self, puestos):
        e = Estacionamiento(
            propietario = "prop",
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = puestos,
            apertura       = "06:00",
            cierre         = "18:00",
        )
        e.save()
        return e

    def testOneReservationMax(self): #borde, ocupaci�n = capacidad
        e = self.crear_estacionamiento(1)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testOneReservationEarly(self): #borde, inicio = aprtura
        e = self.crear_estacionamiento(2)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,10)))

    def testOneReservationLate(self): #borde, fin = cierre
        e = self.crear_estacionamiento(2)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,15), datetime(2015,1,20,18)))

    def testOneReservationFullDay(self): #esquina, inicio = aprtura y fin = cierre
        e = self.crear_estacionamiento(1)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,18)))

    def testSmallestReservation(self): #borde, fin - inicio = 1hora
        e = self.crear_estacionamiento(1)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,8), datetime(2015,1,20,9)))

    def testAllSmallestReservations(self): #malicia, fin - inicio = 1hora, doce veces
        e = self.crear_estacionamiento(1)
        for i in range(12):
            Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 6+i), finalReserva = datetime(2015, 1, 20, 7+i)).save()
        for i in range(12):
            self.assertFalse(marzullo(e.id, datetime(2015,1,20,6+i), datetime(2015,1,20,7+i)))

    def testFullPlusOne(self): #malicia, fin - inicio = 1hora, doce veces + una reserva FullDay
        e = self.crear_estacionamiento(1)
        for i in range(12):
            Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 6+i), finalReserva = datetime(2015, 1, 20, 7+i)).save()
        self.assertFalse(marzullo(e.id, datetime(2015, 1, 20, 6), datetime(2015, 1, 20, 18)))

    def testNoSpotParking(self): #borde, capacidad = 0
        e = self.crear_estacionamiento(0)
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testTenSpotsOneReservation(self): #malicia
        e = self.crear_estacionamiento(10)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testAddTwoReservation(self): #esquina, dos reservaciones con fin = cierre estac.
        e = self.crear_estacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 9), finalReserva = datetime(2015, 1, 20, 18)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,12), datetime(2015,1,20,18)))

    def testAddTwoReservation2(self): #esquina, dos reservaciones con incio = apertura estac.
        e = self.crear_estacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,14)))

    def testAddThreeReservations(self): #malicia, reserva cubre todo el horario, y ocupaci�n = capacidad
        e = self.crear_estacionamiento(3)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,18)))

    def testFiveSpotsFiveReservation(self): #borde, ocupaci�n = capacidad
        e = self.crear_estacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,10), datetime(2015,1,20,18)))

    def testFiveSpotsSixReservation(self): #borde, ocupacion = capacidad antes de intentar hacer reservas nuevas
        e = self.crear_estacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,18)))
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testFiveSpotsSixReservationNoOverlapping(self): #Dos esquinas, 1. count = capacidad, inicio=apertura
                                                        #              2. count = capacidad, fin=cierre
        e = self.crear_estacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,10)))
        #La reserva de arriba NO se concreta, puesto que s�lo se verific� si era v�lida, sin agregar su objeto
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,18)))
        #De todos modos, la segunda falla, porque count = capacidad+1 a partir de las 12m

    def testManyReservationsMaxOverlapping(self): #esquina, count = capacidad en una hora (10am - 11am), algunas reservas tienen inicio = apertura
        e = self.crear_estacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  7), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  8), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  7), finalReserva=datetime(2015, 1, 20, 11)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  8), finalReserva=datetime(2015, 1, 20, 12)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 13)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20,  9)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,10), datetime(2015,1,20,15)))

    def testManyReservationsOneOverlap(self): #malicia, count = (capacidad+1) en la hora (9am - 10am), algunas reservas tienen inicio = apertura
        e = self.crear_estacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 7), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 8), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 9), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 7), finalReserva=datetime(2015, 1, 20, 11)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 8), finalReserva=datetime(2015, 1, 20, 12)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 9), finalReserva=datetime(2015, 1, 20, 13)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20,  9)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,10)))
