# -*- coding: utf-8 -*-


#CAPTURAS
import unittest
from src.functions.Functions import Functions as Selenium
import pytest
import allure


@allure.feature(u'Test Udemy')
@allure.story(u'Entrar a google y enviar una fecha')
@allure.testcase(u'Caso de prueba 018')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Se ingresa a la pagiga de google y se busca la fecha de hoy')

class Test_017(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
        Selenium.get_json_file(self, "Spotify")
   
 

    def test_017(self):
              
        Captcha = Selenium.validar_elemento(self, "chk_captcha")
        
        if Captcha:
            pytest.skip("No se ejecuto la prueba captcha visible ")
           

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
