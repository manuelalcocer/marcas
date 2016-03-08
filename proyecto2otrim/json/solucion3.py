#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 3. Pedir un país, mostrar la mínima y máxima fecha de ingreso en la lista opendata (metadatacreated), pedir un intervalo válido, y mostrar los sites que cumplan con el requisito

from json import loads
from datetime import datetime

with open('./opendata.json') as archivo:
    datos = archivo.read()

datos_dict = loads(datos)

# formato de la fecha -->> "metadatacreated" : "2013-08-29T08:12:05.637Z"


