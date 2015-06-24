# Archivo con funciones de control para SAGE
from estacionamientos.models import Estacionamiento, Reserva, Pago, Billetera, Recarga, Consumo, CancelarReserva, Reembolso, Sage
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta, time
from decimal import Decimal
from collections import OrderedDict
from django.core.exceptions import ObjectDoesNotExist

# chequeo de horarios de extended
def HorarioEstacionamiento(HoraInicio, HoraFin):
	return HoraFin > HoraInicio

def validarHorarioReserva(inicioReserva, finReserva, apertura, cierre, horizonteDias, horizonteHoras):
	if inicioReserva >= finReserva:
		return (False, 'El horario de inicio de reservacion debe ser menor al horario de fin de la reserva.')
	if finReserva - inicioReserva < timedelta(hours=1):
		return (False, 'El tiempo de reserva debe ser al menos de 1 hora.')
	if inicioReserva.date() < datetime.now().date():
		return (False, 'La reserva no puede tener lugar en el pasado.')

	if finReserva > (datetime.now()+timedelta(days=int(horizonteDias),hours=int(horizonteHoras))):
		return (False, 'La reserva debe estar dentro de los proximos'+str(horizonteDias)+' dia(s) y '+str(horizonteHoras)+' hora(s)')
	if apertura.hour==0 and apertura.minute==0 \
		and cierre.hour==23 and cierre.minute==59:
		horizonte=timedelta(days=int(horizonteDias),hours=int(horizonteHoras))
		if finReserva-inicioReserva<=horizonte :
			return (True,'')
		else:
			return(False,str('Se puede reservar un puesto por un máximo de '+horizonteDias+' dias '+horizonteHoras+' horas'))
	else:
		hora_inicio = time(hour = inicioReserva.hour, minute = inicioReserva.minute)
		hora_final  = time(hour = finReserva.hour   , minute = finReserva.minute)
		if hora_inicio<apertura:
			return (False, 'El horario de inicio de reserva debe estar en un horario válido.')
		if hora_final > cierre:
			return (False, 'El horario de fin de la reserva debe estar en un horario válido.')
		if inicioReserva.date()!=finReserva.date():
			return (False, 'No puede haber reservas entre dos dias distintos')
		return (True,'')

def marzullo(idEstacionamiento, hIn, hOut):
	e = Estacionamiento.objects.get(id = idEstacionamiento)
	ocupacion = []
	capacidad = e.capacidad

	for reserva in e.reserva_set.all():
		ocupacion += [(reserva.inicioReserva, 1), (reserva.finalReserva, -1)]
	ocupacion += [(hIn, 1), (hOut, -1)]

	count = 0
	for r in sorted(ocupacion):
		count += r[1]
		if count > capacidad:
			return False
	return True

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def tasa_reservaciones(id_estacionamiento,prt=False):
	e = Estacionamiento.objects.get(id = id_estacionamiento)
	ahora = datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)
	reservas_filtradas = e.reserva_set.filter(finalReserva__gt=ahora)
	lista_fechas=[(ahora+timedelta(i)).date() for i in range(7)]
	lista_valores=[0 for i in range(7)]
	ocupacion_por_dia = OrderedDict(zip(lista_fechas,lista_valores))
	UN_DIA = timedelta(days = 1)
	
	for reserva in reservas_filtradas:
		# Caso del inicio de la reserva
		if (reserva.inicioReserva < ahora):
			reserva_inicio = ahora
		else:
			reserva_inicio = reserva.inicioReserva
		reserva_final = reserva.finalReserva
		final_aux=reserva_inicio.replace(hour=0,minute=0,second=0,microsecond=0)
		while (reserva_final.date()>reserva_inicio.date()): 
			final_aux+=UN_DIA
			longitud_reserva = final_aux-reserva_inicio
			ocupacion_por_dia[reserva_inicio.date()] += longitud_reserva.seconds/60+longitud_reserva.days*24*60
			reserva_inicio = final_aux
		longitud_reserva=reserva_final-reserva_inicio
		ocupacion_por_dia[reserva_inicio.date()] += longitud_reserva.seconds/60 + longitud_reserva.days*24*60
			
	return ocupacion_por_dia

