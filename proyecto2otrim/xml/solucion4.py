#!/usr/bin/env bash
# -*- coding: utf-8 -*-


# 4. Pedir un país y mostrar su capital, sus provincias, ciudades, y religiones.

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

capital = pais.attrib['capital']
ciudades = []
for ciudad in pais.iter('city'):
    if ciudad.attrib['id'] == capital:
        capital = ciudad.find('name').text.strip()
    ciudades += [ ciudad.find('name').text.strip() ]
print '\nCapital: %s' % capital
print '\nCiudades:'
print '========='
for ciudad in ciudades:
    print ciudad

provincias = []
for provincia in pais.iter('province'):
    provincias += [ provincia.attrib['name'] ]

if len(provincias) > 0:
    print '\nListado de provincias:'
    print '======================'
    for provincia in provincias:
        print provincia
else:
    print '\nNo hay provincias'

religiones = []
for religion in pais.iter('religions'):
    religiones += [ religion.text.strip() ]
if len(religiones) > 0:
    print '\nListado de religiones:'
    print '======================'
    for religion in religiones:
        print religion
