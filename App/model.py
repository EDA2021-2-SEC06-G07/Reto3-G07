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


from posixpath import split
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as tree
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.DataStructures import linkedlistiterator as iter
import datetime 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Set catalog as a red black tree
def init_catalog():
    catalog={'DATE': None, 'HOUR': None, 'DATES': None}
    catalog['DATE'] = tree.newMap(omaptype='RBT', comparefunction=cmp_UFO)
    catalog['HOUR']= tree.newMap(omaptype='BST', comparefunction=cmp_UFO)
    catalog['DATES']= tree.newMap(omaptype='BST')
    return catalog


# Adds a UFO site to the tree
def add_ufo(catalog, ufo):
    tree.put(catalog['DATE'], ufo['datetime'], ufo)


def add_hour(catalog,ufo):
    date=ufo['datetime']
    date1=date.split(" ")
    date2=date1[1].split(':')
    ufodate=datetime.time(int(date2[0]),int(date2[1]))
    entry=tree.get(catalog['HOUR'],ufodate)
    if entry is None:
        tree.put(catalog['HOUR'], ufodate, lt.newList(datastructure='ARRAY_LIST'))
        lt.addLast(tree.get(catalog['HOUR'],ufodate)['value'],ufo)
    else:
        lt.addLast(tree.get(catalog['HOUR'],ufodate)['value'],ufo)
    return catalog


def add_dates(catalog,ufo):
    date=ufo['datetime']
    date1=date.split(" ")
    date2=date1[0].split('-')
    ufodate=datetime.date(int(date2[0]),int(date2[1]),int(date2[2]))
    entry=tree.get(catalog['DATES'],ufodate)
    if entry is None:
        tree.put(catalog['DATES'], ufodate, lt.newList(datastructure='ARRAY_LIST'))
        lt.addLast(tree.get(catalog['DATES'],ufodate)['value'],ufo)
    else:
        lt.addLast(tree.get(catalog['DATES'],ufodate)['value'],ufo)
    return catalog
# Funciones para creacion de datos

# Funciones de consulta
def req_3(catalog,hora_min,hora_max):
    antiguo = tree.maxKey(catalog['HOUR'])
    tamaño_antiguo= tree.values(catalog['HOUR'],antiguo, antiguo)
    respuesta= lt.newList(datastructure='ARRAY_LIST')
    min=hora_min.split(':')
    hora_min=datetime.time(int(min[0]), int(min[1]))
    max=hora_max.split(':')
    hora_max=datetime.time(int(max[0]),int(max[1]))
    lst=tree.values(catalog['HOUR'],hora_min,hora_max)
    contador= 0 
    for i in lt.iterator(lst):
        contador += lt.size(i)
        for j in lt.iterator(i):
            lt.addLast(respuesta,j)
    print('')
    print('Se encontraron '+ str(contador)+ ' avistamientos')
    print('')
    print('Mas tarde: '+ str(antiguo) + ' con' + str(lt.size(tamaño_antiguo)))
    return respuesta
    
def req_4(catalog,date_min,date_max):
    respuesta= lt.newList(datastructure='ARRAY_LIST')
    antiguo = tree.minKey(catalog['DATES'])
    tamaño_antiguo= tree.values(catalog['DATES'],antiguo, antiguo)
    min=date_min.split('-')
    fecha_min=datetime.date(int(min[0]), int(min[1]),int(min[2]))
    max=date_max.split('-')
    fecha_max=datetime.date(int(max[0]),int(max[1]),int(max[2]))
    lst=tree.values(catalog['DATES'],fecha_min,fecha_max)
    contador= 0 
    for i in lt.iterator(lst):
        contador += lt.size(i)
        for j in lt.iterator(i):
            lt.addLast(respuesta,j)
    print('')
    print('Se encontraron '+ str(contador) + ' avistamientos')
    print('El avistamiento mas antiguo fue '+ str(antiguo)+ ' con ' + str(lt.size(tamaño_antiguo)))
    return respuesta
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


def cmp_horas(hour1,hour2):
    res = 1
    if hour1<hour2:
        res=-1
    elif hour1>hour2:
        res=0
    return res


def cmp_horass(hour1,hour2):
    hour1= hour1
    res = 1
    if hour1<hour2:
        res=-1
    elif hour1>hour2:
        res=0
    return res


def cmp_seconds(sec1, sec2):
    res = 1
    if sec1 < sec2:
        res = -1
    elif sec1 == sec2:
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

    
def req2(catalog, init_sec, final_sec):
    sites = tree.newMap(omaptype='rbt', comparefunction=cmp_seconds)
    ufos = tree.valueSet(catalog)
    i = iter.newIterator(ufos)
    while iter.hasNext(i):
        ufo = iter.next(i)
        duration = int(ufo['duration (seconds)'].split('.')[0])
        if init_sec <= duration and duration <= final_sec:
            tree.put(sites, ufo['duration (seconds)'], ufo)

    return sites


