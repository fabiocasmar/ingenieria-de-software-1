# -*- coding: utf-8 -*-

from django.test import Client
from django.test import TestCase

from datetime import (
    datetime,
    time,
    timedelta,
)

from estacionamientos.models import (Estacionamiento, Propietario, Usuario, Billetera, Puestos)

###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class IntegrationTest(TestCase):
    
    # TDD
    def setUp(self):
        self.client = Client()
        
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
            #capacidad = puestos,
            #apertura       = hora_apertura,
            #cierre         = hora_cierre,
        )
        e.save()
        return e

    def crear_usuario(self):
        usua = Usuario(
            nombre = "nombre",
            apellido = "apellido",
            cedula = "24256878",
            )
        usua.save()
        return usua

    def test_crear_Billetera(self):
        b = Billetera(
            usuario = self.crear_usuario(),
            saldo = 0.00,
            pin = '1234'
        )
        b.save()
        return b

    # TDD
    def test_primera_vista_disponible(self):
        response = self.client.get('/estacionamientos/')
        self.assertEqual(response.status_code, 200)
    
    # malicia 
    def test_llamada_a_la_raiz_lleva_a_estacionamientos(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)
        
    # integracion TDD
    def test_llamada_a_los_detalles_de_un_estacionamiento(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle-estacionamiento.html')
    
    # integracion malicia
    def test_llamada_a_los_detalles_sin_estacionamiento_creado(self):
        response = self.client.get('/estacionamientos/1/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
    
    # integracion TDD
    def test_llamada_a_reserva(self):
        p = Puestos(particular = 20,
                    moto = 20,
                    carga = 20,
                    discapacitado = 20
        )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = p,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 200)

    # integracion TDD
    def test_llamada_a_billetera_electronica(self):
        b =Billetera(
            usuario = self.crear_usuario(),
            saldo = 0.00,
            pin = '1234'
        )
        b.save()
        response = self.client.get('/estacionamientos/menubilletera')
        self.assertEqual(response.status_code, 200)

    # integracion TDD
    def test_llamada_a_recargar_billetera(self):
        b =Billetera(
            usuario = self.crear_usuario(),
            saldo = 0.00,
            pin = '1234'
        )
        b.save()
        response = self.client.get('/estacionamientos/billetera_recargar')
        self.assertEqual(response.status_code, 200)

    # integracion TDD
    def test_llamada_a_consultar_saldo(self):
        b =Billetera(
            usuario = self.crear_usuario(),
            saldo = 0.00,
            pin = '1234'
        )
        b.save()
        response = self.client.get('/estacionamientos/billetera_saldo')
        self.assertEqual(response.status_code, 200)
        
    # integracion malicia 
    def test_llamada_a_reserva_sin_estacionamiento_creado(self):
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        
    # integracion malicia
    def test_llamada_a_tasa_sin_parametros_especificados_aun(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/tasa')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'template-mensaje.html')
        
    # integracion esquina
    def test_llamada_a_la_generacion_de_grafica_empty_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/grafica/')
        self.assertEqual(response.status_code, 400)
        
    # integracion TDD
    def test_llamada_a_la_generacion_de_grafica_normal_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/grafica/?2015-03-10=10.5')
        self.assertEqual(response.status_code, 200)
    
    # integracion malicia
    def test_llamada_a_la_generacion_de_grafica_bad_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/grafica/?hola=chao')
        self.assertEqual(response.status_code, 400)
    
    # integracion malicia
    def test_llamada_a_la_reserva_por_sms_bad_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/sms?phone=04242221111&text=hola')
        self.assertEqual(response.status_code, 400)
       
    # integracion esquina
    def test_llamada_a_la_reserva_por_sms_empty_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/sms')
        self.assertEqual(response.status_code, 400)
        
    # integracion esquina
    def test_llamada_a_reserva_sin_parametros_especificados_aun(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 403)
    
    # integracion TDD
    def test_llamada_a_consultar_reserva(self):
        response = self.client.get('/estacionamientos/consulta_reserva')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar-reservas.html')
    
    # integracion TDD 
    def test_llamada_a_consultar_ingreso(self):
        response = self.client.get('/estacionamientos/ingreso')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar-ingreso.html')
    
    # integracion malicia  
    def test_llamada_a_url_inexistente(self):
        response = self.client.get('/este/url/no/existe')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
    
    # integracion TDD
    def test_llamada_a_pago_get(self):
        p = Puestos(particular = 20,
                    moto = 20,
                    carga = 20,
                    discapacitado = 20
        )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = p,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.get('/estacionamientos/1/pago')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pago.html')
    
    # integracion TDD  
    def test_llamada_a_pago_post(self):
        p = Puestos(particular = 20,
                    moto = 20,
                    carga = 20,
                    discapacitado = 20
        )
        p.save()
        e = Estacionamiento(
            propietario = self.crear_propietario(),
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = p,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.post('/estacionamientos/1/pago')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pago.html')
    
    # integracion malicia
    def test_llamada_a_pago_sin_parametros_especificados_aun(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 403)
    
    # integracion malicia
    def test_llamada_a_pago_sin_estacionamiento_creado(self):
        response = self.client.get('/estacionamientos/1/pago')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')