# -*- coding: utf-8 -*-

class Registro:
    
    img_logo_xpath = "//a[contains(@class,'Header__LogoContainer-nt28l4-2 lXGct')]"
    
    lbl_titulo_xpath = "//h2[@class='Type__TypeElement-sc-9snywk-0 hCTbot Header__Title-nt28l4-1 bkLUvq'][contains(.,'Regístrate gratis para escuchar')]"
    
    txt_correo_xpath = "//input[contains(@name,'email')]"
    
    txt_confirmarcorreo_xpath = "//input[contains(@name,'confirm')]"
   
    txt_contrasena_id = "password"
    
    btn_registrate_xpath = "//button[@type='submit'][contains(.,'Registrarte')]"