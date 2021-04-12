# -*- coding: utf-8 -*-
import time
import unittest
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro

class test_002(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_002(self):
        #cargar el JSON con los valores de los ID de la APP
        Selenium.get_json_file(self, "Spotify")
        
        #Acceder a las keys (entidades) del JSON
        Selenium.get_entity(self, "lbl_titulo")
        
        assert Selenium.get_elements(self, "lbl_titulo").text == "Regístrate gratis para escuchar"
        
        Selenium.esperar_elemento(self, "txt_correo")
        
        Selenium.get_elements(self, "txt_correo").send_keys("ulurogiju@gmail.com")
        
        Selenium.get_elements(self, "txt_confirmarcorre").send_keys("ulurogiju@gmail.com")
        
        Selenium.get_elements(self, "txt_contrasena").send_keys("ul33333")
        
        Selenium.get_select_elements(self, "dpd_mes").select_by_value('10')
        
        Selenium.get_elements(self, "btn_registrate").click()
        
      


        time.sleep(5)
        
    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
