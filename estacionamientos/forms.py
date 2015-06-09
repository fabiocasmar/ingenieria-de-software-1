#-*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from django.forms.widgets import SplitDateTimeWidget

class CustomSplitDateTimeWidget(SplitDateTimeWidget):

    def format_output(self, rendered_widgets):
        return '<p></p>'.join(rendered_widgets)

class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
        regex   = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
        message = 'Debe introducir un formato válido de teléfono.'
    )
    
    name_validator = RegexValidator(
        regex   = '^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ\-\'0-9! ]+$',
        message = 'La entrada debe ser un nombre en Español sin símbolos especiales.'
    )
    
    rif_validator = RegexValidator(
        regex   = '^[JVD]-\d{8}-?\d$',
        message = 'Introduzca un RIF con un formato válido de la forma X-xxxxxxxxx.'
    )

    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'La cédula solo puede contener caracteres numéricos.'
    )

    propietario = forms.CharField(
        required   = True,
        label      = "Propietario",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula del Propietario'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

    nombre = forms.CharField(
        required = True,
        label    = "Nombre del Estacionamiento",
        validators = [name_validator],
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Estacionamiento'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )


    direccion = forms.CharField(
        required = True,
        label    = "Direccion",
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Dirección'
            , 'message'     : 'La entrada no puede quedar vacía.'
            }
        )
    )

    telefono1 = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono 1'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    telefono2 = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono 2'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    telefono3 = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono 3'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    email1 = forms.EmailField(
        required = False,
        widget   = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'E-mail 1'
            , 'message'     : 'La entrada debe ser un e-mail válido.'
            }
        )
    )

    email2 = forms.EmailField(
        required = False,
        widget   = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'E-mail 2'
            , 'message'     : 'La entrada debe ser un e-mail válido.'
            }
        )
    )

    rif = forms.CharField(
        required   = True,
        label      = "RIF",
        validators = [rif_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'RIF: X-xxxxxxxxx'
            , 'pattern'     : rif_validator.regex.pattern
            , 'message'     : rif_validator.message
            }
        )
    )

class CrearBilleteraForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[VE]-[0-9]+$',
        message = 'La cédula debe estar en formato V/E-NumCedula'
    )

    name_validator = RegexValidator(
        regex   = '^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ\-\' ]+$',
        message = 'La entrada debe ser un nombre en Español sin símbolos especiales.'
    )

    pin_validator = RegexValidator(
        regex = '^[\s\S]{4,6}$',
        message = 'El PIN debe contener entre 4 y 6 caracteres'
        )
    
    nombre = forms.CharField(
        required = True,
        label    = "Nombre del Usuario",
        validators = [name_validator],
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Usuario'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )

    apellido = forms.CharField(
        required = True,
        label    = "Apeliido del Usuario",
        validators = [name_validator],
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Apellido del Usuario'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

    pin = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'PIN de la billetera'
            , 'pattern'     : pin_validator.regex.pattern
            , 'message'     : pin_validator.message
            }
        )
    )

class PropietarioForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'La cédula solo puede contener caracteres numéricos.'
    )

    phone_validator = RegexValidator(
        regex   = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
        message = 'Debe introducir un formato válido de teléfono.'
    )
    
    name_validator = RegexValidator(
        regex   = '^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ\-\' ]+$',
        message = 'La entrada debe ser un nombre en Español sin símbolos especiales.'
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

    nombre = forms.CharField(
        required = True,
        label    = "Nombre del Dueño de Estacionamiento",
        validators = [name_validator],
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Dueño de Estacionamiento'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )

    apellido = forms.CharField(
        required = True,
        label    = "Apeliido del Dueño de Estacionamiento",
        validators = [name_validator],
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Apellido del Dueño de Estacionamiento'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )

    telefono = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono del Dueño'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    email = forms.EmailField(
        required = False,
        widget   = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'E-mail del Dueño'
            , 'message'     : 'La entrada debe ser un e-mail válido.'
            }
        )
    )

