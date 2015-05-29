# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time, date

from estacionamientos.forms import CrearBilleteraForm

###################################################################
# CREAR_BILLETERA_FORM
###################################################################

class CrearBilleteraFormTestCase(TestCase):
    
    # malicia
    def test_crear_billetera_vacio(self):
        form_data = {}
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #TDD
    def test_test_crear_billetera_UnCampo_nombre(self):
        form_data = {'nombre' : None,
                     'apellido' : 'Zeait Mago Zuñigà',
                     'cedula' : 34567890,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #TDD
    def test_test_crear_billetera_UnCampo_apellido(self):
        form_data = {'nombre' : 'Patricia',
                     'apellido' : None,
                     'cedula' : 34567890,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #TDD
    def test_test_crear_billetera_UnCampo_cedula(self):
        form_data = {'nombre' : 'Patricia',
                     'apellido' : 'Del Valle',
                     'cedula' : None,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # TDD
    def test_crear_billetera_UnCampo_Pin(self):
        form_data = {'nombre': 'Susana',
                     'apellido' : 'Rodríguez',
                     'cedula' : 24222693
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_crear_billetera_DosCampos_Ci_Pin(self):
        form_data = {'nombre': 'Susana',
                     'apellido' : 'Carpio'
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_crear_billetera_DosCampos_nombre_apellido(self):
        form_data = {'cedula': 123456789,
                     'pin' : '6789u'
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_crear_billetera_DosCampos_nombre_ci(self):
        form_data = {'apellido': 'Carrasquel',
                     'pin' : '6789u'
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_crear_billetera_DosCampos_apellido_pin(self):
        form_data = {'nombre': 'Soraya',
                     'cedula' : 23456789
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_crear_billetera_DosCampos_nombre_pin(self):
        form_data = {'apellido': 'Marques',
                     'cedula' : 23456789
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_crear_billetera_DosCampos_apellido_ci(self):
        form_data = {'nombre': 'Daniel',
                     'pin' : '456y'
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_crear_billetera_tresCampos_apellido_cedula_pin(self):
        form_data = {'nombre' : 'Gabriel'}
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
    #borde
    def test_crear_billetera_tresCampos_nombre_cedula_pin(self):
        form_data = {'apellido' : 'Uzcategui'}
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_crear_billetera_tresCampos_nombre_apellido_pin(self):
        form_data = {'cedula' : 24222693}
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_crear_billetera_tresCampos_nombre_apellido_ci(self):
        form_data = {'pin' : '3456h'}
        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())


    #TDD
    def test_crear_billetera_todosCamposBien(self):
        form_data = {'nombre' : 'Mariana',
                     'apellido' : 'Gomez',
                     'cedula' : 24222693,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_nombreConAcento(self):
        form_data = {'nombre' : 'Mónica',
                     'apellido' : 'Gomez',
                     'cedula' : 24222693,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_apellidoConAcento(self):
        form_data = {'nombre' : 'Melissa',
                     'apellido' : 'Gómez',
                     'cedula' : 24222694,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #esquina
    def test_apellidoyNombreConAcento(self):
        form_data = {'nombre' : 'Ána',
                     'apellido' : 'Gómez',
                     'cedula' : 24222694,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_NombreConDieresis(self):
        form_data = {'nombre' : 'Cigüeña',
                     'apellido' : 'Gómez',
                     'cedula' : 24222694,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_apellidoConDieresis(self):
        form_data = {'nombre' : 'Gabriel',
                     'apellido' : 'Ungüento',
                     'cedula' : 242226998,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #esquina
    def test_apellidoYNombreConDieresis(self):
        form_data = {'nombre' : 'cigüeña',
                     'apellido' : 'Ungüento',
                     'cedula' : 242226998,
                     'pin'  : '123fr'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #esquina
    def test_apellidoConguion(self):
        form_data = {'nombre' : 'Susana',
                     'apellido' : 'Rodríguez-Mago',
                     'cedula' : 242226998,
                     'pin'  : '189r'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_nombreConguion(self):
        form_data = {'nombre' : 'Jesus-Sofia',
                     'apellido' : 'Rodríguez',
                     'cedula' : 242226998,
                     'pin'  : '189r'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_nombreConApostrofe(self):
        form_data = {'nombre' : 'Jesus\'Sofia',
                     'apellido' : 'Rodríguez',
                     'cedula' : 242226998,
                     'pin'  : '189r'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_apelllidoConApostrofe(self):
        form_data = {'nombre' : 'Jesus',
                     'apellido' : 'D\'Aguiar',
                     'cedula' : 242226998,
                     'pin'  : '189r'
                     }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_nombreConAcentoAlreves(self):
        form_data = {'nombre' : 'Andrù',
                     'apellido' : 'Zeait',
                     'cedula' : 23014266,
                     'pin' : '676ft'
                    }
        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Esquina
    def test_nombreYApellidoConAcentoAlreves(self):
        form_data = {'nombre' : 'Andrù',
                     'apellido' : 'Zèait',
                     'cedula' : 23014266,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Malicia
    def test_nombreMalo(self):
        form_data = {'nombre' : 'Andres6',
                     'apellido' : 'Zeait',
                     'cedula' : 23014266,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #Malicia
    def test_ApellidoMalo(self):
        form_data = {'nombre' : 'Andres',
                     'apellido' : 'Zeait23',
                     'cedula' : 23014266,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #Malicia
    def test_todos_CamposMAlos(self):
        form_data = {'nombre' : 'Andres23',
                     'apellido' : None,
                     'cedula' : '-23014266',
                     'pin' : None
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())

    #Malicia
    def test_nombreyApellidoCompuesto(self):
        form_data = {'nombre' : 'Andres del Carmen',
                     'apellido' : 'Zeait Mago',
                     'cedula' : 23014266,
                     'pin' : '6567y'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Malicia
    def test_nombreyApellidoCompuesto2(self):
        form_data = {'nombre' : 'Andrés del Carmen Iñaqui',
                     'apellido' : 'Zeait Mago Zuñigà',
                     'cedula' : 23014266,
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Malicia
    def test_cedulaMala(self):
        form_data = {'nombre' : 'Andrés del Carmen Iñaqui',
                     'apellido' : 'Zeait Mago Zuñigà',
                     'cedula' : 'sdss',
                     'pin' : '676ft'
                    }

        form = CrearBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())