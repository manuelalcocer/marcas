#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 3. Pedir un país, mostrar la mínima y máxima fecha de ingreso en la lista opendata (metadatacreated), pedir un intervalo válido, y mostrar los sites que cumplan con el requisito

from json import loads

with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)

