# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time,datetime
from estacionamientos.controller import consultar_ingresos
from estacionamientos.models import (
                                        Pago,
                                        Estacionamiento,
                                        Propietario,
                                        Reserva,
                                        Puestos
                                    )

###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class consultaReservaTestCase(TestCase):
    
    def crear_propietario(self):
        prop = Propietario(
            nombre = "nom",
            apellido = "apell",
            cedula = "V-041414141111",
            telefono = "041414141112",
            email = "hola@gmail.com",
            )
        prop.save()
        return prop

    #TDD
    def test_sin_estacionamiento(self):
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == total )

    # TDD
    def test_estacionamiento_sin_pagos(self):
        p = Puestos(
            particular = 20,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            telefono1 = "041414141111",
            telefono2 = "041414141112",
            telefono3 = "04141414111",
            email1 = "hola@gmail.com",
            email2 = "hola@gmail.com",
            rif = "J-123456789",
            capacidad   = p,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == 0)

    # TDD
    def test_un_estacionamiento_un_pago(self):
        p = Puestos(
            particular = 20,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            telefono1 = "041414141111",
            telefono2 = "041414141112",
            telefono3 = "04141414111",
            email1 = "hola@gmail.com",
            email2 = "hola@gmail.com",
            rif =   "J-123456789",
            capacidad   = p,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        r = Reserva(
                estacionamiento = e,
                inicioReserva = datetime(2015,3,10,3,0),
                finalReserva  = datetime(2015,3,10,5,0),
                tipo_puesto = 'Particular'
            )
        r.save()
        p = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = "V-1234567",
                tarjetaTipo      = "VISTA",
                reserva          = r,
                monto            = 150,
            )
        p.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == 150)
    #TDD malicia
    def test_un_estacionamiento_muchos_pagos(self):
        n = 1000
        p = Puestos(
            particular = n,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            telefono1 = "041414141111",
            telefono2 = "041414141112",
            telefono3 = "04141414111",
            email1 = "hola@gmail.com",
            email2 = "hola@gmail.com",
            rif = "J-123456789",
            capacidad   = p,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        for i in range(0,n):
            r = Reserva(
                    estacionamiento = e,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0),
                    tipo_puesto = 'Particular'
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tarjetaTipo      = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == n*100)

    #malicia
    def test_dos_estacionamiento_muchos_pagos(self):
        n = 1000
        p = Puestos(
            particular = n,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            telefono1 = "041414141111",
            telefono2 = "041414141112",
            telefono3 = "04141414111",
            email1 = "hola@gmail.com",
            email2 = "hola@gmail.com",
            rif = "J-123456789",
            capacidad   = p,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        for i in range(0,n):
            r = Reserva(
                    estacionamiento = e,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0),
                    tipo_puesto = 'Particular'
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tarjetaTipo      = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()

        
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == n*100)



    def test_muchos_estacionamiento_mitad_sin_pagos(self):
        n = 100
        m = 10
        p1 = Puestos(
            particular = n,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p1.save()
        p2 = Puestos(
            particular = m,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p2.save()
        for i in range(0,n):
            prop = Propietario(
            nombre = "prop%d"%i,
            apellido = "apell",
            cedula = "V-041414141111",
            telefono = "041414141112",
            email = "hola@gmail.com",
            )
            prop.save()
            e1 = Estacionamiento(
                propietario = prop,
                nombre      = "nom%d"%i,
                direccion   = "dir1",
                rif         = "J-123456789",
                capacidad   = p1,
                apertura    = time(0,0),
                cierre      = time(23,59),
            )
            pro = Propietario(
            nombre = "pro%d"%i,
            apellido = "apell",
            cedula = "V-041414141111",
            telefono = "041414141112",
            email = "hola@gmail.com",
            )
            pro.save()
            e2 = Estacionamiento(
                propietario = pro,
                nombre      = "no%d"%i,
                direccion   = "dir3",
                rif         = "J-123456789",
                capacidad   = p2,
                apertura    = time(0,0),
                cierre      = time(23,59),
            )
            e1.save()
            e2.save()
            for j in range(0,m):
                r = Reserva(
                        estacionamiento = e1,
                        inicioReserva = datetime(2015,3,10,3,0),
                        finalReserva  = datetime(2015,3,10,5,0),
                        tipo_puesto = 'Particular'
                    )
                r.save()
                p = Pago(
                        fechaTransaccion = datetime.now(),
                        cedula           = "V-1234567",
                        tarjetaTipo      = "VISTA",
                        reserva          = r,
                        monto            = 100,
                    )
                p.save()

        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 2*n and total == n*m*100)

    def test_muchos_estacionamiento_sin_pagos(self):
        n  = 1000
        p = Puestos(
            particular = n,
            moto = 20,
            carga = 20,
            discapacitado = 20
            )
        p.save()
        for i in range(0,n):
            prop = Propietario(
            nombre = "prop%d"%i,
            apellido = "apell",
            cedula = "V-041414141111",
            telefono = "041414141112",
            email = "hola@gmail.com",
            )
            prop.save()
            e1 = Estacionamiento(
                propietario = prop,
                nombre      = "nom%d"%i,
                direccion   = "dir1",
                rif         = "J-123456789",
                capacidad   = p,
                apertura    = time(0,0),
                cierre      = time(23,59),
            )
            e1.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == n and total == 0)

    def test_muchos_estacionamiento_con_disintos_rif(self):
        n  = 1000
        for i in range(0,n):
            prop = Propietario(
            nombre = "prop%d"%i,
            apellido = "apell",
            cedula = "V-041414141111",
            telefono = "041414141112",
            email = "hola@gmail.com",
            )
            prop.save()
            p = Puestos(
                particular = n,
                moto = 20,
                carga = 20,
                discapacitado = 20
                )
            p.save()
            e1 = Estacionamiento(
                propietario = prop,
                nombre      = "nom%d"%i,
                direccion   = "dir1",
                rif         = "J-%i"%(123456789-i),
                capacidad   = p,
                apertura    = time(0,0),
                cierre      = time(23,59),
            )
            e1.save()
            r = Reserva(
                    estacionamiento = e1,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0),
                    tipo_puesto = 'Particular'
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tarjetaTipo      = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == 100)

