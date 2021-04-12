# -*- coding: utf-8 -*-
#alphasig login
'''
Created on 10/01/2021

@author: Luisa Avila
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_005(unittest.TestCase):


    def setUp(self):
       
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(15)
        self.USERNAME = "alpha"
        self.PASSWORD = "homero"
        

    def test_005(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("http://omega.compuhora.com.co:8088/cordoba/login")
        
        
        #COLOCAR USERNAME
        self.driver.find_element_by_id("input_username").clear()
        self.driver.find_element_by_id("input_username").send_keys(self.USERNAME)
        
        #COLOCAR PASSWORD
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(self.PASSWORD,Keys.RETURN)
        
       
      
        
                
        time.sleep(10)
        
       
    
    def tearDown(self):
        
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()