#!/usr/bin/env bash
# -*- coding: utf-8 -*-


# 4. Pedir un país y mostrar su capital, sus provincias, ciudades, y religiones.

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

paises = []
for pais in raiz.iter('country'):
    paises += [ pais.attrib['name'] ]

encontrado = False
while not encontrado:
    paispedido = raw_input('Dime un país: ')
    for pais in paises:
        if pais.lower == paispedido.lower:
            encontrado = True
            break
    if not encontrado:
        for pais in paises:
            if pais.lower.startswith(paispedido[0]):
                print pais

