# -*- coding: utf-8 -*-

# FRAME
#verificaciones
import unittest
from src.functions.Functions import Functions as Selenium


class Test_010(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "https://www.spotify.com/co/signup/")
 

    def test_010(self):
        Selenium.get_json_file(self, "Spotify")
        
       
        Selenium.save_variable_scenary(self, "lbl_titulo", "Titulo")#obtengo el valor del elemento lbl_titulo y lo guardo en el directorio
        
        Selenium.new_window(self, "https://www.google.com/?hl=es")#ABRIR UNA NUEVA VENTANA 
        Selenium.get_json_file(self, "google")#TRAER EL JSON DE GOOGLE
        Selenium.switch_to_windows_name(self, "google")# ME UBICO EN LA VENTANA DE GOOGLE
        
        
        texto = Selenium.get_variable_scenary(self, "Titulo")
        
        Selenium.send_key_text(self, "txt_buscar", texto)
 
        
        Selenium.esperar(5)
                  
      

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
