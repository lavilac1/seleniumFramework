'''
Created on 11/01/2021

@author: Luisa Avila
'''
# -*- coding: utf-8 -*-

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    

    def setUp(self):
       
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
       
        

    def test_007(self):
        
        self.driver.get("https://unipython.com/los-mejores-ide-python-instalar-python-os-window-linux/")
        time.sleep(3)
        self.assertIn("Python", self.driver.title)
        time.sleep(3)
        elem = self.driver.find_element_by_name("s")
        time.sleep(3)
        elem.send_keys("aprender")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in self.driver.page_source
        
           
          
      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()