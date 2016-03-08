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
