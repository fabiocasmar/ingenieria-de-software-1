# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import render_to_response
import urllib
from django.http import HttpResponse, Http404
from django.utils.dateparse import parse_datetime
from urllib.parse import urlencode
from matplotlib import pyplot
from decimal import *
from collections import OrderedDict
from datetime import (
    datetime, timedelta, time
)

from estacionamientos.controller import (
    HorarioEstacionamiento,
    validarHorarioReserva,
    marzullo,
    get_client_ip,
    tasa_reservaciones,
    calcular_porcentaje_de_tasa,
    consultar_ingresos,
    mostrar_saldo,
    recargar_saldo,
    consumir_saldo,
    cancelacion,
    crear_cancelacion,
    obtener_recargas,
    obtener_consumos,
    obtener_reembolsos,
    chequear_mover_reserva,
    nuevo_monto_reserva,
    mover_reserva,
    chequear_consumo_billetera,
    guardar_configuracion
)

from estacionamientos.forms import (
    EstacionamientoExtendedForm,
    EstacionamientoForm,
    ReservaForm,
    PagoForm,
    RifForm,
    CedulaForm,
    PropietarioForm,
    RecargaForm,
    ConsumirForm,
    SaldoForm,
    CrearBilleteraForm,
    ModificarPropietarioForm,
    CancelarReservaForm,
    MovimientosForm,
    ReservaCIForm,
    CambiarReservaForm,
    SageForm
)

from estacionamientos.models import (
    Estacionamiento,
    Reserva,
    Pago,
    TarifaHora,
    TarifaMinuto,
    TarifaHorayFraccion,
    TarifaFinDeSemana,
    TarifaHoraPico,
    Propietario,
    Usuario,
    Billetera,
    Recarga,
    Consumo,
    CancelarReserva,
    Reembolso,
    Sage
)

#from django.template.context_processors import request

# Usamos esta vista para procesar todos los estacionamientos.
def estacionamientos_all(request):
    estacionamientos = Estacionamiento.objects.all()
    # Si es un GET, mandamos un formulario vacio
    if request.method == 'POST':
        # Creamos un formulario con los datos que recibimos
        # Parte de la entrega era limitar la cantidad maxima de
        # estacionamientos a 5
        if len(estacionamientos) >= 5:
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'No se pueden agregar más estacionamientos'
                }
            )
        
        form = CedulaForm(request.POST)
        if form.is_valid():
            try:
                obj = Propietario.objects.get(cedula = form.cleaned_data['cedula'])
                form_data = {
                    'nombre' : obj.nombre,
                    'apellido' : obj.apellido,
                    'cedula' : obj.cedula,
                    'telefono' : obj.telefono,
                    'email' : obj.email,
                }
                form = PropietarioForm(data = form_data)
                cedula = obj.cedula
                estacionamientos = Estacionamiento.objects.all
                return render(
                    request,
                    'propietario_editar_catalogo.html',
                    { 'form': form, 'cedula' : cedula
                    , 'estacionamientos': estacionamientos
                    }
                )
            except ObjectDoesNotExist:
                cedula = form.cleaned_data['cedula']
                form = PropietarioForm()
                return render(
                request,
                    'propietario_crear_catalogo.html',
                    { 'form': form, 'cedula': cedula
                    , 'estacionamientos': estacionamientos
                    }
                )
    espacio = " "
    form = CedulaForm()
    return render(
    request,
        'catalogo-estacionamientos.html',
        { 'form': form
        , 'estacionamientos': estacionamientos
        , 'espacio' : espacio
        }
    )

# Usamos esta vista para procesar todos los estacionamientos
def propietario_crear_editar(request, _id):
    estacionamientos = Estacionamiento.objects.all()
    form = PropietarioForm(request.POST)
    if form.is_valid():
        try:
            obj = Propietario.objects.get(cedula = _id)
            obj.nombre = form.cleaned_data['nombre']
            obj.apellido = form.cleaned_data['apellido']
            obj.cedula = form.cleaned_data['cedula']
            obj.telefono = form.cleaned_data['telefono']
            obj.email = form.cleaned_data['email']
            obj.save()
        except ObjectDoesNotExist:
            prop = Propietario(
                    nombre = form.cleaned_data['nombre'],
                    apellido = form.cleaned_data['apellido'],
                    cedula = form.cleaned_data['cedula'],
                    telefono = form.cleaned_data['telefono'],
                    email = form.cleaned_data['email'],
                )
            prop.save()
        cedula=form.cleaned_data['cedula']
        form=EstacionamientoForm()
        return render(
            request,
            'crear_estacionamiento.html',
            { 'form': form,'cedula' : cedula
            , 'estacionamientos': estacionamientos
            }
        )
    else: 
        return render(
            request,
            'propietario_crear_catalogo_2.html',
            { 'form': form,'cedula' : form.cleaned_data['cedula']
            , 'estacionamientos': estacionamientos
            }
    )


# Usamos esta vista para procesar todos los estacionamientos
def crear_estacionamiento(request, _id):
    estacionamientos = Estacionamiento.objects.all()
    form = EstacionamientoForm(request.POST)
    if form.is_valid():
        obj = Propietario.objects.get(cedula = _id)
        prop = Estacionamiento(
            propietario = obj,
            nombre = form.cleaned_data['nombre'],
            direccion = form.cleaned_data['direccion'],
            telefono1 = form.cleaned_data['telefono1'],
            telefono2 = form.cleaned_data['telefono2'],
            telefono3 = form.cleaned_data['telefono3'],
            email1 = form.cleaned_data['email1'], 
            email2 = form.cleaned_data['email2'],
            rif = form.cleaned_data['rif'],
            )
        prop.save()
        form = CedulaForm()
        estacionamientos = Estacionamiento.objects.all
        return redirect('estacionamientos_all')
    else:
        return render(
            request,
            'crear_estacionamiento.html',
            { 'form': form,'cedula' : _id
            , 'estacionamientos': estacionamientos
            }
        )

