# -*- coding: utf-8 -*-

# FRAME
import time
import unittest
from src.functions.Functions import Functions as Selenium



class Test_004(Selenium, unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.mercadolibre.com.co/")

    def test_004(self):
        #cargar el JSON con los valores de los ID de la APP
        Selenium.get_json_file(self, "iframe")
        
        Selenium.new_window(self, "https://www.mercadolibre.com.co/gz/home/navigation#nav-header")
        
        Selenium.switch_to_windows_name(self, "Historial")
        
        Selenium.switch_to_windows_name(self, "Principal")
        
        time.sleep(10)
        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()