def calcular_porcentaje_de_tasa(hora_apertura,hora_cierre, capacidad, ocupacion):
	factor_divisor=timedelta(hours=hora_cierre.hour,minutes=hora_cierre.minute)
	factor_divisor-=timedelta(hours=hora_apertura.hour,minutes=hora_apertura.minute)
	factor_divisor=Decimal(factor_divisor.seconds)/Decimal(60)
	if (hora_apertura==time(0,0) and hora_cierre==time(23,59)):
		factor_divisor+=1 # Se le suma un minuto
	for i in ocupacion.keys():
		ocupacion[i]=(Decimal(ocupacion[i])*100/(factor_divisor*capacidad)).quantize(Decimal('1.0'))

def consultar_ingresos(rif):
            listaEstacionamientos = Estacionamiento.objects.filter(rif = rif)
            ingresoTotal          = 0
            listaIngresos         = []

            for estacionamiento in listaEstacionamientos:
                listaFacturas = Pago.objects.filter(
                    reserva__estacionamiento__nombre = estacionamiento.nombre
                )
                ingreso       = [estacionamiento.nombre, 0]
                for factura in listaFacturas:
                    ingreso[1] += factura.monto
                listaIngresos += [ingreso]
                ingresoTotal  += ingreso[1]

            return listaIngresos, ingresoTotal

def recargar_saldo(_id,_pin,monto):
	try:
		billetera_electronica = Billetera.objects.get(id =_id)
	except ObjectDoesNotExist:
		return False
		
	if _pin == billetera_electronica.pin:
		if float(float(billetera_electronica.saldo)+float(monto)) > 10000:
			return True
		else:
			billetera_electronica.saldo = float(float(billetera_electronica.saldo)+float(monto))
			billetera_electronica.save()
			return billetera_electronica.saldo
	else:
		return False


def consumir_saldo(_id,_pin,monto):
	try:
		billetera_electronica = Billetera.objects.get(id =_id)
	except ObjectDoesNotExist:
		return False

	if _pin == billetera_electronica.pin:
		if float(billetera_electronica.saldo) >= float(monto):
			billetera_electronica.saldo = float(float(billetera_electronica.saldo)-float(monto))
			billetera_electronica.save()
			return True
		else:
			return  format(float(billetera_electronica.saldo), '.2f')
	else:
		return False

def mostrar_saldo(_id,_pin):
	try:
		billetera_electronica = Billetera.objects.get(id =_id)
	except ObjectDoesNotExist:
		return False
	billetera_electronica = Billetera.objects.get(id=_id)
	if _pin == billetera_electronica.pin:
		return True
	else:
		return False


def check_pin(id_belletera,pin_billetera):
    try: 
        billetera_electronica = Billetera.objects.get(id = id_belletera)
    except ObjectDoesNotExist:
        return False
    if pin_billetera == billetera_electronica.pin:
        return True
    else:
        return False


def cambiar_pin(_id,_pin):
	try: 
		billetera_electronica = Billetera.objects.get(id = _id)
	except ObjectDoesNotExist:
		return False
	if _pin == billetera_electronica.pin:
		return True
	else:
		return False
	
def cancelacion(_ci,_pin,_billetera,_pago ):
	
	try:
		pago = Pago.objects.get(id = _pago)
	except ObjectDoesNotExist:
		return (False,'Numero de confirmacion invalido') 
	
	try:
		billetera = Billetera.objects.get(id = _billetera)
	except ObjectDoesNotExist:
		return (False,'Datos invalidos de la billetera electronica')
                
	if (pago.reserva.inicioReserva < datetime.now()):
		return (False,'La fecha de reserva ya ocurrio, no es posible cancelarla')  
                                  

	if ( pago.cedula != _ci):
		return (False,'Numero de cedula errada. Debe introducir el numero de cedula asociado a la factura de pago')
                      	
	if (billetera.pin != _pin):
		return (False,'Datos invalidos de la billetera electronica')
                      	
	else:
		return (True,'')
	
