#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 3. Pedir un país, mostrar la mínima y máxima fecha de ingreso en la lista opendata (metadatacreated), pedir un intervalo válido, y mostrar los sites que cumplan con el requisito

from json import loads
from datetime import datetime

with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)

# formato de la fecha -->> "metadatacreated" : "2013-08-29T08:12:05.637Z"
paises = []
for clave in datos_dict.keys():
    separados = datos_dict[clave]['metadatacreated'].split('T')
    if len(separados[0]) > 0:
        fecha = separados[0].split('-')
        hora = separados[1].split('.')[0].split(':')
        paises += [ [datos_dict[clave]['country'], datetime(int(fecha[0]),int(fecha[1]),int(fecha[2]),int(hora[0]),int(hora[1]))] ]

maximo = [ paises[0] ]
minimo = [ paises[0] ]
for pais in paises:
    if pais[1] > maximo[1]:
        maximo = pais
    if pais[1] < minimo[1]:
        minimo = pais
print maximo
print minimo
