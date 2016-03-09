#!/usr/local/bin/env python2
# -*- coding: utf-8 -*-


from json import loads
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('./opendata.json') as archivo:
    datos = archivo.read()
datos_dict = loads(datos)

lista = ['','','']
with open('index.html', 'w') as f:
    for clave in datos_dict.keys():
        lista += ['<h1>%s</h1>\n' %(datos_dict[clave]['title'].strip())]
        lista += ['<p>%s</p>\n' %(datos_dict[clave]['description'].strip())]
        lista += ['<a href="%s">Información</a>\n' %(datos_dict[clave]['url'].strip())]
       
    f.writelines(lista)
