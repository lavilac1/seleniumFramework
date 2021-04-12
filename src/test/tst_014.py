# -*- coding: utf-8 -*-

# FRAME
#verificaciones
import unittest
from src.functions.Functions import Functions as Selenium
import allure

@allure.feature(u'Test Udemy')
@allure.story(u'Pasar entre ventanas')
@allure.testcase(u'Caso de prueba 014')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Se ingresa a la pagina de spotify y se pasa a la pgina de google se lee un excel se trae una selda y se escribe')

class Test_014(Selenium, unittest.TestCase):


    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a la pagina de spotify'):
            Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
            Selenium.get_json_file(self, "Spotify")


    def test_014(self):
        with allure.step(u'Paso 2: pasarse a la ventana de google'):
            Selenium.save_variable_scenary(self, "lbl_titulo", "Titulo")#obtengo el valor del elemento lbl_titulo y lo guardo en el directorio
        
            Selenium.new_window(self, "https://www.google.com/?hl=es")#ABRIR UNA NUEVA VENTANA 
            Selenium.get_json_file(self, "google")#TRAER EL JSON DE GOOGLE
            Selenium.switch_to_windows_name(self, "google")# ME UBICO EN LA VENTANA DE GOOGLE
           
            Selenium.esperar(5)
            
        with allure.step(u'Paso 3: Recuperar datos del excel'):
            #RECUPERAR DATOS DESD EXCEL.
        
            NOMBRE = Selenium.leer_celda(self, "A1")
            Selenium.create_variable_scenary(self, "nombre", NOMBRE)
            Selenium.create_variable_scenary(self, "apellido", Selenium.leer_celda(self, "B1"))    
            Selenium.create_variable_scenary(self, "cedula", Selenium.leer_celda(self, "C1"))   
        
            texto = Selenium.get_variable_scenary(self, "nombre")
        
            Selenium.send_key_text(self, "txt_buscar", texto)   
        
            Selenium.esperar(5)
      

    def tearDown(self):
        with allure.step(u'Paso 4: Cerra navegador'):
            Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
'''
Created on 26/01/2021

@author: Luisa Avila
'''
