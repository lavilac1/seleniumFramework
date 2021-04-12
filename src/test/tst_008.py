# -*- coding: utf-8 -*-

# FRAME
#assert
import unittest
from src.functions.Functions import Functions as Selenium


class Test_008(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
 

    def test_008(self):
        Selenium.get_json_file(self, "Spotify")
        
        Selenium.send_key_text(self, "txt_correo", "luisalanana@hotmail.com")
        Selenium.send_especific_keys(self, "txt_correo", "Tab")
        
        Selenium.assert_text(self, "lbl_errorcorreo", "Este correo electrónico ya está conectado a una cuenta. Inicia sesión.")
        
        Selenium.esperar(5)
                  
      

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''
Created on 26/01/2021

@author: Luisa Avila
'''
