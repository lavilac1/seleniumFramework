# -*- coding: utf-8 -*-


#CAPTURAS
import unittest
from src.functions.Functions import Functions as Selenium
import allure

@allure.feature(u'Test Udemy')
@allure.story(u'Captura pantalla')
@allure.testcase(u'Caso de prueba 015')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Se ingresa a la pagina de spotify y captura la pantalla')

class Test_015(Selenium, unittest.TestCase):


    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a la pagina de spotify'):
            Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
   
 

    def test_015(self):
        with allure.step(u'Paso 2: Tomar la captura'):      
            Selenium.captura(self, "Spotify")
           

    def tearDown(self):
        with allure.step(u'Paso 3: Cerrar navegador'):
            Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    

