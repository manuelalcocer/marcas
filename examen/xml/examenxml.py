#!/usr/bin/env/bash
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
lista = [ '<h1>%s\n</h1>' % paispedido.attrib['name'] ]

if len(paispedido.find('province')) > 0:
    for provincia in paispedido.iter('province'):
        for ciudad in provincia.iter('name'):
            lista += [ '<p>%s / %s</p>\n' %(provincia.attrib['name'],ciudad.text.strip()) ]
else:
    for ciudad in paispedido.iter('name'):
        lista += [ '<p>%s</p>\n' % ciudad.text ]

with open('index.html', 'w') as f:
    f.writelines(lista)
