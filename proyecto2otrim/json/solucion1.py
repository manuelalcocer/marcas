#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from json import loads
with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)
print datos
