# -*- coding: utf-8 -*-

# FRAME
#verificaciones
import unittest
import allure
from src.functions.Functions import Functions as Selenium

@allure.feature(u'Test Udemy')
@allure.story(u'Entrar a google y enviar una fecha')
@allure.testcase(u'Caso de prueba 018')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Se ingresa a la pagiga de google y se busca la fecha de hoy')

class Test_018(Selenium, unittest.TestCase):


    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a la pagina de google'):

            Selenium.abrir_navegador(self, "https://www.google.com/?hl=es")
            Selenium.get_json_file(self, "google")

    def test_018(self):
            
        with allure.step(u'Paso 2: Retornar el valor'):
            fecha = Selenium.textDateEnvironmentReplace(self, "today")
            Selenium.get_elements(self, "txt_buscar").send_keys(fecha)       
            Selenium.esperar(5)
                  
      

    def tearDown(self):
        with allure.step(u'Paso 3: Cerrar el navegador'):
            Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    