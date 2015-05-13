class Billetera(models.Model):
	nombre      	= models.CharField(max_length = 50)
	apellido	    = models.CharField(max_length = 50)
	cedulaTipo      = models.CharField(max_length = 1)}
	cedula          = models.CharField(max_length = 10)
	pin				= models.DecimalField(max_digits=4, decimal_places=0)
	saldo		    = models.DecimalField(max_digits=1000, decimal_places=2)

	def __str__(self):
		return self.nombre+' '+self.apellido+' '+self.cedula+' '+str(saldo)

class Billetera:

    def __init__(self, nombre,apellido,cedulaTipo,cedula,pin,saldo):
		self.nombre      	= nombre
		self.apellido	    = apellido
		self.cedulaTipo     = cedulaTipo
		self.cedula         = cedula
		self.pin			= pin
		self.saldo 			= 0

	def __str__(self):
		return self.nombre+' '+self.apellido+' '+self.cedula+' '+str(saldo)