# -*- coding: utf-8 -*-
'''
Created on 21/01/2021

@author: Luisa Avila
'''
import time
import unittest
from src.pages.Spotify_registro import Registro as Spoty_registro

from selenium import webdriver
from selenium.webdriver.common.by import By




horaGlobal = time.strftime("%H%M%S")

class Test_019(unittest.TestCase):


    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.spotify.com/co/signup/")
 

    def test_019(self):
 
        self.driver.find_element(By.XPATH, Spoty_registro.txt_correo_xpath).send_keys("arrocito1966@hotmail.com")
        self.driver.find_element(By.XPATH, Spoty_registro.txt_confirmarcorreo_xpath).send_keys("arrocito1966@hotmail.com")
        self.driver.find_element(By.XPATH, Spoty_registro.txt_contrasena_xpath).send_keys("arrocito1966")
        
        self.driver.find_element(By.XPATH, Spoty_registro.btn_registrate_xpath).click()

        time.sleep(10)
        
        title= "test019"
        self.driver.get_screenshot_as_file(f"../\data\capturas\{title} - {horaGlobal}.png")
                
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()