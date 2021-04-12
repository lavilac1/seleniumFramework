# -*- coding: utf-8 -*-
#En function se crean las funciones para ser utilizadas en cad auno de los casos de pruebas, se debe importar el inicializar
'''
Created on 22/01/2021

@author: Luisa Avila
'''
import allure
import openpyxl
import pyodbc as pyodbc
from functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver_manager.firefox import GeckoDriverManager
import pytest
import json
import time
import datetime
import re
import os
from idlelib.calltip import get_entity
Scenario = {}
diaGlobal= time.strftime(Inicializar.DateFormat)  # formato aaaa/mm/dd
horaGlobal = time.strftime(Inicializar.HourFormat)  # formato 24 houras
Scenario = {}
diaGlobal= time.strftime(Inicializar.DateFormat)  # formato aaaa/mm/dd
horaGlobal = time.strftime(Inicializar.HourFormat)  # formato 24 houras


class Functions(Inicializar):
    
    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio Base: " + Inicializar.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("---------------")
        
        if navegador == ("IExplorer"):
            caps = DesiredCapabilities.INTERNETEXPLORER.copy()
            caps["platform"] = "WINDOWS"
            caps["browserName"] = "internet explorer"
            caps["ignoreZoomSetting"] = True
            caps["requireWindowFocus"] = True
            caps["nativeEvents"] = True
            self.driver = webdriver.Ie(Inicializar.basedir + "\\drivers\\IEDriverServer.exe", caps)
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            print(self.ventanas)
            return self.driver
        
        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            ## self.driver = webdriver.Chrome(chrome_options=options, executable_path=Inicializar.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(5)
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}##Almacenar el valor de la pesta�a principal
            return self.driver
        
        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            ## self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            return self.driver
        
    def tearDown(self):
        print("Se cerrara el DRIVER")
        self.driver.quit()
        
        
##########################################################################
##############       -=_lOCATORS   HANDLE _=-              ###############
##############################SIN JSON############################################

    def xpath_element(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements

    def _xpath_element(self, XPATH):
        try:
            wait = WebDriverWait(self.driver, 20) #espere 20 segundos que el elemento se haga presente
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))#espera si el elemento esta presente en todo el DOM
            elements = self.driver.find_element_by_xpath(XPATH)
            print(u"Esperar_Elemento: Se visualizo el elemento " + XPATH)
            return True

        except TimeoutException: #Excepcion del tiempo de espera
            print(u"Esperar_Elemento: No presente " + XPATH)
            Functions.tearDown(self)
        except NoSuchElementException:# Excepcion el elemento no esta en el DOM
            print(u"Esperar_Elemento: No presente " + XPATH)
            Functions.tearDown(self)

    def id_element(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print("Xpath_Elements: Se interactuo con el elemento " + ID)
        return elements

    def _id_element(self, ID):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.ID, ID)))
            elements = self.driver.find_element_by_id(ID)
            print(u"Esperar_Elemento: Se visualizo el elemento " + ID)
            return elements

        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + ID)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_Elemento: No presente " + ID)
            Functions.tearDown(self)

    def name_element(self, name):
        elements = self.driver.find_element_by_name(name)
        print("Xpath_Elements: Se interactuo con el elemento " + name)
        return elements

    def _name_element(self, name):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.ID, name)))
            elements = self.driver.find_element_by_id(name)
            print(u"Esperar_Elemento: Se visualizo el elemento " + name)
            return elements

        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + name)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_Elemento: No presente " + name)
            Functions.tearDown(self)

