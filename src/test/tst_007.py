# -*- coding: utf-8 -*-

# FRAME
#ENVIAR TECLAS ENTER, TAB
import unittest
from src.functions.Functions import Functions as Selenium


class Test_007(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "http://omega.compuhora.com.co:8088/cordoba/login")
 

    def test_007(self):
        Selenium.get_json_file(self, "alphasig")
        
        Selenium.send_key_text(self, "txt_USUARIO", "alpha")
        
        Selenium.send_especific_keys(self,"txt_USUARIO", "Tab")
        
        Selenium.send_key_text(self, "txt_CLAVE", "homero")
                   
        Selenium.send_especific_keys(self,"txt_CLAVE", "Enter")
        
        Selenium.esperar(5)
                  
      

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