class EstacionamientoExtendedForm(forms.Form):
    
    tarifa_validator = RegexValidator(
        regex   = '^([0-9]+(\.[0-9]+)?)$',
        message = 'Sólo debe contener dígitos.'
    )
    
    puestos = forms.IntegerField(
        required  = True,
        min_value = 1,
        label     = 'Número de Puestos',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Número de Puestos'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    horarioin = forms.TimeField(
        required = True,
        label    = 'Horario Apertura',
        widget   = forms.TextInput(attrs =
            { 'class':'form-control'
            , 'placeholder' : 'Horario Apertura'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )

    horarioout = forms.TimeField(
        required = True,
        label    = 'Horario Cierre',
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horario Cierre'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )

    choices_esquema = [
        ('TarifaHora', 'Por hora'),
        ('TarifaMinuto', 'Por minuto'),
        ('TarifaHorayFraccion', 'Por hora y fracción'),
        ('TarifaHoraPico', 'Diferenciada por horario pico'),
        ('TarifaFinDeSemana', 'Diferenciada para fines de semana')
    ]

    esquema = forms.ChoiceField(
        required = True,
        choices  = choices_esquema,
        widget   = forms.Select(attrs =
            { 'class' : 'form-control' }
        )
    )

    tarifa = forms.DecimalField(
        required   = True,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2 = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    inicioTarifa2 = forms.TimeField(
        required = False,
        label    = 'Inicio Horario Especial',
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horario Inicio Reserva'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )

    finTarifa2 = forms.TimeField(
        required = False,
        label    = 'Fin Horario Especial',
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horario Fin Reserva'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )

class ReservaForm(forms.Form):
    
    inicio = forms.SplitDateTimeField(
        required = True,
        label = 'Horario Inicio Reserva',
        widget= CustomSplitDateTimeWidget(attrs=
            { 'class'       : 'form-control'
            , 'type'        : 'date'
            , 'placeholder' : 'Hora Inicio Reserva'
            }
        )
    )

    final = forms.SplitDateTimeField(
        required = True,
        label    = 'Horario Final Reserva',
        widget   = CustomSplitDateTimeWidget(attrs=
            { 'class'       : 'form-control'
            , 'type'        : 'date'
            , 'placeholder' : 'Hora Final Reserva'
            }
        )
    )

class PagoForm(forms.Form):
    
    card_name_validator = RegexValidator(
        regex   = '^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ\-\' ]+$',
        message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    card_surname_validator = RegexValidator(
        regex   = '^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ\-\' ]+$',
        message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'La cédula solo puede contener caracteres numéricos.'
    )
    
    card_validator = RegexValidator(
        regex   = '^[0-9]{16}$',
        message = 'Introduzca un número de tarjeta válido de 16 dígitos.'
    )
    
    nombre = forms.CharField(
        required   = True,
        label      = "Nombre del Tarjetahabiente",
        validators = [card_name_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Tarjetahabiente'
            , 'pattern'     : card_name_validator.regex.pattern
            , 'message'     : card_name_validator.message
            }
        )
    )

    apellido = forms.CharField(
        required   = True,
        label      = "Apellido del Tarjetahabiente",
        validators = [card_surname_validator],
        widget = forms.TextInput(attrs =
            { 'class'      : 'form-control'
            , 'placeholder' : 'Apellido del Tarjetahabiente'
            , 'pattern'     : card_surname_validator.regex.pattern
            , 'message'     : card_surname_validator.message
            }
        )
    )

    cedulaTipo = forms.ChoiceField(
        required = True,
        label    = 'cedulaTipo',
        choices  = (
            ('V', 'V'),
            ('E', 'E')
        ),
        widget   = forms.Select(attrs =
            { 'class' : 'form-control' }
        )
    )

    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

    tarjetaTipo = forms.ChoiceField(
        required = True,
        label    = 'tarjetaTipo',
        choices  = (
            ('Vista',  ' VISTA '),
            ('Mister', ' MISTER '),
            ('Xpress', ' XPRESS ')
        ),
        widget   = forms.RadioSelect()
    )

    tarjeta = forms.CharField(
        required   = True,
        label      = "Tarjeta de Credito",
        validators = [card_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarjeta de Credito'
            , 'pattern'     : card_validator.regex.pattern
            , 'message'     : card_validator.message
            }
        )
    )

class RifForm(forms.Form):
    
    rif_validator = RegexValidator(
        regex   = '^[JVD]-\d{8}-?\d$',
        message = 'Introduzca un RIF con un formato válido de la forma X-xxxxxxxxx.'                              
    )
    
    rif = forms.CharField(
        required   = True,
        label      = "RIF",
        validators = [rif_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'RIF: X-xxxxxxxxx'
            , 'pattern'     : rif_validator.regex.pattern
            , 'message'     : rif_validator.message
            }
        )
    )

class CedulaForm(forms.Form):
    
    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'La cédula solo puede contener caracteres numéricos.'
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

class RecargaForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[1-9]{1}([0-9]+)?$',
        message = 'El ID solo puede contener caracteres numéricos.'
    )

    validar_pin = RegexValidator(
    regex = '^[\s\S]{4,6}$',
    message = 'El PIN debe contener entre 4 y 6 caracteres'
    )


    billetera_id = forms.CharField(
        required   = True,
        label      = "ID",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )
    
    pin = forms.CharField(
        required = True,
        label = "PIN",
        validators = [validar_pin],
        widget = forms.TextInput(attrs =
                { 'class'       : 'form-control'
                , 'placeholder' : 'PIN'
                , 'pattern'     : validar_pin.regex.pattern
                , 'message'     : validar_pin.message
                }
        )
    )

    validar_monto = RegexValidator(
        regex = '^[0-9]+(\.[0-9]{1,2})?$',
        message = 'El monto debe ser valido'
    )

    monto = forms.CharField(
        required = True,
        label = "Monto",
        validators = [validar_monto],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Monto'
            , 'pattern'     : validar_monto.regex.pattern
            , 'message'     : validar_monto.message
            }
        )
    )

class ConsumirForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[1-9]{1}([0-9]+)?$',
        message = 'El ID solo puede contener caracteres numéricos.'
    )

    validar_pin = RegexValidator(
        regex = '^[\s\S]{4,6}$',
        message = 'El PIN debe contener entre 4 y 6 caracteres'
        )

    billetera_id = forms.CharField(
        required   = True,
        label      = "ID",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

    pin = forms.CharField(
        required = True,
        label = "PIN",
        validators = [validar_pin],
        widget = forms.TextInput(attrs =
                { 'class'       : 'form-control'
                , 'placeholder' : 'PIN'
                , 'pattern'     : validar_pin.regex.pattern
                , 'message'     : validar_pin.message
                }
        )
    )

    validar_monto = RegexValidator(
        regex = '^[0-9]+(\.[0-9]{1,2})?$',
        message = 'El monto debe ser valido'
    )

    monto = forms.CharField(
        required = True,
        label = "Monto",
        validators = [validar_monto],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Monto'
            , 'pattern'     : validar_monto.regex.pattern
            , 'message'     : validar_monto.message
            }
        )
    )

class SaldoForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[1-9]{1}([0-9]+)?$',
        message = 'El ID solo puede contener caracteres numéricos.'
    )
    
    billetera_id = forms.CharField(
        required   = True,
        label      = "ID",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )

    validar_pin = RegexValidator(
        regex = '^[\s\S]{4,6}$',
        message = 'El PIN debe contener entre 4 y 6 caracteres'
        )

    pin = forms.CharField(
        required = True,
        label = "PIN",
        validators = [validar_pin],
        widget = forms.TextInput(attrs =
                { 'class'       : 'form-control'
                , 'placeholder' : 'PIN'
                , 'pattern'     : validar_pin.regex.pattern
                , 'message'     : validar_pin.message
                }
        )
    )

class ModificarPropietarioForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'La cédula solo puede contener caracteres numéricos.'
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )
    
class CancelarReservaForm(forms.Form):

    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'La cédula debe estar en formato V/E-NumCedula'
    )
    
    identificador_validator = RegexValidator(
        regex   = '^[1-9]{1}([0-9]+)?$',
        message = 'El identificador solo puede contener caracteres numéricos.'
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )
    
    numero_pago = forms.CharField(
        required   = True,
        label      = "ID de confirmación de pago",        
        validators = [identificador_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID de confirmación de pago'
            , 'pattern'     : identificador_validator.regex.pattern
            , 'message'     : identificador_validator.message
            }
        )
    )
    
    billetera_id_validator = RegexValidator(
        regex   = '^[1-9]{1}([0-9]+)?$',
        message = 'El ID solo puede contener caracteres numéricos.'
    )
    
    billetera_id = forms.CharField(
        required   = True,
        label      = "ID",
        validators = [billetera_id_validator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID Billetera'
            , 'pattern'     : billetera_id_validator.regex.pattern
            , 'message'     : billetera_id_validator.message
            }
        )
    )

    validar_pin = RegexValidator(
        regex = '^[\s\S]{4,6}$',
        message = 'El PIN debe contener entre 4 y 6 caracteres'
        )

    pin = forms.CharField(
        required = True,
        label = "PIN",
        validators = [validar_pin],
        widget = forms.TextInput(attrs =
                { 'class'       : 'form-control'
                , 'placeholder' : 'PIN'
                , 'pattern'     : validar_pin.regex.pattern
                , 'message'     : validar_pin.message
                }
        )
    )

