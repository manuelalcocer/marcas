#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# 4. Pedir una url y decir si está activa

from json import loads
with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)

encontrado = False
while not encontrado:
    url = raw_input('\n\nDime una url: ').lower()
    for clave in datos_dict.keys():
        if datos_dict[clave]['url'].lower().find(url):
            encontrado = True
            url = datos_dict[clave]['url']
            estado = datos_dict[clave]['status']
            if estado == 'active':
                estado = 'Activa'
            else:
                estado = 'Inactiva'
            break

print u'\nLa url %s está %s' %(url,estado)

