import datetime
from decimal import Decimal
from calcularPrecio import calcularPrecio, Tarifa
import unittest

class PruebasTarifa(unittest.TestCase):



	def test_RecargaMontoMaximoInvalido(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera, 0, datetime.now(),1)

	def test_RecargaMontoNegativo(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera,-10,datetime.now(),1)

	def test_RecargaFechaPasada(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera,10,datetime.datetime(2015,5,23,18,25,0,0),1)

	def test_RecargaFechaFutura(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera,10,datetime.datetime(2016,5,23,18,25,0,0),1))
	
	def test_RecargaMuyGrande(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera,10000000000000000000000000000000000000000,datetime.now(),1)

	def test_RecargaMinima(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera,1,datetime.now(),1)

	def test_RecargaCuentaInvalida(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		self.assertRaises(Exception,Recargar,nuevaBilletera,10,datetime.now(),20000)

	def test_DebitoMontoNegativo(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,1,0,datetime.now(),1,1234)

	def test_DebitoMontoNegativo(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,2,-1,datetime.now(),1,1234)
	
	def test_DebitoFechaPasada(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,3,10,datetime.datetime(2015,5,23,18,25,0,0),1,1234)
		
	def test_DebitoFechaFutura(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,4,10,datetime.datetime(2016,5,23,18,25,0,0),1,1234)
	
	def test_DebitoMuyGrande(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,5,10000000000000000000000000000000000000000,datetime.now(),1,1234)

	def test_DebitoMinima(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,6,1,datetime.now(),1,1234)

	def test_DebitoCuentaInvalida(self):
		nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
		Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
		self.assertRaises(Exception,Consumir,7,10,datetime.now(),20000,1234)