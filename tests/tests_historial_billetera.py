# -*- coding: utf-8 -*- 

from django.test import TestCase

from estacionamientos.controller import (
                                            obtener_consumos,
                                            obtener_recargas,
                                            recargar_saldo,
                                            consumir_saldo
                                        )    
from estacionamientos.models import (
                                        Billetera,
                                        Usuario,
                                    )

###################################################################
#             BILLETERA MOSTRAR MOVIMIENTOS
###################################################################

class mostrarHistorialTestCase(TestCase):

    def crear_usuario(self):
        usu = Usuario(
            nombre = "nom",
            apellido = "apell",
            cedula = "2345678",
            )
        usu.save()
        return usu   

    def crear_billetera(self):
        b = Billetera(
            usuario = self.crear_usuario(),
            saldo = 0.00,
            pin = 1234
        )
        b.save()
        return b

    # TDD
    def test_billetera_nueva(self):
        b = self.crear_billetera()
        consumos = obtener_consumos(1,'1234')
        recargas = obtener_recargas(1,'1234')
        self.assertFalse(consumos)
        self.assertFalse(recargas)


    # Malicia
    def test_Pin_distinto(self):
        b = self.crear_billetera()
        sePuede =  obtener_consumos(1,'1234jk')
        self.assertFalse(sePuede)
        sePuede =  obtener_recargas(1,'1234jk')
        self.assertFalse(sePuede)

    # Malicia
    def test_Billetera_inexistente(self):
        sePuede =  obtener_consumos(100,'1234jk')
        self.assertFalse(sePuede)
        sePuede =  obtener_recargas(100,'1234jk')
        self.assertFalse(sePuede)    

    # TDD
    def test_una_recarga(self):
        b = self.crear_billetera()
        recarga = recargar_saldo(b.id,'1234',0)
        recargas = obtener_recargas(b.id,'1234')
        for elemento in recargas:
            self.assertTrue(elemento.id == recarga.id) 

    # Borde
    def test_muchas_recargas(self):
        b = self.crear_billetera()
        
        for num in range(0,10000):
            recargar_saldo(b.id,'1234',0)

        id = 0 
        recargas = obtener_recargas(b.id,'1234')  

        for elemento in recargas:
            self.assertTrue(elemento.id == id)  
            id = id+1         

    # TDD
    def test_un_consumo(self):
        b = self.crear_billetera()
        consumo = consumir_saldo(b.id,'1234',0)
        consumos = obtener_consumos(b.id,'1234')
        for elemento in consumos:
            self.assertTrue(elemento.id == consumos.id) 

    # Borde
    def test_muchos_consumos(self):
        b = self.crear_billetera()
        
        for num in range(0,10000):
            consumir_saldo(b.id,'1234',0)

        id = 0 
        consumos = obtener_consumos(b.id,'1234')  

        for elemento in consumos:
            self.assertTrue(elemento.id == id)  
            id = id+1        