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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as tree
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Set catalog as a red black tree
def init_catalog():
    catalog = tree.newMap(omaptype='RBT', comparefunction=cmp_UFO)
    return catalog


# Adds a UFO site to the tree
def add_ufo(catalog, ufo):
    tree.put(catalog, ufo, ufo['datetime'])

# Funciones para creacion de datos

# Funciones de consulta

# Funciones de comparacion

    #compares 2 ufo sites by the latitude and longitude of the sites
def cmp_UFO(ufo1, ufo2):
    res = 1

    datetime1 = ufo1['datetime']
    datetime2 = ufo2['datetime']

    if datetime1 < datetime2:
        res = -1
    elif datetime1 == datetime2:
        res = 0
    
    return res

# Funciones de ordenamiento
