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
        paises[datos_dict[clave]['country'].upper()].append([datos_dict[clave]['country'].upper(), datos_dict[clave]['location'],datos_dict[clave]['url']])

# Para el ejercicio solo tiene en cuentan los paises que tienen al menos 4 sites de opendata en la lista
print '\nListado de paises disponibles:\n'
for clave in paises.keys():
    if len(paises[clave]) < 4:
        paises.pop(clave)
        continue
    print clave,

correcto = False
while not correcto:
    paiselegido = raw_input('\nElige un país de la lista:').upper()
    if paiselegido in paises:
        correcto = True

# p0 = min,min
# p1 = min,max
# p2 = max,min
# p3 = max,max

p0 = float(paises[paiselegido][1].split(','))
p0 = [p0[1],p0[0]]
p1 = paises[paiselegido][1].split(',')
p0 = [p0[1],p0[0]]
p2 = paises[paiselegido][1].split(',')
p0 = [p0[1],p0[0]]
p3 = paises[paiselegido][1].split(',')
p0 = [p0[1],p0[0]]
for site in paises[paiselegido]:
    if float(paises[paiselegido][1].split(',')[1]) < p0[0] and float(paises[paiselegido][1].split(',')[0]) < p0[1]:
        p0 = [float(paises[paiselegido][1].split(',')[1]),float(paises[paiselegido][1].split(',')[0]) < p0[1]]
    elif float(paises[paiselegido][1].split(',')[1]) < p0[0] and float(paises[paiselegido][1].split(',')[0]) < p0[1]:
        p0 = [float(paises[paiselegido][1].split(',')[1]),float(paises[paiselegido][1].split(',')[0]) < p0[1]]
