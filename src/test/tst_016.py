# -*- coding: utf-8 -*-


#CAPTURAS
import unittest
from src.functions.Functions import Functions as Selenium
import allure

@allure.feature(u'Test Udemy')
@allure.story(u'Mensaje email duplicado')
@allure.testcase(u'Caso de prueba 016')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Se ingresa a la pagina de spotify y se verifico mensaje de correo repetido')


class Test_016(Selenium, unittest.TestCase):


    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a la pagina de spotify'):
            Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
            Selenium.get_json_file(self, "Spotify")
   
 

    def test_016(self):
        with allure.step(u'Paso 2: Ingresar un correo duplicado'):
            Selenium.send_key_text(self, "txt_correo", "luisalanana@hotmail.com")
            Selenium.get_elements(self, "txt_confirmarcorre").click()
            Mensaje_Email_Obj = Selenium.validar_elemento(self, "lbl_errorcorreo")
            Mensaje_Email_texto = Selenium.get_text(self, "lbl_errorcorreo")
            
        #with allure.step(u'Paso 3: verificar mensaje de correo repetido'):
         #   assert Mensaje_Email_Obj == True, "No se visualizo el mensaje de error email duplicado"
            
            Selenium.esperar(5)

    def tearDown(self):
        with allure.step(u'Paso 4: Cerrar el navegador'):
            Selenium.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
