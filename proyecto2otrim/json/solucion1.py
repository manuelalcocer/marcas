#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 1. Lista de los sites de opendata:
#	- Nombre
#	- Autor
#	- País
#	- Descripción

from json import loads
with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)

for clave in datos_dict.keys():
    print '\n\nNombre: ', datos_dict[clave]['name']
    print '\tAutor: ', datos_dict[clave]['author']
    print '\tPaís: ', datos_dict[clave]['country']
    print '\tDescripción:', datos_dict[clave]['description']
