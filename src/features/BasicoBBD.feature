# Created by Luisa Avila at 10/02/2021
@Selenium
Feature: Funciones basicas de selenium con BDD

@Navegador
  Scenario: Abrir el navegador
    Given Abrir la aplicacion
    Then cierro la app

@Navegador
  Scenario: Abrir url
  Given Inicilizo la app en la URL https://www.toolsqa.com/cucumber/behavior-driven-development/

@Navegador
  Scenario: Abrir con Navegador
    Given Abro la app con el navegador FIREFOX
    Then cierro la app

  @DOM
  Scenario: Setear el DOM y trabajar con el
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify
    And En el campo txt_correo escribo luisaavila1993@gmail.com
    Then cierro la app

  @Captura
  Scenario: Tomar capturas
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify
    And En el campo txt_correo escribo luisaavila1993@gmail.com
    And Capturo de pantalla: Emailspotify
    And Tomar captura: Test003
    Then cierro la app

@Textos
  Scenario: Clic dropdowmn y textbox
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify
    And En el campo txt_correo escribo luisaavila1993@gmail.com
    And En el dropdowmn dpd_mes selecciono Octubre
    And En el combobox dpd_mes selecciono 08
    Then cierro la app

  @Frames
  Scenario: Frames y ventanas
    Given Inicilizo la app en la URL https://chercher.tech/practice/frames-example-selenium-webdriver
    And Cargo el DOM de la App: iframe
    And me desplazo al frame: fra_frame2
    And El dropdowm dpd_animales seleccion Avatar
    And vuelvo al frame padre
    And me desplazo al frame: fra_frame1
    And En la caja de texto  txt_topic escribo Hola soy Luisa
    And me desplazo al frame: fra_frame3
    And Selecciono  chk_options
    And Tomar captura: Test004
    Then cierro la app

  @Textos
  Scenario: Buscar text element
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify
    And Hago scroll hacia el elemento: YaCuenta
    And Cliqueo en texto: Inicia sesión
    And Esperar que finalice la carga
    Then cierro la app