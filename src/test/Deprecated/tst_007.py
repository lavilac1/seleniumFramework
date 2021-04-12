# -*- coding: utf-8 -*-
'''
Created on 10/01/2021

@author: Luisa Avila
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Test_007(unittest.TestCase):


    def setUp(self):
       
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.CONSULTAR = "Sobres"
        self.LISTA = "Nacional"
        

    def test_007(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://www.correoargentino.com.ar/servicios/paqueteria")
        
        
        #COLOCAR USERNAME
        self.driver.find_element_by_id("edit-custom-search-blocks-form-1--2").clear()
        self.driver.find_element_by_id("edit-custom-search-blocks-form-1--2").send_keys(self.CONSULTAR)
        
        
        select = Select(self.driver.find_element_by_id("edit-custom-search-vocabulary-8"))
        select.select_by_visible_text(self.LISTA)
        
       
        
       
      
        
                
        time.sleep(10)
        
       
    
    def tearDown(self):
        
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()