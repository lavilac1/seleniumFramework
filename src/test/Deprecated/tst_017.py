'''
Created on 15/01/2021

@author: Luisa Avila
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
   

class Test_015(unittest.TestCase):


    def setUp(self):
        
        self.driver = webdriver.Chrome()
        print("Current session is {}".format(self.driver.session_id))
       
        self.driver.get("https://www.amazon.com/")
 

    def test_015(self):
        localizador = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
        
        localizador2 = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]")
        self.driver.execute_script("arguments[0].click();", localizador2)
        

        time.sleep(10)
        
        assert "About Amazon" == self.driver.title, "No son iguales"
        
        try:
            self.driver.get("https://www.amazon.com/")
        except exceptions.InvalidSessionIdException as e:
            print(e.message)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    

