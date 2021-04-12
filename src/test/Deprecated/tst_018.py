# -*- coding: utf-8 -*-
'''
Created on 21/01/2021

@author: Luisa Avila
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By




class Test018(unittest.TestCase):


    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.LISTA = "Luisa"
        self.driver.get("http://omega.compuhora.com.co/NuevoHelpDesk")

    def test018(self):
        
        self.driver.find_element_by_name("usuario").send_keys("alphas")
        self.driver.find_element_by_name("usuario").send_keys(Keys.BACK_SPACE) # Borrar una letra
       
        self.driver.find_element_by_name("contrasena").send_keys("1234")
        
        self.driver.find_element_by_xpath("//*[@id='datos']/div[3]/div/button").send_keys(Keys.ENTER)
        
        title = "Sistema de soporte técnico (SST) 6.0"
        assert title == self.driver.title, "No son iguales"
        
    
        self.driver.find_element_by_id("idcaso").send_keys("23")
       
        
        
        
        time.sleep(10)
    
    
    
    def tearDown(self):
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()