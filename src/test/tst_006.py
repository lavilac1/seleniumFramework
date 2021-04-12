# -*- coding: utf-8 -*-

# FRAME
#INTERARTUAR CON ALERTAS
import unittest
from src.functions.Functions import Functions as Selenium


class Test_006(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "http://omega.compuhora.com.co/HelpDesk/default.aspx")
 

    def test_006(self):
        Selenium.get_json_file(self, "helpdesk")
        
        Selenium.send_key_text(self, "txt_agente", "alpha")
        
        Selenium.send_key_text(self, "txt_contrasena", "alaaa")
        
        Selenium.get_elements(self, "btn_aceptar").click()
        
        Selenium.esperar(4)
        
        Selenium.alert_windows(self, "accept")
        
        
        Selenium.esperar(5)
                  
      

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()