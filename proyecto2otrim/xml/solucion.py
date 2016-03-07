#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
1. Listar la inforación de los países ordenadas por continentes.
    - País
    - Población
'''

from lxml import etree

raiz = etree.parse('./mondial-3.0.xml').getroot()

# listado de continentes
continentes = {}
for continente in raiz.iter('continent'):
    continentes[continente.attrib['id']] = continente.attrib['name']

# listado de paises
# el continente al que pertenece está en: <country/encompased/continent>
for idcont,nomcont in continentes.iteritems():
    print 'Continente: %s' % nomcont
    raw_input('Pulsar enter para comenzar listado..')
    for pais in raiz.iter('country'):
        continenteid = pais.find('encompassed').attrib['continent']
        nombrepais = pais.attrib['name']
        if idcont == continenteid:
            print 'Nombre continente: %s' % nombrepais