def crear_cancelacion(billetera_id,numero_pago ):
	try:
		
		pago = Pago.objects.get(id=numero_pago)
		billetera   = Billetera.objects.get(id=billetera_id)

		if (pago.tarjetaTipo!= ''):
			try:
				sage = Sage.objects.all() 
				for elemento in sage:
					multa = elemento.deduccion

			except ObjectDoesNotExist:	
				multa = 0	
			
		else:
			multa = 0 

		multa = pago.monto * multa		
		
		obj = CancelarReserva(
			estacionamiento   = Estacionamiento.objects.get(id=pago.reserva.estacionamiento.id),
			fechaTransaccion = datetime.now(),
			billetera   = Billetera.objects.get(id=billetera_id),
			inicioReserva = pago.reserva.inicioReserva,
			finalReserva = pago.reserva.finalReserva,
			cedula = pago.cedula,
			multa = multa                    
	    )
		reserva  = Reserva.objects.get(id=pago.reserva.id)
		
		recargar_saldo(billetera_id,billetera.pin,pago.monto - multa)
		
		reembolso = Reembolso(	nombre= reserva.nombre,
								apellido = reserva.apellido,
								cedula = reserva.cedula,
								estacionamiento = reserva.estacionamiento,
								inicioReserva = reserva.inicioReserva,
								finalReserva = reserva.finalReserva,
								saldo = pago.monto - multa,
								fechaTransaccion = obj.fechaTransaccion,
								fechaTransaccion_vieja = pago.fechaTransaccion,
								billetera = billetera,
								id_viejo = pago.reserva.id,
								monto_reserva = pago.monto,
								mensaje = "Reserva cancelada"
								)
	
		reembolso.save()
		reserva.delete()
		obj.save()
		
		return (True,obj)
	except:
		return(False, '')
		
def obtener_recargas(_id,_pin):
	try:
		billetera_electronica = Billetera.objects.get(id = _id)
	except ObjectDoesNotExist:
		return False
	if _pin == billetera_electronica.pin:
		recargas = Recarga.objects.filter(billetera = billetera_electronica)
		listaRecargas = []
		for elemento in recargas:
			listaRecargas.append(elemento)
		return recargas
	else:
		return False


def obtener_consumos(_id,_pin):
	try:
		billetera_electronica = Billetera.objects.get(id = _id)
	except ObjectDoesNotExist:
		return False
	if _pin == billetera_electronica.pin:
		consumos = Consumo.objects.filter(billetera = billetera_electronica)
		listaConsumos = []
		for elemento in consumos:
			listaConsumos.append(elemento)
			return consumos
	else:
		return False

def obtener_reembolsos(_id,_pin):
	try:
		billetera_electronica = Billetera.objects.get(id = _id)
	except ObjectDoesNotExist:
		return False
	if _pin == billetera_electronica.pin:
		reembolsos = Reembolso.objects.filter(billetera = billetera_electronica)
		listaReembolsos = []
		for elemento in reembolsos:
			listaReembolsos.append(elemento)
			return reembolsos
	else:
		return False

def chequear_mover_reserva(cedula,reserva_id):
	
	try:
		pago = Pago.objects.get(id = reserva_id)
		#reserva = Reserva.objects.get(id = reserva_id)
	except ObjectDoesNotExist:
		return False
	reserva = pago.reserva
	if reserva.cedula != cedula:
		return False
	else:
		return True

def nuevo_monto_reserva(monto_viejo,monto_nuevo):
	if monto_viejo>monto_nuevo:
		monto_actual = monto_viejo-monto_nuevo
		return True,monto_actual
	elif monto_nuevo>monto_viejo:
		monto_actual = monto_nuevo-monto_viejo
		return False,monto_actual
	elif monto_viejo==monto_nuevo:
		monto_actual = monto_nuevo-monto_viejo
		return -1,monto_actual

def mover_reserva(reserva,inicio,fin):
	reserva.inicioReserva = inicio
	reserva.finalReserva = fin
	reserva.save()

# Chequear si el usuario pago con billetera
def chequear_consumo_billetera(pago,reserva):
	consumo = Consumo.objects.filter(reserva=reserva)
	if len(consumo)>0:
		for obj in consumo:
			if obj.flag=="1" and reserva.movidas==1.0:
				return True
			else:
				return False
	else:
		return False

def guardar_configuracion(deduc):

	if (0.00>float(deduc) or 10.00<float(deduc)):
		return (False, 'El monto de deduccion debe estar entre 0.00 y 10.00')

	else:	
		Sage.objects.all().delete()
		obj = Sage(
			deduccion = (float(deduc)/100)
			)

		obj.save()
		return (True, 'Configuracion realizada con exito')
