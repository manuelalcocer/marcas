#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

encontrado = False
while not encontrado:
    paispedido = raw_input('Dime un país: ')
    for pais in raiz.iter('country'):
        if pais.attrib['name'].lower() == paispedido.lower():
            encontrado = True
            paispedido = pais
            break
    if not encontrado:
        for pais in raiz.iter('country'):
            if pais.attrib['name'].lower().startswith(paispedido[0]):
                print pais.attrib['name']

ciudades = []
for ciudad in pais.iter('city'):
    ciudades += [ ciudad ]

ciudades_a = ciudades[:]
ciudades_b = ciudades[:]
# distancia entre 2 ciudades = raiz(diff_lat² + diff_lon²)
distancia = 0
for ciudad_a in ciudades_a:
    for ciudad_b in ciudades_b:
        try:
            diferencia_lats = float(ciudad_a.attrib['latitude']) - float(ciudad_b.attrib['latitude'])**2
            diferencia_longs = float(ciudad_a.attrib['longitude']) - float(ciudad_b.attrib['longitude'])**2
            calculo_modulo = (diferencia_lats**2 + diferencia_longs**2)**0.5 
            if  calculo_modulo > distancia:
                pareja_de_ciudades = [ ciudad_a.find('name').text.strip(), ciudad_b.find('name').text.strip() ]
                distancia = calculo_modulo
        except:
            pass

print '\nCiudades más alejadas: '
print '======================'
print pareja_de_ciudades[0], '-', pareja_de_ciudades[1]




