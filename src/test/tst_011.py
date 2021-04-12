# -*- coding: utf-8 -*-

# FRAME
#verificaciones
import unittest
from src.functions.Functions import Functions as Selenium
import allure

@allure.feature(u'Test Udemy')
@allure.story(u'Ccomparar titulo')
@allure.testcase(u'Caso de prueba 011')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Se ingresa a la pagina de spotify y se compara el titulo')


class Test_011(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
 

    def test_011(self):
        Selenium.get_json_file(self, "Spotify")
        
       
        Selenium.save_variable_scenary(self, "lbl_titulo", "Titulo")#obtengo el valor del elemento lbl_titulo y lo guardo en el directorio
        
        Selenium.new_window(self, "https://www.spotify.com/co/signup/")#ABRIR UNA NUEVA VENTANA 
        
        Selenium.get_json_file(self, "Spotify")#TRAER EL JSON DE GOOGLE
        Selenium.switch_to_windows_name(self, "spotify")# ME UBICO EN LA VENTANA DE GOOGLE
        
        Selenium.compare_with_variable_scenary(self, "lbl_titulo", "Titulo")
        
        Selenium.esperar(5)
                  
      

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
'''
Created on 26/01/2021

@author: Luisa Avila
'''
