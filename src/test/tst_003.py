# -*- coding: utf-8 -*-

# FRAME
import time
import unittest
from src.functions.Functions import Functions as Selenium



class Test_003(Selenium, unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, "https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_003(self):
        #cargar el JSON con los valores de los ID de la APP
        Selenium.get_json_file(self, "iframe")
        
        Selenium.switch_to_iframe(self, "fra_frame2")
        
        Selenium.select_by_text(self, "dpd_animales", "Avatar")
        
        Selenium.switch_to_parentFrame(self)
        
        Selenium.switch_to_iframe(self, "fra_frame1")
        
        Selenium.send_key_text(self, "txt_topic", "Hola soy Luisa")
        
        Selenium.switch_to_iframe(self, "fra_frame3")
        
        Selenium.get_elements(self, "chk_options").click()
        
        time.sleep(10)
        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()