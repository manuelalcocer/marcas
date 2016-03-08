#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 1. Listar de los sites de opendata:
#	- Nombre
#	- Autor
#	- País
#	- Descripción

from json import loads
with open('./opendata.json') as archivo:
    datos = archivo.read()
