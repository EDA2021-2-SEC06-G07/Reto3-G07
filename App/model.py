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
from DISClib.DataStructures import linkedlistiterator as iter
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Set catalog as a red black tree
def init_catalog():
    catalog={'DATE': None, 'HOUR': None}
    catalog['DATE'] = tree.newMap(omaptype='RBT', comparefunction=cmp_UFO)
    catalog['HOUR']= tree.newMap(omaptype='BST')
    return catalog


# Adds a UFO site to the tree
def add_ufo(catalog, ufo):
    tree.put(catalog, ufo['datetime'], ufo)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones de comparacion

    #compares 2 ufo sites by the latitude and longitude of the sites
def cmp_UFO(datetime1, datetime2):
    res = 1

    if datetime1 < datetime2:
        res = -1
    elif datetime1 == datetime2:
        res = 0
    
    return res


def cmp_lists(size1, size2):
    res = -1

    if size1 < size2:
        res = 1
    elif size1 == size2:
        res = 0

    return res


# Funciones de ordenamiento


#Requerimientos
def req1(catalog, city):
    temp_map = mp.newMap()
    ufo_data = tree.valueSet(catalog)

    i = iter.newIterator(ufo_data)
    while(iter.hasNext(i)):
        element = iter.next(i)
        city_element = element['city']

        if(mp.contains(temp_map, city_element)):
            lt.addLast(mp.get(temp_map, city_element)['value'], element)
        else:
            mp.put(temp_map, city_element, lt.newList())
            lt.addLast(mp.get(temp_map, city_element)['value'], element)

    ufo_data = tree.newMap(omaptype='RBT', comparefunction=cmp_lists)
    city_lists = mp.valueSet(temp_map)

    i  = iter.newIterator(city_lists)
    while(iter.hasNext(i)):
        list = iter.next(i)
        tree.put(ufo_data, lt.size(list), list)

    city_list = mp.get(temp_map, city)
    
    return {'city': city_list, 'full_data': ufo_data}

    

