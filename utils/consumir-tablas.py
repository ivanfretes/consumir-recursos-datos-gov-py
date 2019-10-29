#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:44:32 2019

@author: Ivan Fretes
"""

import json
import requests

base_url = "https://www.datos.gov.py/api/action/datastore_search_sql"
tablas_list = [];

def consultar_tabla_json(tabla_nombre):    
    if tabla_nombre:
        querystring = { "sql":"SELECT * FROM \"{}\" ;".format(tabla_nombre) }
        headers = {
            'cache-control': "no-cache",
        }
        response = requests.request("GET", base_url , data="", headers=headers, params=querystring)
        parse_json = json.loads(response.text)
        return json.dumps(parse_json, indent = 4, sort_keys=True)
    
    return None


# Llama al archivo "listado-de-tablas"
def get_listado_de_tablas():
    with open('./listado-de-tablas.json', 'r') as file:
         data = json.load(file)
         nro_de_tabla = 0
         cant_tablas = len(data)
         print("Cantidad de Tablas: {}\n".format(cant_tablas))
         
         for table in data:
             tabla_nombre = table['table_name']
             registros = consultar_tabla_json(tabla_nombre)
             if registros is not None:
                 crear_archivo(tabla_nombre, registros)
                 nro_de_tabla += 1
                 print("Tabla Procesada {} de {} \n".format(nro_de_tabla, cant_tablas))
             else:
                 print('No se encontro tabla')
            
    print('Finalizado')
             


# Genera json en el la carpera informacion
def crear_archivo(nombre_archivo, data):
    with open('../datasets/' + nombre_archivo + '.json', 'w', 
              encoding='utf-8') as file:
        data_json = json.loads(data)
        json.dump(data_json, file, indent=4, ensure_ascii=False)
   

if __name__ == '__main__':
    get_listado_de_tablas()
