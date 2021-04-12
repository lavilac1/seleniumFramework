# -*- coding: utf-8 -*-

# FRAME
import time
import unittest
from src.functions.Functions import Functions as Selenium

   
horaGlobal = time.strftime("%H%M%S")

class Test_005(Selenium, unittest.TestCase):


    def setUp(self):
        
        Selenium.abrir_navegador(self, "https://www.amazon.com/")
 

    def test_005(self):
        Selenium.get_json_file(self, "Amazon")
        
        Selenium.scroll_to(self, "lnk_trabaja_amazon")
        
        Selenium.esperar(5)
               
        Selenium.js_clic(self, "lnk_trabaja_amazon")
        
        
       


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()