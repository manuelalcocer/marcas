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
# p1 = max,min
# p2 = max,max
# p3 = min,max
print paises[paiselegido][0][1]
raw_input('lllll')
p0 = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
p0 = [p0[1],p0[0]]
p1 = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
p1 = [p0[1],p0[0]]
p2 = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
p2 = [p0[1],p0[0]]
p3 = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
p3 = [p0[1],p0[0]]
for indice in xrange(len(paises[paiselegido])):
    print indice
    if float(paises[paiselegido][indice][1].split(',')[1]) < p0[0] and float(paises[paiselegido][indice][1].split(',')[0]) < p0[1]:
        p0 = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

    if float(paises[paiselegido][indice][1].split(',')[1]) > p1[0] and float(paises[paiselegido][indice][1].split(',')[0]) < p1[1]:
        p1 = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

    if float(paises[paiselegido][indice][1].split(',')[1]) > p2[0] and float(paises[paiselegido][indice][1].split(',')[0]) > p2[1]:
        p2 = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

    if float(paises[paiselegido][indice][1].split(',')[1]) < p3[0] and float(paises[paiselegido][indice][1].split(',')[0]) > p3[1]:
        p3 = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

print p0
print p1
print p2
print p3

# cálculo por determinante de Gauss
# Área = 1/2 * (det01 + det12 + det23 + det30)



