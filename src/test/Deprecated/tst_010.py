#Moverse entre Ventanas

'''
Created on 11/01/2021

@author: Luisa Avila
'''
# FRAME
import unittest
import time
from selenium import webdriver


class Test_012(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP DE REGISTRO
        self.driver.get("http://www.echoecho.com/htmllinks10.htm")

    def test_012(self):
        #MAIN
        self.main_Enlace = self.driver.find_element_by_xpath("//span[contains(text(),'Go to Yahoo')]")
        self.main_Enlace.click()

        print("Ventanas" + str(self.driver.window_handles))

        time.sleep(10)

        self.driver.switch_to.window(self.driver.window_handles[0])

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()