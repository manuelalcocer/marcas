#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

## 2. Contar las ciudades de cada país, y mostrar la mas septentrional y meridional

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

for pais in raiz.iter('country'):
    contador = 0
    septentrional = [-90, '']
    meridional = [90, '']
    for ciudad in pais.iter('city'):
        try:
            if ciudad.attrib['country'] == pais.attrib['id']:
                contador += 1
                try:
                    if float(ciudad.attrib['latitude']) > septentrional[0]:
                        septentrional = [round(float(ciudad.attrib['latitude']),2),ciudad.find('name').text.strip()]
                    if float(ciudad.attrib['latitude']) < meridional[0]:
                        meridional = [round(float(ciudad.attrib['latitude']),2),ciudad.find('name').text.strip()]
                except:
                    pass
        except:
            pass
    if len(septentrional[1]) > 0:
        sept = '%s %s' % (str(septentrional[0]),septentrional[1])
    else:
        sept = 'No disponible'
    if len(meridional[1]) > 0:
        med = '%s %s' % (str(meridional[0]), meridional[1])
    else:
        med = 'No disponible'
    print "Pais: %s , Número de ciudades: %d" %(pais.find('name').text.strip(), contador)
    print 'Más septentrional: %s' % sept
    print 'Más meridional: %s' % med
