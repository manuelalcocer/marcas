#!/usr/local/env python2
# -*- coding: utf-8 -*-

# 3. Mostrar los países con una densidad de población superior/inferior a una dada.

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

for pais in raiz.iter('country'):
    try:
        densidad = float(pais.attrib['population'])/float(pais.attrib['total_area'])
        try:
            if densidad > densidadmaxima:
                densidadmaxima = densidad
        except:
            densidadmaxima = densidad
        try:
            if densidad < densidadminima:
                densidadminima = densidad
        except:
            densidadminima = densidad
    except:
        # si no hay datos para calcular la densidad no se hace nada
        pass

print 'Densidad maxima: %.2f hab/km²' % densidadmaxima
print 'Densidad mínima: %.2f hab/km²' % densidadminima
densidadpedida = float(raw_input('Dime una densidad comprendida entre esos valores: '))
while not densidadminima < densidadpedida < densidadmaxima:
    densidad = float(raw_input('Dime una densidad comprendida entre esos valores: '))

for pais in raiz.iter('country'):
    try:
        densidad = round(float(pais.attrib['population'])/float(pais.attrib['total_area']),2)
    except:
        pass
    if densidadpedida < densidad:
        print '%.2f Menor: %s tiene %.2f hab/km²' %(densidadpedida,pais.attrib['name'],densidad)
for pais in raiz.iter('country'):
    try:
        densidad = round(float(pais.attrib['population'])/float(pais.attrib['total_area']),2)
    except:
        pass
    if densidadpedida > densidad:
        print '%.2f Mayor: %s tiene %.2f hab/km²' %(densidadpedida,pais.attrib['name'],densidad)
