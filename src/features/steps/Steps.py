# -*- coding: utf-8 -*-
from behave import *
import pytest
import unittest
from behave import *
from selenium.webdriver.common.keys import Keys
from functions.Functions import Functions as Selenium
from functions.Inicializar import Inicializar
use_step_matcher("re")

class StepsDefinitions():


    @given("Abrir la aplicacion")
    def step_impl(self):
        Selenium.page_has_loaded(self)
        Selenium.abrir_navegador(self)

    @given("Inicilizo la app en la URL (.*)")
    def step_impl(self, URL):
        Selenium.abrir_navegador(self, URL=URL)

    @given("Abro la app con el navegador (.*)")
    def step_impl(self, navegador):
        Selenium.abrir_navegador(self, navegador=navegador)

    @then("cierro la app")
    def step_impl(self):
        Selenium.tearDown(self)


    @step("Cargo el DOM de la App: (.*)")
    def step_impl(self, DOM):
        Selenium.get_json_file(self, DOM)


    @step("En el campo (.*) escribo (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.send_key_text(self, locator, text)


    @step("Capturo de pantalla: (.*)")
    def step_impl(self, descripcion):
        Selenium.captura(self, descripcion)


    @step("Tomar captura: (.*)")
    def step_impl(self, captura):
        Selenium.capturar_pantalla(self),


    @step("En el dropdowmn (.*) selecciono (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.select_by_text(self, locator, text)

    @step("En el combobox (.*) selecciono (.*)")
    def step_impl(self, locator, value):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_select_elements(self,locator).select_by_value(value)


    @step("me desplazo al frame: (.*)")
    def step_impl(self,frame):
        Selenium.switch_to_iframe(self, frame)


    @step("El dropdowm (.*) seleccion (.*)")
    def step_impl(self,locator, text):
        Selenium.select_by_text(self, locator, text)


    @step("En la caja de texto  (.*) escribo (.*)")
    def step_impl(self,locator, text ):
        Selenium.esperar_elemento(self, locator)
        Selenium.send_key_text(self, locator, text)


    @step("vuelvo al frame padre")
    def step_impl(self):
        Selenium.switch_to_parentFrame(self)


    @step("Selecciono  (.*)")
    def step_impl(self,locator):
        Selenium.get_elements(self,locator).click()


    @step("Cliqueo en texto: (.*)")
    def step_impl(self,Text):
        Selenium.get_elements(self, "text", MyTextElement=Text).click()


    @step("Hago scroll hacia el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.scroll_to(self, locator)


    @step("Esperar que finalice la carga")
    def step_impl(self):
        Selenium.page_has_loaded(self)