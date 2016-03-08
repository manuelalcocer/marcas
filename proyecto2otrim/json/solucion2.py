#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 2. Contar los sites de opendata de un país cualquiera, por ejemplo, Reino Unido, crear un ranking, y decir en qué posición se encuentra.

from json import loads

with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)

contadores = {}
for clave in datos_dict.keys():
    if datos_dict[clave]['country'].upper() not in contadores:
        contadores[datos_dict[clave]['country'].upper()] = 1
    else:
        contadores[datos_dict[clave]['country'].upper()] += 1
print contadores
        
