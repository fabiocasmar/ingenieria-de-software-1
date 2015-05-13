# -*- coding: utf-8 -*-

from django.test import TestCase

from decimal import Decimal
from datetime import (
    datetime,
    time,
    timedelta,
)

from estacionamientos.controller import (
    tasa_reservaciones, 
    calcular_porcentaje_de_tasa
)

from estacionamientos.models import (
    Estacionamiento,
    Reserva
)

###################################################################
# Casos de prueba de la tasa de resevación
###################################################################

class TestTasaEstacionamiento(TestCase):
    
    def crear_estacionamiento(self, puestos,hora_apertura=time(0,0),hora_cierre=time(23,59)):
        e = Estacionamiento(
            propietario = "prop",
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = puestos,
            apertura       = hora_apertura,
            cierre         = hora_cierre,
        )
        e.save()
        return e
    
    # Esquina 
    def test_estacionamiento_sin_reservas(self): # Esquina
        e=self.crear_estacionamiento(1)
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        salida=dict(zip(lista_fechas,lista_valores))
        self.assertEqual(tasa_reservaciones(e.id),salida)
    
    def test_estacionamiento_reserva_una_hora_sin_cambio_fecha(self): # Normal TDD
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[1]=60
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=(ahora+timedelta(1)).replace(hour=15,minute=15)
        fecha_fin=fecha_inicio.replace(hour=16,minute=15)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
        
    def test_estacionamiento_reserva_una_hora_cambio_fecha_mediaNoche(self): # Esquina
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[1]=45
        lista_valores[2]=1
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=(ahora+timedelta(1)).replace(hour=23,minute=15,second=0)
        fecha_fin=fecha_inicio+timedelta(minutes=46)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        x=tasa_reservaciones(e.id)
        self.assertEqual(x,salida)
        
    def test_reserva_inicio_antes_de_inicioVentana_fin_despues_inicioVentana(self): # Esquina
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=1
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora-timedelta(1)
        fecha_fin=ahora.replace(hour=0,minute=1)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
        
    def test_estacionamiento_reserva_un_dia_sola_casilla_menos_un_minuto(self): # Normal TDD
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[1]=60*24-1
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora+timedelta(1)
        fecha_fin=ahora+timedelta(days=1,hours=23,minutes=59)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_estacionamiento_reserva_un_dia_sola_casilla(self): # Borde
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[1]=60*24
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora+timedelta(1)
        fecha_fin=ahora+timedelta(days=2)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_estacionamiento_reserva_un_dia_dos_casillas(self): #Borde
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[1]=780
        lista_valores[2]=660
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora+timedelta(days=1,hours=11)
        fecha_fin=ahora+timedelta(days=2,hours=11)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_estacionamiento_reserva_un_dia_mas_un_minuto(self): #Borde
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[1]=60*24
        lista_valores[2]=1
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora+timedelta(1)
        fecha_fin=ahora+timedelta(days=2,seconds=60)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_estacionamiento_reserva_siete_dias(self): # Esquina
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[60*24 for i in range(7)]
        lista_valores[6]=60*24-1
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora
        fecha_fin=ahora+timedelta(days=6,hours=23,minutes=59,seconds=0)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        self.assertEqual(tasa_reservaciones(e.id,True),salida)
        
    def test_estacionamiento_reserva_siete_dias_antes_media_noche(self): #Esquina
        e=self.crear_estacionamiento(1)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[60*24 for i in range(7)]
        lista_valores[0]=1
        lista_valores[6]=60*24-1
        salida=dict(zip(lista_fechas,lista_valores))
        fecha_inicio=ahora.replace(hour=23,minute=59)
        fecha_fin=ahora.replace(hour=23,minute=59)+timedelta(days=6)
        Reserva(estacionamiento= e,inicioReserva=fecha_inicio,finalReserva=fecha_fin).save()
        x=tasa_reservaciones(e.id)
        self.assertEqual(x,salida)
        
    def test_estacionamiento_reserva_una_hora_dos_puestos(self): # Borde
        e=self.crear_estacionamiento(2)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=90
        salida=dict(zip(lista_fechas,lista_valores))
        Reserva(estacionamiento= e,inicioReserva=ahora,finalReserva=ahora+timedelta(seconds=2700)).save()
        Reserva(estacionamiento= e,inicioReserva=ahora+timedelta(seconds=2700),finalReserva=ahora+timedelta(seconds=5400)).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_dos_reservaciones_mismo_dia(self): # Borde
        e=self.crear_estacionamiento(2)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=1440*2
        salida=dict(zip(lista_fechas,lista_valores))
        Reserva(estacionamiento= e,inicioReserva=ahora,finalReserva=ahora+timedelta(1)).save()
        Reserva(estacionamiento= e,inicioReserva=ahora,finalReserva=ahora+timedelta(1)).save()
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_reserva_6_dias_misma_hora(self): # Normal TDD
        e=self.crear_estacionamiento(2)
        ahora=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[1440 for i in range(7)]
        lista_valores[0]=0
        lista_valores[1]=0
        lista_valores[2]=18*60
        lista_valores[6]=6*60
        salida=dict(zip(lista_fechas,lista_valores))
        Reserva(estacionamiento= e,inicioReserva=ahora.replace(hour=6)+timedelta(2),finalReserva=ahora.replace(hour=6)+timedelta(6)).save()
        x=tasa_reservaciones(e.id)
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_reservaciones_de_una_hora_24_horas(self): # Esquina
        CAPACIDAD = 10
        HORAS_SEMANA = 168
        UNA_HORA = timedelta(hours=1)
        ahora = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        e = self.crear_estacionamiento(CAPACIDAD)
        for i in range(CAPACIDAD):
            hora_reserva = ahora
            for j in range(HORAS_SEMANA):
                if j!=HORAS_SEMANA-1:
                    Reserva(estacionamiento=e,inicioReserva=hora_reserva,finalReserva=hora_reserva+UNA_HORA).save()
                else:
                    Reserva(estacionamiento=e,inicioReserva=hora_reserva,finalReserva=hora_reserva+timedelta(minutes=59)).save()
                hora_reserva += UNA_HORA
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[60*CAPACIDAD*24 for i in range(7)]
        lista_valores[6]=60*CAPACIDAD*24-CAPACIDAD
        salida=dict(zip(lista_fechas,lista_valores))
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
    def test_reservaciones_de_una_hora_6_a_18_horas(self): # Esquina
        CAPACIDAD = 10
        HORAS_DIA = 12
        UNA_HORA = timedelta(hours=1)
        ahora = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0)
        e = self.crear_estacionamiento(CAPACIDAD,time(6,0),time(18,0))
        for i in range(CAPACIDAD):
            hora_reserva = ahora
            for j in range(7):
                for k in range(HORAS_DIA):
                    Reserva(estacionamiento=e,inicioReserva=hora_reserva,finalReserva=hora_reserva+UNA_HORA).save()
                    hora_reserva += UNA_HORA
                hora_reserva=ahora+timedelta(j+1)
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[60*CAPACIDAD*HORAS_DIA for i in range(7)]
        salida=dict(zip(lista_fechas,lista_valores))
        self.assertEqual(tasa_reservaciones(e.id),salida)
        
                
        
