"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv

FILE = "/Data/UFOS/UFOS-utf8-small.csv"

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Initializes the catalog
def init_catalog():
    catalog = model.init_catalog()
    return catalog


# Adds the data to the catalog
def load_catalog(catalog):
    ufo_file = cf.file_dir + FILE
    data = csv.DictReader(open(ufo_file, encoding='utf-8'))
    for ufo in data:
        model.add_ufo(catalog, ufo)
        model.add_hour(catalog,ufo)

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

# Requerimientos
def req1(catalog, city):
    return model.req1(catalog, city)
def req3(catalog,hora_min,hora_max):
    return model.req_3(catalog,hora_min,hora_max)