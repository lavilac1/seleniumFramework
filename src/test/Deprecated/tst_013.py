## Traer una lista de elementos en un array y recorrerlo VIDEO 28

'''
Created on 14/01/2021

@author: Luisa Avila
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.get("https://www.mercadolibre.com.co/")
        self.LISTADO = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'slick-slide slick-active')]")
        self.LISTADO2 = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'price-tag-fraction')]")
        

        print ("listado de elementos encontrados" + str(self.LISTADO))
        
        self.count = 0
        
        for self.lista in self.LISTADO:
            
            print(self.lista.text)
            self.count = self.count + 1
            print(self.count)
            
            
        for self.lista2 in self.LISTADO2:
            print(self.lista2.text)

    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()