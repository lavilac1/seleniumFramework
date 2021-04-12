##Alphasig
import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_008(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.USERNAME = "alpha"
        self.PASSWORD = "homero"
        

    def test_008(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("http://omega.compuhora.com.co:8088/cordoba/login")
        
        
        #COLOCAR USERNAME
        self.driver.find_element_by_id("input_username").clear()
        self.driver.find_element_by_id("input_username").send_keys(self.USERNAME)
        
        #COLOCAR PASSWORD
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(self.PASSWORD,Keys.RETURN)
        
        self.driver.find_element(By.ID,"administrator_container").click()
        
        self.driver.find_element(By.ID,"dependency_secretary_button").click()
        self.driver.find_element(By.ID,"add_button").click()
        
        Posicion = 1
        Text = ['salud', 'salud', 'MiPass2019', 'Mervin Alberto']

        while (Posicion <= 4):
            self.driver.find_element(By.XPATH, u"/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/form[1]/div" + "[" + str(Posicion) + "]" + "/div[1]/input[1]").send_keys(Text[Posicion-1])
            Posicion = Posicion + 1

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()