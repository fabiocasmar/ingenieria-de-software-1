# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time

from estacionamientos.forms import EstacionamientoExtendedForm

###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

class ExtendedFormTestCase(TestCase):

    # malicia
    def test_estacionamiento_extended_form_un_campo(self):
        form_data = { 'puestos1': 2}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_dos_campo(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_tres_campo(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_cuatro_campo(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_cinco_campos(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time(hour = 6,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_seis_campos(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_estacionamiento_extended_form_siete_bien(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 12
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_estacionamiento_extended_form_todos_campos_bien(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':'TarifaMinuto',
                      'horizonteDias':15,
                      'horizonteHoras': 0
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # caso borde
    def test_estacionamiento_extended_form_puestos_1(self):
        form_data = { 'puestos1': 1,
                      'puestos2': 1,
                      'puestos3': 1,
                      'puestos4': 1,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':'TarifaHora',
                      'horizonteDias':15,
                      'horizonteHoras': 0}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_puestos_negativos(self):
        form_data = { 'puestos1': -1,
                      'puestos2': -1,
                      'puestos3': -1,
                      'puestos4': -1,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': '12',
                      'esquema':'TarifaHora'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_estacionamiento_extended_form_puestos_0(self):
        form_data = { 'puestos1': 0,
                      'puestos2': 0,
                      'puestos3': 0,
                      'puestos4': 0,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':'TarifaHora',
                      'horizonteDias':15,
                      'horizonteHoras': 0}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    # caso borde
    def test_estacionamiento_extended_form_hora_inicio_igual_hora_cierre(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 6,  minute = 0),
                      'tarifa': '12',
                      'esquema':'TarifaHora'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # esquina
    def test_estacionamiento_extended_form_hora_inicio_igual_hora_cierre_y_puesto_0(self):
        form_data = { 'puestos1': 0,
                      'puestos2': 0,
                      'puestos3': 0,
                      'puestos4': 0,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 6,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':'TarifaHora',
                      'horizonteDias':15,
                      'horizonteHoras': 0
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_string_en_campo_puesto(self):
        form_data = { 'puestos1': 'hola',
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':15,
                      'horizonteHoras': 0
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_string_hora_inicio(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': 'holaa',
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':15,
                      'horizonteHoras': 0
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_none_en_tarifa(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': None,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':15,
                      'horizonteHoras': 0
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

      # malicia
    def test_estacionamiento_extended_form_maxDias(self):
        form_data = { 'puestos': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':15,
                      'horizonteHoras':5
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())    
    #borde
    def test_estacionamiento_extended_form_horizonte_dias_cero(self):
        form_data = { 'puestos': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':0,
                      'horizonteHoras': 0
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid()) 
    #borde    
    def test_estacionamiento_extended_form_maximoDias_maximaHoras(self):
        form_data = { 'puestos': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':14,
                      'horizonteHoras': 23
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())       
    #borde    
    def test_estacionamiento_extended_form_minimoDias_maximaHoras(self):
          form_data = { 'puestos': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 1.2,
                      'esquema':('TarifaHora', 'Por hora'),
                      'horizonteDias':0,
                      'horizonteHoras': 23
                    }
          form = EstacionamientoExtendedForm(data = form_data)
          self.assertFalse(form.is_valid())    
    #borde      
    def test_estacionamiento_extended_form_maximoDias_unaHora(self):
          form_data = { 'puestos': 2,
                        'horarioin': time( hour = 6,  minute = 0),
                        'horarioout': time(hour = 19,  minute = 0),
                        'tarifa': 1.2,
                        'esquema':('TarifaHora', 'Por hora'),
                        'horizonteDias':14,
                        'horizonteHoras': 1
                      }
          form = EstacionamientoExtendedForm(data = form_data)
          self.assertFalse(form.is_valid())   

     #borde      
    def test_estacionamiento_extended_form_unDia_unaHora(self):
          form_data = { 'puestos': 2,
                        'horarioin': time( hour = 6,  minute = 0),
                        'horarioout': time(hour = 19,  minute = 0),
                        'tarifa': 1.2,
                        'esquema':('TarifaHora', 'Por hora'),
                        'horizonteDias':1,
                        'horizonteHoras': 1
                      }
          form = EstacionamientoExtendedForm(data = form_data)
          self.assertFalse(form.is_valid())            

     # malicia
    def test_estacionamiento_extended_form_none_en_esquema(self):
        form_data = { 'puestos1': 2,
                      'puestos2': 2,
                      'puestos3': 2,
                      'puestos4': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': '12',
                      'esquema':None
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())