def estacionamiento_detail(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404

    if request.method == 'GET':
        if estacionamiento.tarifa:
            
            form_data = {
                'horarioin' : estacionamiento.apertura,
                'horarioout' : estacionamiento.cierre,
                'tarifa' : estacionamiento.tarifa.tarifa,
                'tarifa2' : estacionamiento.tarifa.tarifa2,
                'inicioTarifa2' : estacionamiento.tarifa.inicioEspecial,
                'finTarifa2' : estacionamiento.tarifa.finEspecial,
                'puestos' : estacionamiento.capacidad,
                'esquema' : estacionamiento.tarifa.__class__.__name__,
                'horizonteDias': estacionamiento.horizontedias,
                'horizonteHoras': estacionamiento.horizontehoras 
            }
            form = EstacionamientoExtendedForm(data = form_data)
        else:
            form = EstacionamientoExtendedForm()

    elif request.method == 'POST':
        # Leemos el formulario
        form = EstacionamientoExtendedForm(request.POST)
        # Si el formulario
        if form.is_valid():
            horaIn          = form.cleaned_data['horarioin']
            horaOut         = form.cleaned_data['horarioout']
            tarifa          = form.cleaned_data['tarifa']
            tipo            = form.cleaned_data['esquema']
            inicioTarifa2   = form.cleaned_data['inicioTarifa2']
            finTarifa2      = form.cleaned_data['finTarifa2']
            tarifa2         = form.cleaned_data['tarifa2']
            horizonteDias   = form.cleaned_data['horizonteDias'] 
            horizonteHoras  = form.cleaned_data['horizonteHoras'] 
            horizonteActual = timedelta(days=int(horizonteDias),hours=int(horizonteHoras))
            horizonteMaximo = timedelta(days=15)
            if horizonteActual > horizonteMaximo:
                return render(
                    request,
                    'template-mensaje.html',
                    { 'color':'red'
                    , 'mensaje': 'El horizonte máximo de reserva es de 15 días'
                    }
                )
            esquemaTarifa = eval(tipo)(
                tarifa         = tarifa,
                tarifa2        = tarifa2,
                inicioEspecial = inicioTarifa2,
                finEspecial    = finTarifa2
            )

            esquemaTarifa.save()
            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            if not HorarioEstacionamiento(horaIn, horaOut):
                return render(
                    request,
                    'template-mensaje.html',
                    { 'color':'red'
                    , 'mensaje': 'El horario de apertura debe ser menor al horario de cierre'
                    }
                )
            # debería funcionar con excepciones
            estacionamiento.tarifa         = esquemaTarifa
            estacionamiento.apertura       = horaIn
            estacionamiento.cierre         = horaOut
            estacionamiento.capacidad      = form.cleaned_data['puestos']
            estacionamiento.horizontedias  = horizonteDias
            estacionamiento.horizontehoras = horizonteHoras

            estacionamiento.save()

    return render(
        request,
        'detalle-estacionamiento.html',
        { 'form': form
        , 'estacionamiento': estacionamiento
        }
    )


def estacionamiento_reserva(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404

    # Verificamos que el estacionamiento este parametrizado
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # Esta prohibido entrar aun

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = ReservaForm()

    # Si es un POST estan mandando un request
    elif request.method == 'POST':
        form = ReservaForm(request.POST)
        # Verificamos si es valido con los validadores del formulario
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            cedula = form.cleaned_data['cedula']
            inicioReserva = form.cleaned_data['inicio']
            finalReserva = form.cleaned_data['final']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(
                inicioReserva,
                finalReserva,
                estacionamiento.apertura,
                estacionamiento.cierre,
                estacionamiento.horizontedias,
                estacionamiento.horizontehoras
            )

            # Si no es valido devolvemos el request
            if not m_validado[0]:
                return render(
                    request,
                    'template-mensaje.html',
                    { 'color'  :'red'
                    , 'mensaje': m_validado[1]
                    }
                )

            if marzullo(_id, inicioReserva, finalReserva):
                reservaFinal = Reserva(
                    estacionamiento = estacionamiento,
                    inicioReserva   = inicioReserva,
                    finalReserva    = finalReserva,
                    nombre          = form.cleaned_data['nombre'],
                    cedula          = form.cleaned_data['cedula'],
                    apellido 	    = form.cleaned_data['apellido']
		        )

                monto = Decimal(
                    estacionamiento.tarifa.calcularPrecio(
                        inicioReserva,finalReserva
                    )
                )

                request.session['monto'] = float(
                    estacionamiento.tarifa.calcularPrecio(
                        inicioReserva,
                        finalReserva
                    )
                )
                request.session['finalReservaHora']    = finalReserva.hour
                request.session['finalReservaMinuto']  = finalReserva.minute
                request.session['inicioReservaHora']   = inicioReserva.hour
                request.session['inicioReservaMinuto'] = inicioReserva.minute
                request.session['anioinicial']         = inicioReserva.year
                request.session['mesinicial']          = inicioReserva.month
                request.session['diainicial']          = inicioReserva.day
                request.session['aniofinal']           = finalReserva.year
                request.session['mesfinal']            = finalReserva.month
                request.session['diafinal']            = finalReserva.day
                request.session['nombre']              = reservaFinal.nombre
                request.session['apellido']            = reservaFinal.apellido
                request.session['cedula']              = reservaFinal.cedula
                
                return render(
                            request,
                            'confirmar.html',
                            { 'id'      : _id
                            , 'monto'   : monto
                            , 'reserva' : reservaFinal
                            , 'color'   : 'green'
                            , 'mensaje' : 'Existe un puesto disponible'
                            }
                        )
            else:
                # Cambiar mensaje
                return render(
                    request,
                    'template-mensaje.html',
                    {'color'   : 'red'
                    , 'mensaje' : 'No hay un puesto disponible para ese horario'
                    }
                )

    return render(
        request,
        'reserva.html',
        { 'form': form
        , 'estacionamiento': estacionamiento
        }
    )

def estacionamiento_pago(request,_id):
    form = PagoForm()
    
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404
    
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # No esta permitido acceder a esta vista aun
    
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            
            inicioReserva = datetime(
                year   = request.session['anioinicial'],
                month  = request.session['mesinicial'],
                day    = request.session['diainicial'],
                hour   = request.session['inicioReservaHora'],
                minute = request.session['inicioReservaMinuto']
            )

            finalReserva  = datetime(
                year   = request.session['aniofinal'],
                month  = request.session['mesfinal'],
                day    = request.session['diafinal'],
                hour   = request.session['finalReservaHora'],
                minute = request.session['finalReservaMinuto']
            )

            reservaFinal = Reserva(
                nombre = request.session['nombre'],
                apellido = request.session['apellido'],
                cedula = request.session['cedula'],
                estacionamiento = estacionamiento,
                inicioReserva   = inicioReserva,
                finalReserva    = finalReserva
            )

            # Se guarda la reserva en la base de datos
            reservaFinal.save()

            monto = Decimal(request.session['monto']).quantize(Decimal(10) ** -2)
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = form.cleaned_data['cedula'],
                monto            = monto,
                tarjetaTipo      = form.cleaned_data['tarjetaTipo'],
                reserva          = reservaFinal,
            )


            # Se guarda el recibo de pago en la base de datos
            pago.save()

            return render(
                request,
                'pago.html',
                { "id"      : _id
                , "pago"    : pago
                , "color"   : "green"
                , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                }
            )

    return render(
        request,
        'pago.html',
        { 'form' : form }
    )

def estacionamiento_ingreso(request):
    form = RifForm()
    if request.method == 'POST':
        form = RifForm(request.POST)
        if form.is_valid():

            rif = form.cleaned_data['rif']
            listaIngresos, ingresoTotal = consultar_ingresos(rif)

            return render(
                request,
                'consultar-ingreso.html',
                { "ingresoTotal"  : ingresoTotal
                , "listaIngresos" : listaIngresos
                , "form"          : form
                }
            )

    return render(
        request,
        'consultar-ingreso.html',
        { "form" : form }
    )

def estacionamiento_consulta_reserva(request):
    form = CedulaForm()
    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula        = form.cleaned_data['cedula']
            reservar      = Reserva.objects.filter(cedula = cedula)
            listaReservas = []

            listaReservas = sorted(
                list(reservar),
                key = lambda r: r.inicioReserva
            )
            
            if not reservar:
                msg = "Datos Inválidos";
                return render(
                    request,
                    'consultar-reservas.html',
                    { "form" : form , "msg": msg,'color' : 'red'}
                )
            else:
                return render(
                    request,
                    'consultar-reservas.html',
                    { "listaReservas" : listaReservas
                    , "form"          : form
                    }
                )

    return render(
        request,
        'consultar-reservas.html',
        { "form" : form }
    )

def billetera_recargar(request):
    if request.method == 'GET':
        form = RecargaForm()
    elif request.method == 'POST':
        form = RecargaForm(request.POST)
        if form.is_valid():
            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']
            monto = form.cleaned_data['monto']
            # try:
            #     billetera = Billetera.objects.get(id = billetera_id)
            # except ObjectDoesNotExist:
            #     return render(
            #         request,
            #         'autenticacion_denegada.html',
            #         )
            check = recargar_saldo(billetera_id,pin,monto)
            print(check)
            print(monto)
            print(monto=="0")
            
            if check or (monto=="0") or (monto=="0.0") or (monto=="0.00") :
                billetera = Billetera.objects.get(id = billetera_id)
                usuario = billetera.usuario
                #nombre = usuario.nombre
                #apellido = usuario.apellido
                #cedula = usuario.cedula
                recarga = Recarga(
                          nombre= form.cleaned_data['nombre'],
                          apellido = form.cleaned_data['apellido'],
                          cedula = form.cleaned_data['cedula'],
                          saldo = monto,
                          fechaTransaccion = datetime.now(),
                          numtarjeta = form.cleaned_data['tarjeta'][12:16],
                          tarjetaTipo = form.cleaned_data['tarjetaTipo'],
                          billetera = billetera
                          )
                recarga.save()
                espacio = " "
                if (monto=="0") or (monto=="0.0") or (monto=="0.00") :
                    return render(
                        request,
                        'error_monto_cero.html')
                if check == True:
                    return render(
                        request,
                        'error_recarga_maxima.html')    
                recarga.save()
                return render(
                    request,
                    'billetera_recargada.html',

                    {"form"          : form,
                     "nombre"        : recarga.nombre,
                     "apellido"      : recarga.apellido,
                     "cedula"        : recarga.cedula,
                     "fecha"         : recarga.fechaTransaccion,
                     "monto"         : recarga.saldo,
                     "espacio"       : espacio
                    }

                )
            elif not(check):
                return render(
                    request,
                    'autenticacion_denegada.html',
                    )
        else:
            error = "There was an error!"
    return render(
        request,
        'billetera_recargar.html',
        { "form" : form }

    )

def billetera_consumir(request,_id,_monto):
    form = ConsumirForm()
    
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404
    
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # No esta permitido acceder a esta vista aun
    
    if request.method == 'POST':
        form = ConsumirForm(request.POST)
        if form.is_valid():
            
            inicioReserva = datetime(
                year   = request.session['anioinicial'],
                month  = request.session['mesinicial'],
                day    = request.session['diainicial'],
                hour   = request.session['inicioReservaHora'],
                minute = request.session['inicioReservaMinuto']
            )

            finalReserva  = datetime(
                year   = request.session['aniofinal'],
                month  = request.session['mesfinal'],
                day    = request.session['diafinal'],
                hour   = request.session['finalReservaHora'],
                minute = request.session['finalReservaMinuto']
            )

            monto = Decimal(request.session['monto'])

            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']

            check = consumir_saldo(billetera_id,pin,monto)
            if check == True:
                 bille = Billetera.objects.get(id = form.cleaned_data['billetera_id'])
                 usuario = bille.usuario
                 reservaFinal = Reserva(
                    nombre = request.session['nombre'],
                    apellido = request.session['apellido'],
                    cedula = request.session['cedula'],
                    estacionamiento = estacionamiento,
                    inicioReserva   = inicioReserva,
                    finalReserva    = finalReserva
                 )
                 # Se guarda la reserva en la base de datos
                 reservaFinal.save()

                 # Se crea el objeto pago.
                 pago = Pago(
                   fechaTransaccion = datetime.now(),
                   cedula           = bille.usuario.cedula,
                   monto            = monto,
                   reserva          = reservaFinal,
                 )
                 #Se guarda el recibo de pago en la base de datos
                 pago.save()
                 #Se realiza el consumo de la billetera.

                 bille = Billetera.objects.get(id = form.cleaned_data['billetera_id'])
                 montoo = round(monto,2)
                 consumo = Consumo(saldo = montoo,
                          fechaTransaccion = datetime.now(),
                          billetera = bille,
                          establecimiento = estacionamiento,
                          reserva = reservaFinal,
                          flag = 1
                          )

                 if (float(bille.saldo) == 0.00):
                    mensaje2 = "Su billetera se quedo sin fondos."
                    mensaje3 = "Se recomienda recargar la billetera."
                 else:
                    mensaje3 = ""
                    mensaje2 = ""
                    consumo.save()
                 return render(
                    request,
                    'pago_billetera.html',
                    {  'id' : _id
                    ,  'pago' : pago
                    , "color"   : "green"
                    , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
               		, 'mensaje2' : mensaje2
               		, 'mensaje3' : mensaje3
                    }
                 )
            elif check==False:
                msg="Autenticacion denegada"
                return render(
                    request,
                        'denegado_pago_billetera.html',
                        {  'msg' : msg,
                            "color": "red" }
                )
            else:
                msg="Saldo Insuficiente."
                msg2="Se recomienda recargar."
                return render(
                    request,
                        'denegado_pago_billetera.html',
                        {  'msg' : msg,
                           'msg2' : msg2,
                            "color": "red" }
                )

    return render(
        request,
    	'pago_billetera.html',
        { 'form' : form, "monto": _monto }
    )

def billetera_saldo(request):
    if request.method == 'GET':
        form = SaldoForm()
    if request.method == 'POST':
        print("entre aca")
        form = SaldoForm(request.POST)
        
        if form.is_valid():
            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']
            check = mostrar_saldo(billetera_id,pin)
            try:
                billetera_electronica = Billetera.objects.get(id =billetera_id)
            except ObjectDoesNotExist:
                return render(
                    request,
                    'autenticacion_denegada_mostrarsaldo.html'
                    )
            billetera = Billetera.objects.get(id = billetera_id)
            
            saldo = format(float(billetera.saldo), '.2f')

            if check:
                if saldo==format(float(0.00), '.2f'):
                    mensaje = "Su saldo actual es : "
                    return render(
                    request,
                    'mostrar-saldo-cero.html',
                    {
                        "mensaje" : mensaje,
                        "saldo"   : saldo
                    }
                )
           
                else:
                    mensaje = "Su saldo actual es : "

                    return render(
                        request,
                        'mostrar-saldo.html',
                        {
                            "mensaje" : mensaje,
                            "saldo"   : saldo
                        }
                    )
            else:
                return render(
                    request,
                    'datos_invalidos.html',
                    {'color'   : 'red'
                    , 'mensaje' : 'Autenticacion Denegada'
                    }
                )


    return render(
        request,
        'billetera_saldo.html',
        { "form" : form }
    )

def billetera_movimientos(request):
    form = MovimientosForm()
    if request.method == 'POST':
        form = MovimientosForm(request.POST)
        if form.is_valid():
            billetera_id = form.cleaned_data['billetera_id'] 
            pin = form.cleaned_data['pin']
            check_recargas = obtener_recargas(billetera_id,pin)
            check_consumos = obtener_consumos(billetera_id,pin)
            check_reembolsos = obtener_reembolsos(billetera_id,pin)
            recargas = obtener_recargas(billetera_id,pin)
            consumos = obtener_consumos(billetera_id,pin)
            reembolsos = obtener_reembolsos(billetera_id,pin)
            lista_final = []
            if recargas:
                lista_final = lista_final + list(recargas)
            if consumos:
                lista_final = lista_final + list(consumos)
            if reembolsos:
                lista_final = lista_final + list(reembolsos)

            listaTotal = sorted(lista_final,
                key = lambda r: r.fechaTransaccion
            )

            if (check_consumos==False) and (check_recargas==False):
                return render(
                    request,
                    'datos_invalidos.html',
                    {'color'   : 'red'
                    , 'mensaje' : 'autenticación Denegada'
                    }
                )
            else:
                billetera = Billetera.objects.get(id=billetera_id)
                usuario = billetera.usuario
                pago = Pago
                return render(
                    request,
                    'billetera_mostrar_movimientos.html',
                    { "recargas"   : check_recargas,
                      "consumos"   : check_consumos,
                      "reembolsos" : reembolsos,
                      "billetera"  : billetera,
                      "usuario"    : usuario,
                      "listaTotal" : listaTotal,
                      "form"       : form,

                    }
                )
    return render(
        request,
        'billetera_movimientos.html',
        {"form" : form
        }
    )



def estacionamiento_ingreso(request):
    form = RifForm()
    if request.method == 'POST':
        form = RifForm(request.POST)
        if form.is_valid():

            rif = form.cleaned_data['rif']
            listaIngresos, ingresoTotal = consultar_ingresos(rif)

            return render(
                request,
                'consultar-ingreso.html',
                { "ingresoTotal"  : ingresoTotal
                , "listaIngresos" : listaIngresos
                , "form"          : form
                }
            )

    return render(
        request,
        'consultar-ingreso.html',
        { "form" : form }
    )


def receive_sms(request):
    ip = get_client_ip(request) # Busca el IP del telefono donde esta montado el SMS Gateway
    port = '8000' # Puerto del telefono donde esta montado el SMS Gateway
    phone = request.GET.get('phone', False)
    sms = request.GET.get('text', False)
    if (not sms or not phone):
        return HttpResponse(status=400) # Bad request
    
    phone = urllib.parse.quote(str(phone)) # Codificacion porcentaje del numero de telefono recibido
    
    # Tratamiento del texto recibido
    try:
        sms = sms.split(' ')
        id_sms = int(sms[0])
        inicio_reserva = sms[1] + ' ' + sms[2]
        final_reserva = sms[3] + ' ' + sms[4]
        inicio_reserva = parse_datetime(inicio_reserva)
        final_reserva = parse_datetime(final_reserva)
    except:
        return HttpResponse(status=400) # Bad request
    
    # Validacion del id de estacionamiento recibido por SMS
    try:
        estacionamiento = Estacionamiento.objects.get(id = id_sms)
    except ObjectDoesNotExist:
        text = 'No existe el estacionamiento ' + str(id_sms) + '.'
        text = urllib.parse.quote(str(text))
        urllib.request.urlopen('http://{0}:{1}/sendsms?phone={2}&text={3}&password='.format(ip, port, phone, text))
        return HttpResponse('No existe el estacionamiento ' + str(id_sms) + '.')
    
    # Validacion de las dos fechas recibidas por SMS
    m_validado = validarHorarioReserva(
        inicio_reserva,
        final_reserva,
        estacionamiento.apertura,
        estacionamiento.cierre,
        estacionamiento.horizontedias,
        estacionamiento.horizontehoras
    )
    if m_validado[0]:
        '''reserva_sms = Reserva(
            estacionamiento = estacionamiento,
            inicioReserva   = inicio_reserva,
            finalReserva    = final_reserva,
        )
        reserva_sms.save()'''
        text = 'Se realizó la reserva satisfactoriamente.'
        text = urllib.parse.quote(str(text))
        urllib.request.urlopen('http://{0}:{1}/sendsms?phone={2}&text={3}&password='.format(ip, port, phone, text))
    else:
        text = m_validado[1]
        text = urllib.parse.quote(str(text))
        urllib.request.urlopen('http://{0}:{1}/sendsms?phone={2}&text={3}&password='.format(ip, port, phone, text))
        return HttpResponse(m_validado[1])
    
    return HttpResponse('')
    
def tasa_de_reservacion(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404
    if (estacionamiento.apertura is None):
        return render(
            request, 'template-mensaje.html',
            { 'color'   : 'red'
            , 'mensaje' : 'Se debe parametrizar el estacionamiento primero.'
            }
        )
    ocupacion = tasa_reservaciones(_id)
    calcular_porcentaje_de_tasa(estacionamiento.apertura, estacionamiento.cierre, estacionamiento.capacidad, ocupacion)
    datos_ocupacion = urlencode(ocupacion) # Se convierten los datos del diccionario en el formato key1=value1&key2=value2&...
    return render(
        request,
        'tasa-reservacion.html',
        { "ocupacion" : ocupacion
        , "datos_ocupacion": datos_ocupacion
        }
    )

def editar_dueno(request, _id):
    _id = int(_id)
    msg = ""
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404

    if request.method == 'GET':
            form = CedulaForm()

    elif request.method == 'POST':
        # Leemos el formulario
        try: 
            form = CedulaForm(request.POST)        
            # Si el formulario
            if form.is_valid():
                nuevo_propietario = Propietario.objects.get(cedula = form.cleaned_data['cedula'])
                estacionamiento.propietario = nuevo_propietario
                estacionamiento.save()
                msg = "¡Cambiado dueño con Éxito!"
                return render(
                    request,
                    'editar_dueno.html',
                    { 'form': form
                    , 'estacionamiento': estacionamiento, 
                    'msg': msg
                    , 'color' : 'black'
                    }
                )
        except ObjectDoesNotExist:
            form = CedulaForm()
            msg = "Propietario no existe"

            return render(
                request,
                'editar_dueno_noexiste.html',
                { 'form': form
                , 'estacionamiento': estacionamiento
                }
            )
    return render(
                request,
                'editar_dueno.html',
                { 'form': form
                , 'color' : 'red'
                , 'estacionamiento': estacionamiento, 'msg': msg,
                }
            )
def grafica_tasa_de_reservacion(request):
    
    # Recuperacion del diccionario para crear el grafico
    try:
        datos_ocupacion = request.GET.dict()
        datos_ocupacion = OrderedDict(sorted((k, float(v)) for k, v in datos_ocupacion.items()))     
        response = HttpResponse(content_type='image/png')
    except:
        return HttpResponse(status=400) # Bad request
    
    # Si el request no viene con algun diccionario
    if (not datos_ocupacion):
        return HttpResponse(status=400) # Bad request
    
    # Configuracion y creacion del grafico de barras con la biblioteca pyplot
    pyplot.switch_backend('Agg') # Para que no use Tk y aparezcan problemas con hilos
    pyplot.bar(range(len(datos_ocupacion)), datos_ocupacion.values(), hold = False, color = '#6495ed')
    pyplot.ylim([0,100])
    pyplot.title('Distribución de los porcentajes por fecha')
    pyplot.xticks(range(len(datos_ocupacion)), list(datos_ocupacion.keys()), rotation=20)
    pyplot.ylabel('Porcentaje (%)')
    pyplot.grid(True, 'major', 'both')
    pyplot.savefig(response, format='png') # Guarda la imagen creada en el HttpResponse creado
    pyplot.close()
    
    return response

def menu_billetera(request):
    if request.method == 'GET':
        return render(
         request,
         'menu_billetera.html'
     )
    return render(
         request,
         'menu_billetera.html'
     )


def crear_billetera(request):

     #usuarios = Usuario.objects.all()

    if request.method == 'GET':
        form = CrearBilleteraForm()

     # Si es POST, se verifica la información recibida
    elif request.method == 'POST':

         # Creamos un formulario con los datos que recibimos
        form = CrearBilleteraForm(request.POST)

         # Si el formulario es valido, entonces creamos un objeto con
         # el constructor del modelo
        if form.is_valid():
            obj = Usuario(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                cedula = form.cleaned_data['cedula'],
            )

            obj.save()

            obj2 = Billetera(
                usuario = obj,
                saldo = float(0.00),
                pin = form.cleaned_data['pin']
            )

            obj2.save()
            id_billetera = obj2.id
            mensaje = 'El id correspondiente a la billetera es : '

            return render(
                            request,
                            'creada-billetera.html',
                            { "form" : form,
                              "id_billetera" : id_billetera,
                              "mensaje" : mensaje  }
                        )

        else :
            error = "There was an error!"
            return render(
                            request,
                            'crear-billetera.html',
                            {"form" : form   }
                )


    return render(
         request,
         'crear-billetera.html',
         { "form" : form }
     )

def menu_propietario(request):

    return render(
         request,
         'menu_propietario.html'
    )

def crear_propietario(request):
    error = ""
    # Si es un GET, mandamos un formulario vacio
    if request.method == 'GET':
        form = PropietarioForm()

	# Si es POST, se verifica la información recibida
    elif request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            # Creamos un formulario con los datos que recibimos
            try:
                cedula = form.cleaned_data['cedula']
                propietario = Propietario.objects.get(cedula = cedula)
                error = "Usuario ya existe"
                return render(request,
                    'crear_propietario.html',
                     { "form" : form , "error":error}
                )
                
            except ObjectDoesNotExist:
                # Si el formulario es válido, entonces creamos un objeto con
                # el constructor del modelo
                if form.is_valid():
                    obj = Propietario(
                        nombre   = form.cleaned_data['nombre'],
                        apellido = form.cleaned_data['apellido'],
                        cedula   = form.cleaned_data['cedula'],
                        telefono = form.cleaned_data['telefono'],
                        email    = form.cleaned_data['email'],
                    )

                    obj.save()

                    return render(
                        request,
                        'propietario_creado.html',
                        { "form" : form }
                    )
        # Si el formulario no está completo resalta los campos obligatorios.
        else:
            error = "There was an error!"

    return render(
        request,
        'crear_propietario.html',
        { "form" : form , "error":error}
    )

# Verifica si el propietario a modificar existe.
def  modificar_propietario(request):

    # Si es un GET, mandamos un formulario vacio
    if request.method == 'GET':
        form = ModificarPropietarioForm()

    # Si es POST, se verifica la información recibida
    elif request.method == 'POST':

        # Creamos un formulario con los datos que recibimos
        form = ModificarPropietarioForm(request.POST)

        # Si el formulario es válido, entonces verifica si el propietario
        # existe.
        if form.is_valid():

            cedula = form.cleaned_data['cedula']          
            try:
                obj = Propietario.objects.get(cedula = cedula)
                form_data = {
                    'nombre'   : obj.nombre,
                    'apellido' : obj.apellido,
                    'cedula'   : obj.cedula,
                    'telefono' : obj.telefono,
                    'email'    : obj.email
                }

                form = PropietarioForm(data = form_data)
                return render(
                    request,
                    'modificar_propietario_bloq.html',
                    { "form" : form }
                )

            except ObjectDoesNotExist:
                
                form = ModificarPropietarioForm()
                return render(
                request,
                'modificar_propietario.html',
                { "form" : form }
            )

        # Si el formulario no está completo resalta los campos obligatorios.
        else:
            error = "There was an error!"

    return render(
        request,
        'modificar_propietario.html',
        { "form" : form }
    )

def buscar_propietario(request):
    estacionamientos = Estacionamiento.objects.all()
    form = PropietarioForm(request.POST)
    if(form.is_valid()):
        cedula = form.cleaned_data['cedula']
        obj = Propietario.objects.get(cedula = cedula)
        obj.nombre = form.cleaned_data['nombre']
        obj.apellido = form.cleaned_data['apellido']
        obj.telefono = form.cleaned_data['telefono']
        obj.email = form.cleaned_data['email']
        obj.save()
    return redirect('estacionamientos_all')


def confirmar_cancelacion(request):
    
    try:
       
            billetera_id = request.session['billetera_id'] 
            numero_pago = request.session['numero_pago']
            
            pago = Pago.objects.get(id=numero_pago)
            billetera   = Billetera.objects.get(id=billetera_id)
            cancelacion = crear_cancelacion(billetera_id,numero_pago)

            if (cancelacion[0] == False) :
                print(cancelacion[1])          
                
            return render(
                request,
                'confirmar_cancelacion.html',
                { 'color'  :'green',
                'mensaje': 'Cancelacion realizada con Exito',
                'exito':'exito',
                "pago" : pago,
                "recarga" : pago.monto -  cancelacion[1].multa,
                "cancelacion": cancelacion[1],
                "billetera" : billetera,
                }
            )
    except: 
        form = CancelarReservaForm()
        return render(
            request,
            'cancelar_reserva.html',
            {"form" : form }
        )        
   


def cancelar_reserva(request):
    
    form = CancelarReservaForm()
    
    if request.method == 'POST':
        form = CancelarReservaForm(request.POST)
        
        if form.is_valid():
               
            numero_pago = form.cleaned_data['numero_pago']
            cedula = form.cleaned_data['cedula']
            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']   
                 
            check = cancelacion(cedula,pin,billetera_id,numero_pago)  
           
            if check[0]:
                
                billetera = Billetera.objects.get(id=billetera_id)
                pago = Pago.objects.get(id=numero_pago)

               
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
                    
                request.session['billetera_id']    = billetera_id
                request.session['numero_pago']  = numero_pago 
                                                           
                return render(
                        request,
                        'confirmar_cancelacion.html',
                        {  "pago" : pago,
                           "mensaje":"Datos de la Cancelacion",
                           "color" : "black",
                           "costo" : multa,
                           "recarga" : pago.monto - multa,
                           "billetera" : billetera,
                        }
                    )
            else:
                return render(
                    request,
                    'cancelacion_mensaje.html',
                    { 'color'  :'red'
                    , 'mensaje': check[1]
                    }
                )
         
    return render(
        request,
        'cancelar_reserva.html',
        { "form" : form }
    )

# Chequea principalmente que la cedula corresponda con el id
# de reserva
def mover_reserva(request):
    form = ReservaCIForm()
    form2 = CambiarReservaForm()
    if request.method == 'POST':
        form = ReservaCIForm(request.POST)
        if form.is_valid():
            reserva_id = form.cleaned_data['reserva_id']
            request.session['pago_id'] = reserva_id
            cedula = form.cleaned_data['cedula']
            # hace el chequeo id-cedula
            check = chequear_mover_reserva(cedula,reserva_id)
            if check == False:
                return render(
                    request,
                    'reserva_no_existe.html'
                )
            elif check == True:
                # Necesitaremos el id de la reserva en otra vista
                request.session['pago_id'] = reserva_id
                return render(
                    request,
                    'cambiar_datos_reserva.html',
                    {'form' : form2
                    }
                )
            
    return render(
        request,
        'reserva_cedula.html',
        {'form' : form
        }
    )

# Aqui se cambian los datos de la reserva
def cambiar_datos_reserva(request):
    pago_id = request.session['pago_id']
    form = CambiarReservaForm()
    print("GET")
    if request.method == 'POST':
        print("POST")
        form = CambiarReservaForm(request.POST)
        # Verificamos si es valido con los validadores del formulario
        if form.is_valid():

            inicioReserva = form.cleaned_data['inicio']
            finalReserva = form.cleaned_data['final']

            pago = Pago.objects.get(id = pago_id)
            reserva = pago.reserva
            #reserva = Reserva.objects.get(id = reserva_id)
            estacionamiento = reserva.estacionamiento

            #Obtenemos el pago correspondiente a la reserva
            #pago = Pago.objects.get(reserva = reserva)
            monto_viejo = pago.monto
            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(
                inicioReserva,
                finalReserva,
                estacionamiento.apertura,
                estacionamiento.cierre,
                estacionamiento.horizontedias,
                estacionamiento.horizontehoras
            )

            #print (datetime.now()+
            #        timedelta(
            #                days=int(estacionamiento.horizontedias),
            #                hours=int(estacionamiento.horizontehoras))-
            #        inicioReserva)
            #print (finalReserva-
            #        datetime.now()-
            #                timedelta(days=int(estacionamiento.horizontedias),
            #                  hours=int(estacionamiento.horizontehoras)))
            #print (datetime.now()+
            #        timedelta(
            #                days=int(estacionamiento.horizontedias),
            #                hours=int(estacionamiento.horizontehoras))-
            #        inicioReserva>
            #        finalReserva-
            #        datetime.now()-
            #                timedelta(days=int(estacionamiento.horizontedias),
            #                  hours=int(estacionamiento.horizontehoras)))

            # Si no es valido devolvemos el request
            if not m_validado[0]:
                if(datetime.now()+
                    timedelta(
                            days=int(estacionamiento.horizontedias),
                            hours=int(estacionamiento.horizontehoras))-
                    inicioReserva>
                    finalReserva-
                    datetime.now()-
                            timedelta(days=int(estacionamiento.horizontedias),
                              hours=int(estacionamiento.horizontehoras))):
                    pass
                else:
                    return render(
                        request,
                        'template-mensaje.html',
                        { 'color'  :'red'
                        , 'mensaje': m_validado[1]
                        }
                    )
            # verificamos que hay puesto disponible
            if marzullo(estacionamiento.id, inicioReserva, finalReserva):
                #cambiamos los datos de la reserva
                reserva.inicioReserva = inicioReserva
                reserva.finalReserva  = finalReserva
                reserva.save()

                monto = Decimal(
                    estacionamiento.tarifa.calcularPrecio(
                        inicioReserva,finalReserva
                    )
                )
                # calculamos el nuevo monto de la reserva
                monto_total = nuevo_monto_reserva(monto_viejo,monto)

                request.session['monto'] = float(
                    estacionamiento.tarifa.calcularPrecio(
                        inicioReserva,
                        finalReserva
                    )
                )
                # Si el monto anterior es mayor, hay que proceder
                # a reembolsar

                request.session['reembolso'] = float(monto_total[1])
                request.session['monto_diferencia'] = float(monto_total[1])
                request.session['estacionamiento_id'] = estacionamiento.id
                
                if monto_total[0] == True:
                    return render(
                                request,
                                'confirmar_mover_reserva_reembolso.html',
                                { 'id'      : estacionamiento.id
                                , 'monto'   : monto_total[1]
                                , 'reserva' : reserva
                                , 'color'   : 'green'
                                , 'mensaje' : 'Existe un puesto disponible'
                                }
                            )
                # Si el monto nuevo es mayor, hay que proceder
                # a pagar la diferencia
                elif monto_total[0] == False:
                    return render(
                        request,
                        'confirmar_mover_reserva_pagar.html',
                            { 'id'      : estacionamiento.id
                            , 'monto'   : monto_total[1]
                            , 'reserva' : reserva
                            , 'color'   : 'green'
                            , 'mensaje' : 'Existe un puesto disponible'
                            }
                       )
                # El monto nuevo es igual al monto anterior, no hay que pagar
                # ni reembolsar
                elif monto_total[0] == -1:
                    return render(
                        request,
                        'confirmar_mover_reserva.html',
                            { 'id'      : estacionamiento.id
                            , 'monto'   : monto_total[1]
                            , 'reserva' : reserva
                            , 'color'   : 'green'
                            , 'mensaje' : 'Existe un puesto disponible'
                            }
                       )
            else:
                
                return render(
                    request,
                    'template-mensaje.html',
                    {'color'   : 'red'
                    , 'mensaje' : 'No hay un puesto disponible para ese horario'
                    }
                )

                       
    return render(
        request,
        'cambiar_datos_reserva.html',
        {'form' : form
        }
    )

# Este es el metodo para el pago de la diferencia con la tarjeta
def pagar_tarjeta_mover_reserva(request):
    form = PagoForm()
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            cedula = form.cleaned_data['cedula']
            tarjetaTipo = form.cleaned_data['tarjetaTipo']
            tarjeta = form.cleaned_data['tarjeta']

            pago_id = request.session['pago_id']
            monto = request.session['monto_diferencia']
            estacionamiento_id = request.session['estacionamiento_id']
            
            _pago = Pago.objects.get(id = pago_id)
            reserva = _pago.reserva
            #reserva = Reserva.objects.get(id = reserva_id)
            
            # Hay que generar el recibo de pago
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = cedula,
                monto            = monto,
                tarjetaTipo      = form.cleaned_data['tarjetaTipo'],
                reserva          = reserva,
            )

            # Se guarda el recibo de pago en la base de datos
            pago.save()

            reserva.movidas+= 1
            reserva.save()

            # Chequeamos si el usuario pago con billetera la reserva
            check = chequear_consumo_billetera(_pago,reserva)
            # Si el usuario no pago con billetera, paga por el servicio
            if check == False:
                return render(
                request,
                'pago_reserva_exitoso_tarjeta.html',
                { "id"      : estacionamiento_id
                , "pago"    : pago
                , "color"   : "green"
                , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                }
    )
            # Si el usuario pago con billetera, no paga por el servicio
            else:
                return render(
                request,
                'pago_reserva_exitoso_tarjeta2.html',
                { "id"      : estacionamiento_id
                , "pago"    : pago
                , "color"   : "green"
                , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                }
            )

            return render(
                        request,
                        'pago.html',
                        { "id"      : estacionamiento_id
                        , "pago"    : pago
                        , "color"   : "green"
                        , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                        }
                    )

    return render(
        request,
        'pago.html',
        { 'form' : form }
    )

# Este es el metodo para el pago de la diferencia con la billetera
def pagar_billetera_mover_reserva(request):
    monto = request.session['monto_diferencia']
    pago_id = request.session['pago_id']
    estacionamiento_id = request.session['estacionamiento_id']
    estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
    form = ConsumirForm()
    if request.method == 'POST':
        form = ConsumirForm(request.POST)
        if form.is_valid():
            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']
            # Hay que consumir el dinero de la billetera
            consumir = consumir_saldo(billetera_id,pin,monto)
            if consumir == False:
                return render(
                    request,
                    'datos_invalidos_billetera_mover_reserva.html'
                )
            elif consumir == True:
                billetera = Billetera.objects.get(id = billetera_id)
                _pago = Pago.objects.get(id = pago_id)
                reserva = _pago.reserva
                #reserva = Reserva.objects.get(id=reserva_id)
                pago = Pago(
                   fechaTransaccion = datetime.now(),
                   cedula           = billetera.usuario.cedula,
                   monto            = monto,
                   reserva          = reserva,
                 )
                pago.save()

                consumo = Consumo (saldo = monto,
                                   fechaTransaccion = datetime.now(),
                                   billetera = billetera,
                                   establecimiento = estacionamiento,
                                   reserva = reserva
                                   )
                consumo.save()

                reserva.movidas+= 1
                reserva.save()

                # Chequeamos si el usuario pago con billetera la reserva
                check = chequear_consumo_billetera(_pago,reserva)
                # Si el usuario no pago con billetera, paga por el servicio
                if check == False:
                    return render(
                    request,
                    'pago_reserva_exitoso_billetera.html',
                    {  'id' : estacionamiento_id
                    ,  'pago' : pago
                    , "color"   : "green"
                    , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                    , 'mensaje2' : " "
                    , 'mensaje3' : " "
                    }
                )
                # Si el usuario pago con billetera, no paga por el servicio
                else:
                    return render(
                    request,
                    'pago_reserva_exitoso_billetera2.html',
                    {  'id' : estacionamiento_id
                    ,  'pago' : pago
                    , "color"   : "green"
                    , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                    , 'mensaje2' : " "
                    , 'mensaje3' : " "
                    }
                )

            else:
                return render(
                    request,
                    'monto_exceso_pago.html',
                )

    return render(
        request,
        'pago_billetera.html',
        {'form' : form,
        'monto' : monto
        }
    )

# Este es el metodo para el reembolso
def reembolsar_reserva(request):
    estacionamiento_id = request.session['estacionamiento_id']
    pago_id = request.session['pago_id']
    pago = Pago.objects.get(id = pago_id)
    reserva = pago.reserva
    estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
    # Reutilizamos el form de chequear movimientos de la billetera
    form = MovimientosForm()

    if request.method == 'POST':
        reembolso = request.session['reembolso'] 
        form = MovimientosForm(request.POST)
        if form.is_valid():
            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']
            # Se reembolsa el dinero a la billetera como una recarga
            recargar = recargar_saldo(billetera_id,pin,reembolso)

            if recargar == False:
                return render(
                    request,
                    'datos_invalidos_reembolso.html'
                    )
            elif recargar == True:
                return render(
                    request,
                    'saldo_exceso_reembolso.html'
                    )
            else:
                billetera = Billetera.objects.get(id = billetera_id)
                usuario = billetera.usuario
                _reembolso = Reembolso(nombre = usuario.nombre,
                                      apellido = usuario.apellido,
                                      cedula = usuario.cedula,
                                      estacionamiento = estacionamiento,
                                      inicioReserva = reserva.inicioReserva,
                                      finalReserva = reserva.finalReserva,
                                      saldo = reembolso,
                                      fechaTransaccion_vieja = pago.fechaTransaccion,
                                      fechaTransaccion = datetime.now(),
                                      billetera = billetera,
                                      id_viejo = pago.id,
                                      monto_reserva = pago.monto,
                                      mensaje = "Reembolso reserva"
                                      )
                _reembolso.save()

                reserva.movidas+= 1
                reserva.save()

                # Chequeamos si el usuario pago con billetera la reserva
                check = chequear_consumo_billetera(pago,reserva)
                # Si el usuario no pago con billetera, paga por el servicio
                if check == False:
                    return render(
                        request,
                        'mover_reserva_exitosa_reembolso.html',
                        {'nombre': billetera.usuario.nombre,
                         'apellido': billetera.usuario.apellido,
                         'cedula'  : billetera.usuario.cedula,
                         'fecha'   : datetime.now(),
                         'monto'   : reembolso
                        }
                    )
                # Si el usuario pago con billetera, no paga por el servicio
                else:
                    return render(
                        request,
                        'mover_reserva_exitosa_reembolso2.html',
                        {'nombre': billetera.usuario.nombre,
                         'apellido': billetera.usuario.apellido,
                         'cedula'  : billetera.usuario.cedula,
                         'fecha'   : datetime.now(),
                         'monto'   : reembolso
                        }
                    )


    return render(
        request,
        'reembolsar_reserva.html',
        {'form': form
        }
    )

# Simplementa se muestra el mensaje que se movio la reserva exitosamente
def mover_reserva_exitosa(request):
    return render(
        request,
        'mover_reserva_exitosa_reembolso.html'
    )

def pagar_servicio_mover_reserva(request):
    return render(
        request,
        'seleccionar_pago_servicio.html'
    )

def pagar_servicio_tarjeta(request):
    form = PagoForm()
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            cedula = form.cleaned_data['cedula']
            tarjetaTipo = form.cleaned_data['tarjetaTipo']
            tarjeta = form.cleaned_data['tarjeta']

            pago_id = request.session['pago_id']
            monto = request.session['monto_diferencia']
            estacionamiento_id = request.session['estacionamiento_id']
            
            # De acuerdo a la tarifa establecida
            multa=0
            try:
                sage = Sage.objects.all() 
                for elemento in sage:
                    multa = elemento.deduccion 

            except ObjectDoesNotExist:  
                multa = 0   
            _monto = Decimal(multa)*Decimal(monto)

            # Hay que generar el recibo de pago
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = cedula,
                monto            = _monto,
                tarjetaTipo      = form.cleaned_data['tarjetaTipo'],
            )

            # Se guarda el recibo de pago en la base de datos
            pago.save()
            
            return render(
                        request,
                        'pago_servicio_tarjeta.html',
                        { "id"      : estacionamiento_id
                        , "pago"    : pago
                        ,"monto"    : _monto
                        , "color"   : "green"
                        , 'mensaje' : "Se realizo el pago de servicio satisfactoriamente."
                        }
                    )

    return render(
        request,
        'pago_servicio_tarjeta.html',
        { 'form' : form }
    )

