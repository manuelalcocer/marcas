#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 5. Pedir un país medir el área máxima que abarcan sus sites opendata y la densidad de sites que alberga.
'''
    Radio terrestre = Rt = 6371 km
    grados a radianes => radianes = grados * pi / 180
    cuerda de un circulo => l = rad * radio
    Suponiendo esférica la tierra: 1 grado (latitud o longitud ) = pi * Rt / 180 ~ 111 km
'''

from json import loads
with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)
paises = []
for clave in datos_dict.keys():
    if 0 < len(datos_dict[clave]['country']) < 3:
        paises += [ datos_dict[clave]['country'] ]

print '\nListado de paises disponibles:\n'
for pais in paises:
    print pais,

