# -*- coding: utf-8 -*-
import time
import unittest
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro

class test_001(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_001(self):
        assert Selenium.xpath_element(self, Registro.lbl_titulo_xpath).text == "Regístrate gratis para escuchar"
        print (Selenium.xpath_element(self, Registro.lbl_titulo_xpath).text)
        
        Selenium.xpath_element(self, Registro.txt_correo_xpath).send_keys("lulurogiju@gmail.com")
        Selenium.xpath_element(self, Registro.txt_confirmarcorreo_xpath).send_keys("lulurogiju@gmail.com")
        
        Selenium._id_element(self, Registro.txt_contrasena_id).send_keys("lulurogiju@gmail.com")
        Selenium.xpath_element(self, Registro.btn_registrate_xpath).click()
        
        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
