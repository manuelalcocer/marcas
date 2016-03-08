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
    if 0 < len(datos_dict[clave]['country']) < 3 and len(datos_dict[clave]['location']) > 4:
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
puntos = [[],[],[],[]]
puntos[0] = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
puntos[0] = [puntos[0][1],puntos[0][0]]
puntos[1] = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
puntos[1] = [puntos[1][1],puntos[1][0]]
puntos[2] = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
puntos[2] = [puntos[2][1],puntos[2][0]]
puntos[3] = [ float(coordenada) for coordenada in paises[paiselegido][0][1].split(',') ]
puntos[3] = [puntos[3][1],puntos[3][0]]
for indice in xrange(len(paises[paiselegido])):
    if float(paises[paiselegido][indice][1].split(',')[1]) < puntos[0][0] and float(paises[paiselegido][indice][1].split(',')[0]) < puntos[0][1]:
        puntos[0] = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

    if float(paises[paiselegido][indice][1].split(',')[1]) > puntos[1][0] and float(paises[paiselegido][indice][1].split(',')[0]) < puntos[1][1]:
        puntos[1] = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

    if float(paises[paiselegido][indice][1].split(',')[1]) > puntos[2][0] and float(paises[paiselegido][indice][1].split(',')[0]) > puntos[2][1]:
        puntos[2] = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]

    if float(paises[paiselegido][indice][1].split(',')[1]) < puntos[3][0] and float(paises[paiselegido][indice][1].split(',')[0]) > puntos[3][1]:
        puntos[3] = [float(paises[paiselegido][indice][1].split(',')[1]),float(paises[paiselegido][indice][1].split(',')[0])]


# cálculo por determinante de Gauss
# Área = 1/2 * (det01 + det12 + det23 + det30)
# Area en km = Area * 111^2 km^2

# suma de determinantes
sumatorio = 0
for indice in xrange(len(puntos)):
    x1 = puntos[indice%4][0]
    y1 = puntos[indice%4][1]
    x2 = puntos[(indice+1)%4][0]
    y2 = puntos[(indice+1)%4][1]
    sumatorio += (x1 * y2 - x2 * y1)

area = sumatorio * 0.5
areakm2 = area*(3.1416*6371/180)**2
densidad = len(paises[paiselegido]) / areakm2 
print 'El area es que abarcan las sites es: %.2f km² y la densidad es: %.4f sites/km²' %(areakm2,densidad)