###################################################################
    # Casos de prueba para calcular tarifas        
##################################################################

    def test_estacionamiento_vacio(self):
        e=self.crear_estacionamiento(2)
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        ocupacion1=dict(zip(lista_fechas,lista_valores))
        calcular_porcentaje_de_tasa(hora_apertura=e.apertura,hora_cierre=e.cierre,capacidad=2, ocupacion=ocupacion1)
        self.assertEqual(dict(zip(lista_fechas,[Decimal(0) for i in range(7)])),ocupacion1)

    def test_estacionamiento_siempre_abierto_mitad_capacidad_primer_dia(self):
        e=self.crear_estacionamiento(2)
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=1440
        ocupacion1=dict(zip(lista_fechas,lista_valores))
        calcular_porcentaje_de_tasa(hora_apertura=e.apertura,hora_cierre=e.cierre,capacidad=2, ocupacion=ocupacion1)
        lista_valores2=[Decimal(0) for i in range(7)]
        lista_valores2[0]=Decimal(50)
        self.assertEqual(dict(zip(lista_fechas,lista_valores2)),ocupacion1)
    
    def test_estacionamiento_horario_restringido_mitad_capacidad_primer_dia(self):
        e=self.crear_estacionamiento(2,time(6,0),time(18,45))
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=765
        ocupacion1=dict(zip(lista_fechas,lista_valores))
        calcular_porcentaje_de_tasa(hora_apertura=e.apertura,hora_cierre=e.cierre,capacidad=2, ocupacion=ocupacion1)
        lista_valores2=[Decimal(0) for i in range(7)]
        lista_valores2[0]=Decimal(50)
        self.assertEqual(dict(zip(lista_fechas,lista_valores2)),ocupacion1)
        
    def test_estacionamiento_horario_restringido_toda_capacidad_primer_dia(self):
        e=self.crear_estacionamiento(2,time(6,0),time(18,45))
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=765*2
        ocupacion1=dict(zip(lista_fechas,lista_valores))
        calcular_porcentaje_de_tasa(hora_apertura=e.apertura,hora_cierre=e.cierre,capacidad=2, ocupacion=ocupacion1)
        lista_valores2=[Decimal(0) for i in range(7)]
        lista_valores2[0]=Decimal(50)*2
        self.assertEqual(dict(zip(lista_fechas,lista_valores2)),ocupacion1)
    
    def test_horario_restringido_toda_capacidad_primer_dia_y_un_minuto(self):
        e=self.crear_estacionamiento(2,time(6,0),time(18,45))
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=765*2
        lista_valores[1]=1
        ocupacion1=dict(zip(lista_fechas,lista_valores))
        calcular_porcentaje_de_tasa(hora_apertura=e.apertura,hora_cierre=e.cierre,capacidad=2, ocupacion=ocupacion1)
        lista_valores2=[Decimal(0) for i in range(7)]
        lista_valores2[0]=Decimal(50)*2
        lista_valores2[1]=Decimal(100)/Decimal(765*2)
        lista_valores2[1] = lista_valores2[1].quantize(Decimal('1.0'))
        self.assertEqual(dict(zip(lista_fechas,lista_valores2)),ocupacion1)
    
    def test_horario_restringido_toda_capacidad_primer_dia_exceso_1_minuto(self):
        e=self.crear_estacionamiento(2,time(6,0),time(18,45))
        ahora=datetime.now()
        lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
        lista_valores=[0 for i in range(7)]
        lista_valores[0]=765*2+1
        ocupacion1=dict(zip(lista_fechas,lista_valores))
        calcular_porcentaje_de_tasa(hora_apertura=e.apertura,hora_cierre=e.cierre,capacidad=2, ocupacion=ocupacion1)
        lista_valores2=[Decimal(0) for i in range(7)]
        lista_valores2[0]=Decimal(765*2+1)*100/Decimal(765*2)
        lista_valores2[0] = lista_valores2[0].quantize(Decimal('1.0'))
        self.assertEqual(dict(zip(lista_fechas,lista_valores2)),ocupacion1)