##########################################################################
    ##############       -=_JSON     HANDLE _=-              #################
    ##########################################################################

    def get_json_file(self, file):#cargar el archivo
        json_path = "C:\\seleniumFramework\\src\\pages\\"+ file + '.json'
            ##Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)
            Functions.tearDown(self)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True

            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                # self.driver.close()
                Functions.tearDown(self)
                return None

    def get_elements(self, entity, MyTextElement = None):#obtener un elemento u objeto
        Get_Entity = Functions.get_entity(self, entity)#a una variable le doy las entidades

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":#verifico si la variable globarl getfielby es id
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":#verifico si la variable globarl getfielby es name
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":#verifico si la variable globarl getfielby es xpath
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print (self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":#verifico si la variable globarl getfielby es link
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":#verifico si la variable globarl getfielby es css
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
                
    def get_text(self, entity, MyTextElement = None):#obtener un elemento u objeto tipo texto
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print (self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_text: " + self.json_ValueToFind)
                print("Text Value : " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def get_select_elements(self, entity):#obtener un elemento u objeto tipo drop down
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element_by_id(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element_by_name(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element_by_xpath(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                print("get_select_elements: " + self.json_ValueToFind)
                return select

            # USO

            #       select by visible text  #       select.select_by_visible_text('Banana')

            #       select by value  #       select.select_by_value('1')

            except NoSuchElementException:
                print("No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)           
                   
    
    def esperar_elemento(self, locator, MyTextElement=None):#esperar que el elemento se haga presente
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)
            except NoSuchElementException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)
                
                
##########################################################################
    ##############       -=_TEXTBOX & COMBO HANDLE _=-   #################
    ##########################################################################

    def select_by_text(self, entity, text):#enviarle el texto que se quiere seleccionar en un combo
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

    def send_key_text(self, entity, text):#enviar texto a una caja de texto
        Functions.get_elements(self, entity).clear()
        Functions.get_elements(self, entity).send_keys(text)

    ##crear step
    def send_especific_keys(self, element, key):
        if key == 'Enter':
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        if key == 'Tab':
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        if key == 'Space':
            Functions.get_elements(self, element).send_keys(Keys.SPACE)
        time.sleep(3)


    def switch_to_iframe(self, Locator):#pasarse entre iframe
        iframe = Functions.get_elements(self, Locator)
        self.driver.switch_to.frame(iframe)
        print (f"Se realizo el switch a {Locator}")

    def switch_to_parentFrame(self):# volver al iframe principal
        self.driver.switch_to.parent_frame()
        
    def switch_to_windows_name(self, ventana): #pasarse entre ventanas
        if ventana in self.ventanas:
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print ("volviendo a " + ventana + " : " + self.ventanas[ventana])
        else:
            self.nWindows = len(self.driver.window_handles) - 1
            self.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print ("Estas en " + ventana + " : " + self.ventanas[ventana])
            Functions.page_has_loaded(self)
        

#####################   -=_JAVASCRIPT_=-   ###############################
    #####################################################################
    ######################################################################

    def new_window(self, URL):# abrir una nueva ventana
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    def page_has_loaded(self):#Verificar que el DOM este cargado por completo
        driver = self.driver
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"

    def scroll_to(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

            except TimeoutException:
                print(u"scroll_to: No presente " + locator)
                Functions.tearDown(self)

    def js_clic(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        Functions.esperar_elemento(self, locator, MyTextElement)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    localizador = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

            except TimeoutException:
                print(u"js_clic: No presente " + locator)
                Functions.tearDown(self)

##############   -=_Wait Elements_=-   #############################
    ##########################################################################
    def esperar(self, timeLoad=8):
        print ("Esperar: Inicia ("+str(timeLoad)+")")
        try:
                totalWait = 0
                while (totalWait < timeLoad):
                    #print("Cargando ... intento: " + str(totalWait))
                    time.sleep(1)
                    totalWait = totalWait + 1
        finally:
            print ("Esperar: Carga Finalizada ... ")
            
            
    def alert_windows(self, accept ="accept"):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.alert_is_present(), print("Esperando alerta..."))

            alert = self.driver.switch_to.alert

            print (alert.text)

            if accept.lower()== "accept":
                alert.accept()
                print ("Click in Accept")
            else:
                alert.dismiss()
                print ("Click in Dismiss")

        except NoAlertPresentException:
            print('Alerta no presente')
        except NoSuchWindowException:
            print('Alerta no presente')
        except TimeoutException:
            print('Alerta no presente')
            
    ##########################################################################
#################   -=_VERIFICACION _=-                ###################
##########################################################################

    def check_element(self, locator):  # devuelve true o false verificaciones
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.LINK, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False

    def assert_text(self, locator, TEXTO):

        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            if self.json_GetFieldBy.lower() == "id":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_id(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "name":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_name(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "xpath":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_xpath(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "link":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_partial_link_text(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "css":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_css_selector(self.json_ValueToFind).text

        print("Verificar Texto: el valor mostrado en: " + locator + " es: " + ObjText + " el esperado es: " + TEXTO)
        assert TEXTO == ObjText, "Los valores comparados no coinciden"

##########################################################################
    #################   -=DATA DE ESCENARIO=-                ################
    ##########################################################################

    def create_variable_scenary(self, key, value):
        Scenario[key] = value
        print(Scenario)
        print ("Se almaceno la key " + key + " : " + value)

    def save_variable_scenary(self, element, variable):#almacenar en un diccionario el valor d ela variable
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print ("Se almaceno el valor " + variable + " : " + Scenario[variable])

    def get_variable_scenary(self, variable):#extraer el valor de una variable
        self.variable = Scenario[variable]
        print(f"get_variable_scenary: {self.variable}")
        return self.variable

    def compare_with_variable_scenary(self, element, variable): #comparar el valor de dos vairables
        variable_scenary = str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print (_exist)
        print (f'Comparando los valores... verificando que si {variable_scenary} esta presente en {element_text} : {_exist}')
        assert _exist == True, f'{variable_scenary} != {element_text}'

    def textDateEnvironmentReplace(self, text):#escribir fecha en un campo de texto
        if text == 'today':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'Last Month':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormat)

        return text
    
    #### Excel
    def leer_celda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)#abrir el archivo de excel definido en el inicializar
        sheet = wb["DataTest"]#ubicarse en la pesta�a
        valor = str(sheet[celda].value)#a la variable valor asignarle la hoja y la celda
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print(u"El valor de la celda es: " + valor)
        print(u"------------------------------------")
        return valor

    def escribir_celda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda] = valor
        wb.save(Inicializar.Excel)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print(u"Se escribio en la celda " + str(celda) + u" el valor: " + str(valor))
        print(u"------------------------------------")

    
                    
        ##############   -=_CAPTURA DE PANTALLA_=-   #############################
    ##########################################################################

    def hora_Actual(self):
        self.hora = time.strftime(Inicializar.HourFormat)  # formato 24 horas
        return self.hora

    def crear_path(self):
        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd
        GeneralPath = Inicializar.Path_Evidencias#Trae la ruta base donde se van a guardar las capturas
        DriverTest = Inicializar.NAVEGADOR#Trae el navegador con el que se hizo la prueba
        TestCase = self.__class__.__name__#Trae el nombre d ela clase con el que se esta corriendo la prueba
        horaAct = horaGlobal#Trae la hora global
        x = re.search("Context", TestCase)#cuando son por comportamiento, pregunta si tiene context en el titulo de la prueba
        if (x):
            path = f"{GeneralPath}/{dia}/{DriverTest}/{horaAct}/"
        else:
            path = f"{GeneralPath}/{dia}/{TestCase}/{DriverTest}/{horaAct}/"#genera la ruta

        if not os.path.exists(path):  # si no existe el directorio lo crea
            os.makedirs(path)

        return path

    def capturar_pantalla(self, TestCase= "Captura"):
        PATH = Functions.crear_path(self)
        img = f'{PATH}/TestCase_(' + str(Functions.hora_Actual(self)) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def captura(self, Descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), Descripcion, attachment_type=allure.attachment_type.PNG)
        

    ##############   -=_VERIFICAR LA PRESENCIA DE ELEMENTOS_=-   #############################
    ##########################################################################
   

    def validar_elemento(self, locator):
        Get_Entity  = Functions.get_entity(self, locator)
        
        TIME_OUT = 15
        
        if Get_Entity is None:
            return print ("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until (EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until (EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar Elemento: Se visualizo el elemento " + locator)
                    return True
                
                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until (EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until (EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until (EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar Elemento: Se visualizo el elemento " + locator)
                    return True
                
            except TimeoutException:
                print (u"Assert xpath: Elemento No presente " + locator)
                return False
        