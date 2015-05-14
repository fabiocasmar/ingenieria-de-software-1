# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import render_to_response
import urllib
from django.http import HttpResponse, Http404
from django.utils.dateparse import parse_datetime
from urllib.parse import urlencode
from matplotlib import pyplot
from decimal import Decimal
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
    UsuarioForm
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
    Consumo
)

from estacionamientos.models import Propietario, Usuario

# Usamos esta vista para procesar todos los estacionamientos
def estacionamientos_all(request):
    estacionamientos = Estacionamiento.objects.all()
    form1=-1
    form2=-1
    # Si es un GET, mandamos un formulario vacio
    if request.method == 'GET':
        form1 = CedulaForm()

    # Si es POST, se verifica la información recibida
    elif request.method == 'POST':
        # Creamos un formulario con los datos que recibimos
        form1 = CedulaForm(request.POST)

        # Parte de la entrega era limitar la cantidad maxima de
        # estacionamientos a 5
        if len(estacionamientos) >= 5:
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'No se pueden agregar más estacionamientos'
                }
            ) 

        # Si el formulario es valido, entonces creamos un objeto con
        # el constructor del modelo
        if form1.is_valid():
            try:
                obj = Propietario.objects.get(cedula = form1.cleaned_data['cedula'])
                form1 = EstacionamientoForm()
                form2 = PropietarioForm()
            except ObjectDoesNotExist:
                form1 = EstacionamientoForm()
                form2 = PropietarioForm()
            # Recargamos los estacionamientos ya que acabamos de agregar
            estacionamientos = Estacionamiento.objects.all()
    return render(
        request,
        'catalogo-estacionamientos.html',
        { 'form1': form1, 'form2': form2
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

            monto = Decimal(request.session['monto']).quantize(Decimal('1.00'))
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
            success = "Datos validos!"
            return render(
                request,
                'billetera_recargada.html',
                {"form"          : form
                }
            )
        else:
            error = "There was an error!"
    return render(
        request,
        'billetera_recargar.html',
        { "form" : form }

    )

def billetera_consumir(request):
    if request.method == 'GET':
        form = ConsumirForm()
    elif request.method == 'POST':
        form = ConsumirForm(request.POST)
        if form.is_valid():
            success = "Datos validos!"
            return render(
                request,
                'billetera_consumorealizado.html',
                {"form"          : form
                }
            )
    else:
        error = "There was an error!"
    return render(
        request,
        'billetera_consumir.html',
        { "form" : form }
    )

def billetera_saldo(request):
    if request.method == 'GET':
        form = SaldoForm()
    return render(
        request,
        'billetera_saldo.html',
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

def estacionamiento_usuario(request):

     #usuarios = Usuario.objects.all()

    if request.method == 'GET':
        form = UsuarioForm()

     # Si es POST, se verifica la información recibida
    elif request.method == 'POST':

         # Creamos un formulario con los datos que recibimos
         form = UsuarioForm(request.POST)

         # Si el formulario es valido, entonces creamos un objeto con
         # el constructor del modelo
         if form.is_valid():
             obj = Usuario(
                 nombre = form.cleaned_data['nombre'],
                 apellido = form.cleaned_data['apellido'],
                 cedula = form.cleaned_data['cedula'],
                 telefono = form.cleaned_data['telefono'],
                 email = form.cleaned_data['email']
             )

             obj.save()

             obj2 = Billetera(
                usuario = obj,
                saldo = 0,
                pin = form.cleaned_data['pin']
            )

             obj2.save()

         return render(
             request,
             'creado-usuario.html',
             { "form" : form  }
         )

    return render(
         request,
         'crear-usuario.html',
         { "form" : form }
     )

