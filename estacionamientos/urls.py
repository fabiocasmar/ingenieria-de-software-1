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
    url(r'^billetera_movimientos$', views.billetera_movimientos, name = 'billetera_movimientos'),
    url(r'^sms$', views.receive_sms, name='receive_sms'),
    url(r'^grafica/.*$', views.grafica_tasa_de_reservacion, name = 'grafica_tasa_de_reservacion'),
    url(r'^cancelar_reserva$', views.cancelar_reserva, name = 'cancelar_reserva'),
    url(r'^confirmar_cancelacion$', views.confirmar_cancelacion, name = 'confirmar_cancelacion'),
    url(r'^(?P<_id>[VE]-\d+)/tasa$', views.tasa_de_reservacion, name = 'tasa_de_reservacion'),
    url(r'^(?P<_id>[VE]-\d+)/editar_dueno$', views.editar_dueno, name = 'editar_dueno'),
    url(r'^(?P<_id>[VE]-\d+)/propietario_crear_editar$', views.propietario_crear_editar, name = 'propietario_crear_editar'),
    url(r'^(?P<_id>[VE]-\d+)/crear_estacionamiento$', views.crear_estacionamiento, name = 'crear_estacionamiento'),
)
