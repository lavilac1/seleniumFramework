# -*- coding: utf-8 -*-
'''
Created on 10/01/2021

@author: Luisa Avila
'''
import unittest
import time
from selenium import webdriver

class Test_005(unittest.TestCase):


    def setUp(self):
       
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.NOMBRE = "Luisa "
        self.APELLIDO = "Avila "
        self.USERNAME = "lavila233344"
        self.PASSWORD = "Udemytest2019-A"
        

    def test_005(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        
        #COLOCAR NOMBRE
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys(self.NOMBRE)
        
        #COLOCAR APELLIDO
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").clear()
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").send_keys(self.APELLIDO)
        
        #COLOCAR USERNAME
        self.driver.find_element_by_name("Username").clear()
        self.driver.find_element_by_name("Username").send_keys(self.USERNAME)
        
        #COLOCAR PASSWORD
        self.driver.find_element_by_name("Passwd").clear()
        self.driver.find_element_by_name("Passwd").send_keys(self.PASSWORD)
        
        #COLOCAR CONFIRMACION DE  PASSWORD
        self.driver.find_element_by_name("ConfirmPasswd").clear()
        self.driver.find_element_by_name("ConfirmPasswd").send_keys(self.PASSWORD)
        
        #BOTON NEXT
        self.driver.find_element_by_xpath("//*[@id='accountDetailsNext']").click()
        
        time.sleep(10)
        
        #MENSAJE DE VALIDACION
        MENSAJE_ERROR = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div").text
       
        print(MENSAJE_ERROR)
    
        assert MENSAJE_ERROR == "Verifica tu teléfono", "No coinciden"
    
    def tearDown(self):
        
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()