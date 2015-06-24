# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import (
    datetime,
    time,
    timedelta
)

from estacionamientos.controller import validarHorarioReserva


##############################################################
# Estacionamiento Reserva Controlador
###################################################################

class ReservaFormControllerTestCase(TestCase):
# HorarioReserva, pruebas Unitarias
    # normal
    def test_HorarioReservaValido(self):
        hoy=datetime.now()
        ReservaInicio = datetime(hoy.year,hoy.month,hoy.day,15) + timedelta(days=1)
        ReservaFin = datetime(hoy.year,hoy.month,hoy.day,17) + timedelta(days=1)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (True, ''))

    # borde
    def test_UnDiaDeReserva_Estacionamiento_No_24_horas(self):
        hoy=datetime.now()
        HoraApertura=time(6,0)
        HoraCierre=time(18,0)
        ReservaInicio=datetime(hoy.year,hoy.month,hoy.day,15) + timedelta(days=1)
        ReservaFin=datetime(hoy.year,hoy.month,hoy.day,15) + timedelta(days=2)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (False, 'No puede haber reservas entre dos dias distintos'))
    #Borde
    def test_reservaHorarioCompleto(self):
        hoy=datetime.now()
        HoraApertura=time(6,0)
        HoraCierre=time(18,0)
        ReservaInicio=datetime(hoy.year,hoy.month,hoy.day,6) + timedelta(days=1)
        ReservaFin=datetime(hoy.year,hoy.month,hoy.day,18) + timedelta(days=1)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (True,''))

    def test_reservaHorarioCompletoYUnMinuto(self):
        hoy=datetime.now()
        HoraApertura=time(6,0)
        HoraCierre=time(18,0)
        ReservaInicio=datetime(hoy.year,hoy.month,hoy.day,6) + timedelta(days=1)
        ReservaFin=datetime(hoy.year,hoy.month,hoy.day,18,1) + timedelta(days=2)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (False, 'El horario de fin de la reserva debe estar en un horario válido.'))


    #Normal
    def test_UnDiaDeReserva_Estacionamiento_24_horas(self):
        hoy=datetime.now()
        HoraApertura=time(0,0)
        HoraCierre=time(23,59)
        ReservaInicio=datetime(hoy.year,hoy.month,hoy.day,15) + timedelta(days=1)
        ReservaFin=datetime(hoy.year,hoy.month,hoy.day,15) + timedelta(days=2)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (True, ''))

    #Esquina
    def test_SieteDiasDeReserva(self):
        hoy=datetime.now().replace(hour = 0, minute = 0)
        HoraApertura=time(0,0)
        HoraCierre=time(23,59)
        ReservaInicio=hoy
        ReservaFin=hoy + timedelta(7) - timedelta(minutes=1)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (True, ''))

    def test_DiasDeReservaYUnMinuto(self):
        hoy=datetime.now().replace(hour = 0, minute = 0)
        HoraApertura=time(0,0)
        HoraCierre=time(23,59)
        ReservaInicio=hoy
        ReservaFin=hoy + timedelta(days=15,minutes=1)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        a = str(horizonteDias)
        b = str(horizonteHoras)
        self.assertEqual(x, (False, 'La reserva debe estar dentro de los proximos' +a+' dias y'+b+' horas'))

    # caso borde
    def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
        ReservaInicio = datetime.now()+timedelta(minutes=1)
        ReservaFin = datetime.now()
        HoraApertura = time(hour = 0, minute = 0, second = 0)
        HoraCierre = time(hour = 23, minute = 59, second = 59)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (False, 'El horario de inicio de reservacion debe ser menor al horario de fin de la reserva.'))

    # caso borde
    def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 13, minute = 0, second = 0)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 13, minute = 59, second = 59)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora.'))

    # caso borde.
    def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
        HoraApertura = time(hour = 10, minute = 0, second = 0)
        HoraCierre = time(hour = 22, minute = 0, second = 0)
        hoy=datetime.today()
        ReservaInicio=datetime(hoy.year,hoy.month,hoy.day,17) + timedelta(days=1)
        ReservaFin=datetime(hoy.year,hoy.month,hoy.day,23) + timedelta(days=1)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (False, 'El horario de fin de la reserva debe estar en un horario válido.'))

    # Caso borde
    def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
        hoy=datetime.now()
        ReservaInicio = datetime(hoy.year,hoy.month,hoy.day,7) + timedelta(days=1)
        ReservaFin = datetime(hoy.year,hoy.month,hoy.day,15) + timedelta(days=1)
        HoraApertura=time(8,0)
        HoraCierre=time(18,0)
        horizonteDias = 15
        horizonteHoras = 0
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horizonteDias, horizonteHoras)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe estar en un horario válido.'))


