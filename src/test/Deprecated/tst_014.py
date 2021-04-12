'''
Created on 15/01/2021

@author: Luisa Avila
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common import exceptions
   

class Test_014(unittest.TestCase):


    def setUp(self):
        
        self.driver = webdriver.Chrome()
        print("Current session is {}".format(self.driver.session_id))
        self.action = ActionChains(self.driver)
        self.driver.get("https://www.mercadolibre.com.co/")
 

    def test_014(self):
        localizador = self.driver.find_element(By.XPATH,
                                               "/html/body/header/div/div[2]/ul/li[2]/a")

        action = ActionChains(self.driver)

        action.move_to_element(localizador)
        action.perform()

        localizador2 = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/nav[1]/section[1]/ul[2]/li[1]/a[1]")
                                                
        action.move_to_element(localizador2)
        action.perform()

        time.sleep(5)

        localizador3 = self.driver.find_element(By.XPATH,
                                                "/html/body/header/div/div[2]/ul/li[2]/nav/section[2]/div/div/article[1]/h2/a")
        localizador3.click()

        time.sleep(10)
        
        try:
            self.driver.get("https://www.mercadolibre.com.co/")
        except exceptions.InvalidSessionIdException as e:
            print(e.message)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    

