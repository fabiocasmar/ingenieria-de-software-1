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
    datetime,
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
    consumir_saldo
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
    CancelarReservaForm
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
    CancelarReserva   
)

# Usamos esta vista para procesar todos los estacionamientos
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
                'esquema' : estacionamiento.tarifa.__class__.__name__
            }
            form = EstacionamientoExtendedForm(data = form_data)
        else:
            form = EstacionamientoExtendedForm()

    elif request.method == 'POST':
        # Leemos el formulario
        form = EstacionamientoExtendedForm(request.POST)
        # Si el formulario
        if form.is_valid():
            horaIn        = form.cleaned_data['horarioin']
            horaOut       = form.cleaned_data['horarioout']
            tarifa        = form.cleaned_data['tarifa']
            tipo          = form.cleaned_data['esquema']
            inicioTarifa2 = form.cleaned_data['inicioTarifa2']
            finTarifa2    = form.cleaned_data['finTarifa2']
            tarifa2       = form.cleaned_data['tarifa2']

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
            estacionamiento.tarifa    = esquemaTarifa
            estacionamiento.apertura  = horaIn
            estacionamiento.cierre    = horaOut
            estacionamiento.capacidad = form.cleaned_data['puestos']

            estacionamiento.save()
            form = EstacionamientoExtendedForm()

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

            inicioReserva = form.cleaned_data['inicio']
            finalReserva = form.cleaned_data['final']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(
                inicioReserva,
                finalReserva,
                estacionamiento.apertura,
                estacionamiento.cierre,
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
                estacionamiento = estacionamiento,
                inicioReserva   = inicioReserva,
                finalReserva    = finalReserva,
            )

            # Se guarda la reserva en la base de datos
            reservaFinal.save()

            monto = Decimal(request.session['monto']).quantize(Decimal(10) ** -2)
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = form.cleaned_data['cedula'],
                cedulaTipo       = form.cleaned_data['cedulaTipo'],
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
            facturas      = Pago.objects.filter(cedula = cedula)
            listaFacturas = []

            listaFacturas = sorted(
                list(facturas),
                key = lambda r: r.reserva.inicioReserva
            )
            return render(
                request,
                'consultar-reservas.html',
                { "listaFacturas" : listaFacturas
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
          
            if check:
                billetera = Billetera.objects.get(id = billetera_id)
                usuario = billetera.usuario
                nombre = usuario.nombre
                apellido = usuario.apellido
                cedula = usuario.cedula
                recarga = Recarga(saldo = monto,
                          fechaTransaccion = datetime.now(),
                          )
                espacio = " "
                return render(
                    request,
                    'billetera_recargada.html',

                    {"form"          : form,
                     "nombre"        : nombre,
                     "apellido"      : apellido,
                     "cedula"        : cedula,
                     "fecha"         : recarga.fechaTransaccion,
                     "monto"         : recarga.saldo,
                     "espacio"       : espacio
                    }

                )
            else:
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

                 reservaFinal = Reserva(
                    estacionamiento = estacionamiento,
                    inicioReserva   = inicioReserva,
                    finalReserva    = finalReserva,
                 )
                 # Se guarda la reserva en la base de datos
                 reservaFinal.save()

                 # Se crea el objeto pago.
                 pago = Pago(
                   fechaTransaccion = datetime.now(),
                   cedula           = bille.usuario.cedula[2:],
                   monto            = monto,
                   reserva          = reservaFinal,
                 )
                 #Se guarda el recibo de pago en la base de datos
                 pago.save()
                 #Se realiza el consumo de la billetera.
                 consumo = Consumo(saldo = monto,
                          fechaTransaccion = datetime.now(),
                          )
                 bille = Billetera.objects.get(id = form.cleaned_data['billetera_id'])
                 if (float(bille.saldo) == 0.00):
                    mensaje2 = "Su billetera se quedo sin fondos."
                    mensaje3 = "Se recomienda recargar la billetera."
                 else:
                    mensaje3 = ""
                    mensaje2 = ""
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
                    , 'mensaje' : 'Los datos ingresados son inválidos'
                    }
                )


    return render(
        request,
        'billetera_saldo.html',
        { "form" : form }
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


def cancelar_reserva(request):
    form = CancelarReservaForm()
    if request.method == 'POST':
        form = CancelarReservaForm(request.POST)
        
        if form.is_valid():
            try:        
                numero_pago = form.cleaned_data['numero_pago']
                cedula = form.cleaned_data['cedula']
                pago = Pago.objects.get(id = numero_pago)
                    
            except ObjectDoesNotExist:
                
                return render(
                    request,
                   'cancelacion_mensaje.html',
                    { 'color'  :'red'
                    , 'mensaje': 'Numero de confirmacion invalido'
                    }
                )              
                
            try:
                billetera_id = form.cleaned_data['billetera_id']  
                billetera = Billetera.objects.get(id = billetera_id)
            except ObjectDoesNotExist:
                
                return render(
                    request,
                    'cancelacion_mensaje.html',
                    { 'color'  :'red'
                    , 'mensaje': 'Datos invalidos de la billetera electronica'
                    }
                )
                
            if (pago.reserva.inicioReserva < datetime.now()):
                    return render(
                        request,
                        'cancelacion_mensaje.html',
                        { 'color'  :'red'
                         , 'mensaje': 'La fecha de reserva ya ocurrio, no es posible cancelarla'
                         }
                    )  
                       
            if (pago.cedula != cedula):
                    return render(
                        request,
                        'cancelacion_mensaje.html',
                        { 'color'  :'red'
                         , 'mensaje': 'Numero de cedula errada. Debe introducir el numero de cedula asociado a la factura de pago'
                         }
                    )          
               
            else:
                obj = CancelarReserva(
                        estacionamiento   = Estacionamiento.objects.get(id=pago.reserva.estacionamiento.id),
                        fechaTransaccion = datetime.now(),
                        billetera   = Billetera.objects.get(id=billetera_id),
                        inicioReserva = pago.reserva.inicioReserva,
                        finalReserva = pago.reserva.finalReserva,
                        cedula = pago.cedula     
                    )
                obj.save()
                
                reserva  = Reserva.objects.get(id=pago.reserva.id)
                reserva.delete()
                                               
                return render(
                    request,
                    'cancelar_reserva.html',
                    { 
                        "pago" : pago,
                        "billetera" : billetera,
                        "form" : form
                    }
                )
               
    return render(
        request,
        'cancelar_reserva.html',
        { "form" : form }
    )
    
    