def pagar_servicio_billetera(request):
    form = ConsumirForm()
    monto = request.session['monto_diferencia']
    estacionamiento_id = request.session['estacionamiento_id']
    estacionamiento = Estacionamiento.objects.get(id = estacionamiento_id)

    # De acuerdo a la tarifa establecida
    multa=0
    try:
        sage = Sage.objects.all() 
        for elemento in sage:
            multa = elemento.deduccion 

    except ObjectDoesNotExist:  
        multa = 0   
    _monto = multa*monto

    if request.method == 'POST':
        form = ConsumirForm(request.POST)
        if form.is_valid():

            billetera_id = form.cleaned_data['billetera_id']
            pin = form.cleaned_data['pin']

            check = consumir_saldo(billetera_id,pin,_monto)
            if check == True:
                 bille = Billetera.objects.get(id = form.cleaned_data['billetera_id'])
                 usuario = bille.usuario
                 
                 # Se crea el objeto pago.
                 pago = Pago(
                   fechaTransaccion = datetime.now(),
                   cedula           = bille.usuario.cedula,
                   monto            = _monto,
                 )

                 #Se realiza el consumo de la billetera.
                 bille = Billetera.objects.get(id = form.cleaned_data['billetera_id'])
                 montoo = round(_monto,2)
                 consumo = Consumo(saldo = montoo,
                          fechaTransaccion = datetime.now(),
                          billetera = bille,
                          establecimiento = estacionamiento
                          )

                 if (float(bille.saldo) == 0.00):
                    mensaje2 = "Su billetera se quedo sin fondos."
                    mensaje3 = "Se recomienda recargar la billetera."
                 else:
                    mensaje3 = ""
                    mensaje2 = ""
                    pago.save()
                    consumo.save()
                 return render(
                    request,
                    'pago_servicio_billetera.html',
                    {  'id' : estacionamiento_id
                    , 'monto' : montoo
                    ,  'pago' : pago
                    , "color"   : "green"
                    , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                    , 'mensaje2' : mensaje2
                    , 'mensaje3' : mensaje3
                    }
                 )
            elif check==False:
                msg="Autenticacion denegada"
                return render(
                    request,
                        'denegado_pago_billetera.html',
                        {  'msg' : msg,
                            "color": "red" }
                )
            else:
                msg="Saldo Insuficiente."
                msg2="Se recomienda recargar."
                return render(
                    request,
                        'denegado_pago_billetera.html',
                        {  'msg' : msg,
                           'msg2' : msg2,
                            "color": "red" }
                )


    return render(
        request,
        'pago_servicio_billetera.html',
        { 'form' : form, 
          'monto': _monto 
        }
    )

def configuracion(request):

    form = SageForm()

    if request.method == 'POST':

        form = SageForm(request.POST)
        
        if form.is_valid():

            deduccion = form.cleaned_data['porcentaje']
            exito = guardar_configuracion(deduccion)

            if (exito[0] == True):

                sage = Sage.objects.all() 
                for elemento in sage:
                    multa = elemento.deduccion
                
                return render(
                        request,
                        'configuracion.html',
                        { 'color'  :'green'
                        , 'mensaje': exito[1]
                        , 'monto' : multa * 100
                        }
                    ) 
            else:
                form2 = SageForm()
                return render(
                        request,
                        'configuracion.html',
                        { 'color'  :'red'
                        , 'mensaje': exito[1]
                       
                        }
                    ) 

    return render(
        request,
        'configuracion.html',
        {"form" : form
        }
    )