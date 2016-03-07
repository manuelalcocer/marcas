#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

## 2. Contar las ciudades de cada país, y mostrar la mas septentrional y meridional

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

for pais in raiz.iter('country'):
    for ciudad in pais.iter('city'):
        print ciudad.find('name').text.strip()
