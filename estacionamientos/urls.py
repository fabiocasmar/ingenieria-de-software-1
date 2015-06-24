# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from estacionamientos import views


# Este error es raro, en django funciona
urlpatterns = patterns('',
    url(r'^$', views.estacionamientos_all, name = 'estacionamientos_all'),
    url(r'^(?P<_id>\d+)/$', views.estacionamiento_detail, name = 'estacionamiento_detail'),
    url(r'^(?P<_id>\d+)/reserva$', views.estacionamiento_reserva, name = 'estacionamiento_reserva'),
    url(r'^(?P<_id>\d+)/pago$', views.estacionamiento_pago, name = 'estacionamiento_pago'),
    url(r'^(?P<_id>\d+)/pago_billetera/(?P<_monto>\d+.\d{2})$', views.billetera_consumir, name = 'billetera_consumir'),
    url(r'^ingreso$', views.estacionamiento_ingreso, name = 'estacionamiento_ingreso'),
    url(r'^menupropietario$', views.menu_propietario, name = 'menu_propietario'),
    url(r'^propietario$', views.crear_propietario, name = 'crear_propietario'),
    url(r'^buscar_propietario$', views.buscar_propietario, name = 'buscar_propietario'),
    url(r'^modificar_propietario$', views.modificar_propietario, name = 'modificar_propietario'),
    url(r'^billetera$', views.crear_billetera, name = 'crear_billetera'),
    url(r'^menubilletera$', views.menu_billetera, name = 'menu_billetera'),
    url(r'^consulta_reserva$', views.estacionamiento_consulta_reserva, name = 'estacionamiento_consulta_reserva'),
    url(r'^billetera_recargar$', views.billetera_recargar, name = 'billetera_recargar'),
    url(r'^billetera_recargada$', views.billetera_recargar, name = 'billetera_recargada'),
    url(r'^billetera_saldo$', views.billetera_saldo, name = 'billetera_saldo'),
    url(r'^cambiar_pin$', views.cambiar_pin, name = 'cambiar_pin'),
    url(r'^billetera_movimientos$', views.billetera_movimientos, name = 'billetera_movimientos'),
    url(r'^sms$', views.receive_sms, name='receive_sms'),
    url(r'^grafica/.*$', views.grafica_tasa_de_reservacion, name = 'grafica_tasa_de_reservacion'),
    url(r'^cancelar_reserva$', views.cancelar_reserva, name = 'cancelar_reserva'),
    url(r'^configuracion$', views.configuracion, name = 'configuracion'),
    url(r'^confirmar_cancelacion$', views.confirmar_cancelacion, name = 'confirmar_cancelacion'),
    url(r'^mover_reserva$', views.mover_reserva, name = 'mover_reserva'),
    url(r'^cambiar_datos_reserva$', views.cambiar_datos_reserva, name = 'cambiar_datos_reserva'),
    url(r'^reembolsar_reserva$', views.reembolsar_reserva, name = 'reembolsar_reserva'),
    url(r'^mover_reserva_exitosa$', views.mover_reserva_exitosa, name = 'mover_reserva_exitosa'),
    url(r'^pagar_tarjeta_mover_reserva$', views.pagar_tarjeta_mover_reserva, name = 'pagar_tarjeta_mover_reserva'),
    url(r'^pagar_billetera_mover_reserva$', views.pagar_billetera_mover_reserva, name = 'pagar_billetera_mover_reserva'),
    url(r'^pagar_servicio_mover_reserva$', views.pagar_servicio_mover_reserva, name = 'pagar_servicio_mover_reserva'),
    url(r'^pagar_servicio_tarjeta$', views.pagar_servicio_tarjeta, name = 'pagar_servicio_tarjeta'),
    url(r'^pagar_servicio_billetera$', views.pagar_servicio_billetera, name = 'pagar_servicio_billetera'),
    url(r'^(?P<_id>\S+)/tasa$', views.tasa_de_reservacion, name = 'tasa_de_reservacion'),
    url(r'^(?P<_id>\S+)/editar_dueno$', views.editar_dueno, name = 'editar_dueno'),
    url(r'^(?P<_id>[VE]-\d+)/propietario_crear_editar$', views.propietario_crear_editar, name = 'propietario_crear_editar'),
    url(r'^(?P<_id>[VE]-\d+)/crear_estacionamiento$', views.crear_estacionamiento, name = 'crear_estacionamiento'),
)
