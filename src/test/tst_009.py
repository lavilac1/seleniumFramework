# -*- coding: utf-8 -*-

# FRAME
#verificaciones
import unittest
from src.functions.Functions import Functions as Selenium


class Test_009(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
 

    def test_009(self):
        Selenium.get_json_file(self, "Spotify")
        
        Selenium.get_elements(self, "txt_correo").send_keys("luisalanana@hotmail.com")
        Selenium.send_especific_keys(self, "txt_correo", "Tab")
        
        verificar = Selenium.check_element(self, "lbl_errorcorreo")
        
        
        if verificar == True:
            #Selenium.get_elements(self, "txt_correo").clear()
            Selenium.send_key_text(self, "txt_correo", "9087665@hotmail.com")
            Selenium.send_especific_keys(self, "txt_correo", "Tab")
            #unittest.TestCase.skipTest(self, "El email ya existe")
        
        
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