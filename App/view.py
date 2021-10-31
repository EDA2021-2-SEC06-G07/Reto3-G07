"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

from typing import Collection
import config as cf
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as tree
from DISClib.DataStructures import linkedlistiterator as iter
assert cf


UFO_ART1 = """                 _,--=--._
               ,'    _    `.
              -    _(_)_o   -
         ____'    /_  _/]    `____
  -=====::(+):::::::::::::::::(+)::=====-
           (+).""""""""""""",(+)
               .           ,
                 `  -=-  '"""
UFO_ART2 = """
                 _                ( Muchas gracias por usar la App51. )
                /\\\\               ( La informacion en esta App es confidencial.)
                \ \\\\  \__/ \__/  / ( No comparta la informacion que se )
                 \ \\\\ (oo) (oo) /    (encuentra en la App con nadie.)
                  \_\\\\/~~\_/~~\_
                 _.-~===========~-._
                (___/_______________)
                   /  \_______/
       ( Sabemos donde vive... )"""

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido a la App51.")
    print(UFO_ART1)
    print('Porfavor tenga cuidado.')
    print("Objetos voladores no identificados han siido vistos en este programa.")
    print("Queda advertido.")
    print("0- Buscar UFOs")
    print("1- Mirar UFOs por ciudad")
    print('2- Contar avistamientos por Hora/Minutos del día')
    print()

catalog = None


# Initializes the catalog and gets the data
def load():
    catalog = controller.init_catalog()
    controller.load_catalog(catalog)
    return catalog


#req 1
def req1():
    print("UFOs por ciudad")
    city = input("Porfavor dinos cual ciudad quieres mirar.\n")

    data = controller.req1(catalog['DATE'], city)
    
    print('Primeros 3 avistamientos:')
    for i in range(0, 3):
        print(data['city'].keys())
        ufo = lt.getElement(data['city']['value'], i)
        print(f'avistamiento {i + 1}:')
        datetime = ufo['datetime']
        print(f'\tfecha y hora: {datetime}')
        country = ufo['country']
        print(f'\tpais: {country}, city: {city}')
        duration = ufo['duration (hours/min)']
        print(f'\tduraciom: {duration}')
        shape = ufo['shape']
        print(f'\tshape: {shape}')

    print('ultimos avistamientos:')
    for i in range(lt.size(data['city']['value']) - 3, lt.size(data['city']['value'])):
        ufo = lt.getElement(data['city']['value'], i)
        print(f'avistamiento {i + 1}:')
        datetime = ufo['datetime']
        print(f'\tfecha y hora: {datetime}')
        country = ufo['country']
        print(f'\tpais: {country}, city: {city}')
        duration = ufo['duration (hours/min)']
        print(f'\tduraciom: {duration}')
        shape = ufo['shape']
        print(f'\tshape: {shape}')

    print('We recomend you to check this other locations')
    for i in range(1, 7):
        locations = tree.valueSet(data['full_data'])
        location_list = lt.getElement(locations, i)
        location = location_list['first']['info']['city']
        size = lt.size(location_list)
        print(f'\t{location} tiene {size} avistamientos')

def req_3():
    print('ingrese las horas en formato HH:MM')
    
    hora_min=input('ingresa hora minima: ')
    hora_max=input('ingresa hora maxima: ')
    lolo=controller.req3(catalog,hora_min,hora_max)
    print(lolo)

"""
Menu principal
"""

if __name__ == "__main__":
    running = True
    while running:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 0:
            print("Buscando UFOs")
            catalog = load()
            size = tree.size(catalog['DATE'])
            print(f"Se han encontrado {size} UFOs en su area.")
            print("Se le recomienda tener quidado.")
           
            print()

        elif int(inputs[0]) == 1:
            req1()

        elif int(inputs[0]) == 3:
            req_3()
        else:
            print(UFO_ART2)
            print()
            running = False
