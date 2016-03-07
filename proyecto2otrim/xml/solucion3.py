#!/usr/local/env python2
# -*- coding: utf-8 -*-

# 3. Mostrar los países con una densidad de población superior/inferior a una dada.

from lxml import etree

densidadmaxima = 0
densidadminima = 0

raiz = etree.parse('./mondial-3.0.xml').getroot()

for pais in raiz.iter('country'):
    try:
        densidad = round(float(pais.attrib['population'])/float(pais.attrib['total_area']),2)
    except:
        densidad = 0
    print densidad
