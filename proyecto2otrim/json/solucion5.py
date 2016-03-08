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
paises = {}
for clave in datos_dict.keys():
    if datos_dict[clave]['country'].upper() not in paises and 0 < len(datos_dict[clave]['country']) < 3:
        paises[datos_dict[clave]['country'].upper()] = []
    if 0 < len(datos_dict[clave]['country']) < 3 and len(datos_dict[clave]['location']) > 2:
        print 'lllll'
        paises[datos_dict[clave]['country'].upper()].append([datos_dict[clave]['country'].upper(), datos_dict[clave]['location'],datos_dict[clave]['url']])

print '\nListado de paises disponibles:\n'
for clave in paises.keys():
    print clave, paises[clave],

correcto = False
while not correcto:
    paiselegido = raw_input('\nElige un país de la lista:')
    if paiselegido.upper() in paises:
        correcto = True

# p0 = min,min
# p1 = min,max
# p2 = max,min
# p3 = max,max


