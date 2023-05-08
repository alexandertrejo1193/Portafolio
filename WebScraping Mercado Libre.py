#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:11:59 2023

@author: alexandertrejo
"""

def webscrapingmercadolibre(liga,nombredoc):
    import requests
    from bs4 import BeautifulSoup
    from lxml import etree
    import pandas as pd
    import datetime

    #conseguir links
    r=requests.get(liga)
    soup= BeautifulSoup(r.content,'html.parser')
    urls=soup.find_all('a',attrs={'class':'ui-search-item_group_element ui-search-link'})
    urls=[i.get('href') for i in urls]
    dom=etree.HTML(str(soup))
    siguiente= dom.xpath('//div[@class="ui-search-pagination"]/ul/li[contains(@class,"--next")]/a')[0].get('href')
    ini= soup.find('span',attrs={"class":"andes-pagination__link"}).text
    ini=int(ini)
    can= soup.find('li',attrs={"class":"andes-pagination__page-count"}).text.split(" ")[1]
    can=int(can)
    lista_urls = []
    siguiente= liga
    while True:
        r =requests.get(siguiente)
        if r.status_code==200:
            soup= BeautifulSoup(r.content,'html.parser')
            #URL
            urls=soup.find_all('a',attrs={'class':'ui-search-item_group_element ui-search-link'})
            urls=[i.get('href') for i in urls]
            lista_urls.extend(urls)
            dom=etree.HTML(str(soup))
            ini= soup.find('span',attrs={"class":"andes-pagination__link"}).text
            ini=int(ini)
            can= soup.find('li',attrs={"class":"andes-pagination__page-count"}).text.split(" ")[1]
            can=int(can)
            print(ini,can)
        else:
            break
        if ini==can:
            break
        siguiente=dom.xpath('//div[@class="ui-search-pagination"]/ul/li[contains(@class,"--next")]/a')[0].get('href')
    print(len(lista_urls))
    #termina conseguir links  

    #empieza abrir paginas
    lista_precio = []
    lista_titulo = []
    lista_descripcion= []
    lista_vendidos= []
    lista_color= []
    lista_marca= []
    lista_posicionmasvendido= []
    lista_numop= []
    list123=[]
    list_disponible=[]
    list_vendedor=[]
    list_vendidosVend=[]
    for url in lista_urls:
        r =requests.get(url)
        if r.status_code==200:
            soup= BeautifulSoup(r.content,'html.parser')
            #precio
            titulo=soup.find('h1',attrs={'class':'ui-pdp-title'})
            precio=soup.find('span',attrs={'class':'andes-money-amount__fraction'})
            #toma primer precio
            descripcion=soup.find('p',attrs={'class':'ui-pdp-description__content'})
            list1 =[]
            if len(descripcion)>1:
                for i in descripcion:
                    if i:
                        list1.append(i.text.strip())
                    descripcion=list1
                    descripcion= ",".join(descripcion)
            if soup.find('span',attrs={'class':'ui-pdp-subtitle'}) == None:
                vendidos= [0]
            else:
                vendidos=soup.find('span',attrs={'class':'ui-pdp-subtitle'}).text
            if soup.find('span',attrs={'class':'ui-pdp-dropdown-selector__item--label-small ui-pdp-color--BLACK'}) == None:
                color= [0]
            else:
                color=soup.find('span',attrs={'class':'ui-pdp-dropdown-selector__item--label-small ui-pdp-color--BLACK'})
            if soup.find('span',attrs={'class':'ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--BOLD'}) == None:
                marca= [0]
            else:
                marca=soup.find_all('p',attrs={'class':'ui-pdp-family--REGULAR ui-pdp-list__text'})
                list2 =[]
                if len(marca)>1:
                    for i in marca:
                        if i:
                            list2.append(i.text.strip())
                        marca=list2
                        marca= ",".join(marca)
                      
            if len(soup.find_all('a',attrs={'class':'ui-pdp-promotions-pill-label__target'}))<2:
                posicionmasvendido= [0]
            else:
                posicionmasvendido=soup.find_all('a',attrs={'class':'ui-pdp-promotions-pill-label__target'})[1]
            if  soup.find('span',attrs={'class':'ui-pdp-review__amount'})   == None:
                numop= [0]
            else:
                numop=soup.find('span',attrs={'class':'ui-pdp-review__amount'})
            if  soup.find('span',attrs={'class':'ui-pdp-buybox_quantity_available'})  == None:
                disponible= [0]
            else:
                disponible=soup.find('span',attrs={'class':'ui-pdp-buybox_quantity_available'})
            if  soup.find('strong',attrs={'class':'ui-pdp-seller__sales-description'})  == None:
                vendidosVend= [0]
            else:
                vendidosVend=soup.find('strong',attrs={'class':'ui-pdp-seller__sales-description'}).text
                
            if soup.find('a',attrs={'class':'ui-pdp-media_action ui-box-component_action'})== None:
                vendedor=0
            else:
                
                url1=soup.find('a',attrs={'class':'ui-pdp-media_action ui-box-component_action'})
                url1=url1.get('href')
                r1 =requests.get(url1)
                if r1.status_code==200:
                    soup1= BeautifulSoup(r1.content,'html.parser')
                    if soup1.find('h3',attrs={'id':'store-info__name'})== None:
                        if soup1.find('h3',attrs={'id':'brand'})==None:
                            vendedor=0
                        else:
                           vendedor=soup1.find('h3',attrs={'id':'brand'}).text 
                    else:
                        vendedor=soup1.find('h3',attrs={'id':'store-info__name'}).text
        #marca tiene que arreglar la ruta o jalar todos .find_all y ponerle de nombre otros
        else:
            break
        list_vendedor.append(vendedor)
        lista_precio.extend(precio)
        lista_titulo.extend(titulo)
        lista_descripcion.append(descripcion)
        lista_vendidos.append(vendidos)
        lista_color.extend(color)
        lista_marca.append(marca)
        lista_posicionmasvendido.extend(posicionmasvendido)
        lista_numop.extend(numop)
        list_disponible.extend(disponible)
        list_vendidosVend.append(vendidosVend)
        print(len(list_disponible),len(lista_urls))
    #termina de abrir paginas
    for i in range(len(lista_numop)):
        ahora=datetime.datetime.now()
        fecha=ahora.date()
        list123.append(fecha)
    print(len(lista_precio),len(lista_titulo),len(lista_descripcion),len(lista_vendidos),len(lista_color),len(lista_marca),len(lista_posicionmasvendido),len(lista_numop),len(list_vendedor),len(list_vendidosVend))   
    datos=pd.read_csv(nombredoc+'.csv',header=0)
    df1=pd.DataFrame(datos)
    print(df1.shape)
    #hace un dataframe
    df= pd.DataFrame({'Fecha':list123,'link':lista_urls,'Titulo':lista_titulo,'Precio':lista_precio,'Vendidos':lista_vendidos,
                      "Color":lista_color,"Otros":lista_marca,'Descripcion':lista_descripcion
                      ,'Posicion mas vendido':lista_posicionmasvendido,'Disponibilidad':list_disponible,'VendidosVend':list_vendidosVend,'Vendedor':list_vendedor})
    #Hace el archivo
    df=df1.append(df,ignore_index=True)
    df.to_csv(nombredoc+'.csv',index=False) 
    
webscrapingmercadolibre('https://listado.mercadolibre.com.mx/delineador-retractil#D[A:delineador%20retractil]','delineador_retractil')
webscrapingmercadolibre('https://listado.mercadolibre.com.mx/lapiz-delineador#D[A:lapiz%20delineador]','delineador_lapiz')
webscrapingmercadolibre('https://listado.mercadolibre.com.mx/delineador-liquido#D[A:delineador%20liquido]','delineador_liquido')