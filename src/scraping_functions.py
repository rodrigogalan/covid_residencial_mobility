#Se importan los paquetes necesarios
import pandas as pd
import numpy as np
import re
import time
import requests as req
from bs4 import BeautifulSoup as bs
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#driver configuration
opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
#opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
#opciones.add_extension('driver_folder/adblock.crx')       # adblocker
opciones.add_argument('--incognito')
opciones.add_experimental_option("detach", True)
path = "/mnt/d/Google Drive/Iron hack/Instalaciones/chromedriver.exe"


def time_from_1970(dias):
    '''Esta función da el número de segundos desde enero de 1970 hasta una fecha introducida'''
    datetime_object = datetime(2019, 8, 8)
    datetime_object = datetime.now()+timedelta(-dias)
    return int(datetime_object.timestamp())


def scroll_all_down(driver, pause_time=0.5):
    '''Función para hacer scroll hasta el final de la página'''
    
    #Lo primero es saber la altura actual
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #Ahora se itera hasta que al hacer scroll la altura no cambie
    while True:
        # Se baja hasta el fondo de la página
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

        # Se da un tiempo para que la página carge
        time.sleep(pause_time)

        # Se comprueba si la altura ha disminuido y en caso contrario se detiene la función
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scroll_to_element(driver, xpath,pause_time=0.5):
    '''Dado un xpath hace scroll hasta que el elemento se vea'''
    
    #Lo primero es saber la altura actual
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #Se fija el elemento que se quiere visualizar
    element =driver.find_element_by_xpath(xpath)
    
    #Ahora se itera hasta que la altura no cambie
    while True:
        #Se baja hasta que se vea el elemento
        element.location_once_scrolled_into_view
        
        # Se da un tiempo para que la página carge
        time.sleep(pause_time)

        # Se comprueba si la altura ha disminuido y en caso contrario se detiene la función
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def yahoo_finance(company, days_start, days_end, freq, option):
    '''Función para el screapeo de yahoo finance'''
    
    # Se declara la URL
    URL='https://finance.yahoo.com/quote/'
    scrape_url=''.join([
        URL,
        f'{company}/', #compañia a scrapear
        f'history?period1={time_from_1970(days_start)}', #inicio del periodo de tiempo
        f'&period2={time_from_1970(days_end)}', #fin del periodo de tiempo
        f'&interval={freq}d', #intervalo de tiempo entre valores en dias
        f'&filter={option}', #datos a scrapear
                            # Las opciones son: Chart, Conversations, Statistics, Historical Data, 
                            # Profile, Financials, Analysis, Options, Holders, Sustainability
        f'&frequency={freq}d', #intervalo de tiempo entre valores en dias
        f'&includeAdjustedClose=true',
        f'&guccounter=1'
    ])
   
    # Se llama al webdriver
    driver=webdriver.Chrome(path,options=opciones)
    driver.get(scrape_url)
    time.sleep(1)

    # Se quita el aviso de cookies
    cookies = driver.find_element_by_css_selector("#consent-page > div > div > div > form > div.wizard-body > div.actions.couple > button");
    cookies.click()
    time.sleep(1)

    try:
        # Se pasa el overlayer
        boton_here = driver.find_element_by_css_selector("#loaderContainer > p > a")
        boton_here.click()
        time.sleep(3)
    except:
        pass

    # Se carga toda la página
    scroll_all_down(driver)

    # Se copian los valores
    tabla = driver.find_element_by_css_selector(
        "#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody").text
    
    # Se cierra la pestaña de Chrome
    driver.close()

    return tabla