#!/usr/local/env python2
# -*- coding: utf-8 -*-

# 3. Mostrar los países con una densidad de población superior/inferior a una dada.

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

for pais in raiz.iter('country'):
    try:
        densidad = round(float(pais.attrib['population'])/float(pais.attrib['total_area']),2)
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

print 'Densidad maxima: %f' % densidadmaxima
print 'Densidad mínima: %f' % densidadminima
densidad = float(raw_input('Dime una densidad comprendida entre esos valores: '))
while densidadminima < densidad < densidadmaxima:
    densidad = float(raw_input('Dime una densidad comprendida entre esos valores: '))


