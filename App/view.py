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
import timer
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
def print_ufo(ufo):
    date_time = ufo['datetime']
    print(f'date and time: {date_time}')

    city = ufo['city']
    print(f'    city: {city}')

    country = ufo['country']
    print(f'    country: {country}')

    duration = ufo['duration (seconds)']
    print(f'    duration: {duration}')

    shape = ufo['shape']
    print(f'    shape: {shape}')


def printMenu():
    print("Bienvenido a la App51.")
    print(UFO_ART1)
    print('Porfavor tenga cuidado.')
    print("Objetos voladores no identificados han siido vistos en este programa.")
    print("Queda advertido.")
    print("0- Buscar UFOs")
    print("1- Mirar UFOs por ciudad")
    print('2- Contar los avistamientos por duración')
    print('3-Contar avistamientos por Hora/Minutos del día')
    print('4-Contar los avistamientos en un rango de fechas')
    print('5-Contar los avistamientos de una Zona Geográfica')

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


def req2():
    init_sec = float(input("Place initial duration in seconds:"))
    final_sec = float(input('Place the final duration in seconds:'))

    res = controller.req2(catalog['DATE'], init_sec, final_sec)
    info = tree.valueSet(res)
    size = tree.size(res)
    print(f'hubo {size} avistammientos')

    for i in range(0, 3):
        print_ufo(lt.getElement(info, i))

    for i in range(lt.size(info) - 3, lt.size(info)):
        print_ufo(lt.getElement(info, i))


def req_3():
    print('ingrese las horas en formato HH:MM')
    
    hora_min=input('ingresa hora minima: ')
    hora_max=input('ingresa hora maxima: ')
    ufos=controller.req3(catalog,hora_min,hora_max)
    print('')
    print('Primero 3')
    for i in range (0,3):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    print('')
    print('Ultimos 3')
    for i in range(lt.size(ufos)-3,lt.size(ufos)):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])


def req_4():
    print('Ingrese las fechas en formato AA-MM_DD')
    date_min=input('Ingrese la fecha minima: ')
    date_max=input('Ingrese la fecha maxima: ')
    ufos= controller.req4(catalog,date_min,date_max)
    print('')
    print('Primero 3')
    for i in range(0,3):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    print('')
    print('Ultimos 3')
    for i in range(lt.size(ufos)-3,lt.size(ufos)):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    

def req_5():
    long_min= float(input('Ingresa la longitud minima: '))
    long_max=float(input('Ingresa la longitud maxima: '))
    lat_min= float(input('Ingresa la latitud minima: '))
    lat_max= float(input('Ingresa la latitud maxima: '))
    ufos= controller.req5(catalog,long_min,long_max,lat_min,lat_max)
    print('')
    print('Primero 3')
    for i in range(0,5):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    print('')
    print('Ultimos 3')
    for i in range(lt.size(ufos)-5,lt.size(ufos)):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
        print('longitude: '+ lt.getElement(ufos,i)['longitude'])
        print('latitude: '+ lt.getElement(ufos,i)['latitude'])

# Speed_test

def req1_test():
    print("UFOs por ciudad")

    data = controller.req1(catalog['DATE'], 'las vegas')
    
    print('Primeros 3 avistamientos:')
    for i in range(0, 3):
        print(data['city'].keys())
        ufo = lt.getElement(data['city']['value'], i)
        print(f'avistamiento {i + 1}:')
        datetime = ufo['datetime']
        print(f'\tfecha y hora: {datetime}')
        country = ufo['country']
        print(f'\tpais: {country}, city: las vegas')
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
        print(f'\tpais: {country}, city: las vegas')
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


def req2_test():
    
    res = controller.req2(catalog['DATE'], 30, 150)
    info = tree.valueSet(res)
    size = tree.size(res)
    print(f'hubo {size} avistammientos')

    for i in range(0, 3):
        print_ufo(lt.getElement(info, i))

    for i in range(lt.size(info) - 3, lt.size(info)):
        print_ufo(lt.getElement(info, i))


def req3_test():
    print('ingrese las horas en formato HH:MM')
    
    ufos=controller.req3(catalog,'20:45:00','23:15:00')
    print('')
    print('Primero 3')
    for i in range (0,3):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    print('')
    print('Ultimos 3')
    for i in range(lt.size(ufos)-3,lt.size(ufos)):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])


def req4_test():
    print('Ingrese las fechas en formato AA-MM_DD')
    
    ufos= controller.req4(catalog,'1945-08-06','1984-11-15')
    print('')
    print('Primero 3')
    for i in range(0,3):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    print('')
    print('Ultimos 3')
    for i in range(lt.size(ufos)-3,lt.size(ufos)):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])


def req5_test():

    ufos= controller.req5(catalog,-109.05,-103.0,31.33,37.0)
    print('')
    print('Primero 3')
    for i in range(0,5):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
    print('')
    print('Ultimos 3')
    for i in range(lt.size(ufos)-5,lt.size(ufos)):
        print('')
        print('Datetime: '+ lt.getElement(ufos,i)['datetime'])
        print('city: '+ lt.getElement(ufos,i)['city'])
        print('state: '+ lt.getElement(ufos,i)['state'])
        print('country: ' + lt.getElement(ufos,i)['country'])
        print('shape: '+ lt.getElement(ufos,i)['shape'])
        print('duration: '+ lt.getElement(ufos,i)['duration (seconds)'])
        print('longitude: '+ lt.getElement(ufos,i)['longitude'])
        print('latitude: '+ lt.getElement(ufos,i)['latitude'])



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
        elif int(inputs[0]) == 2:
            req2()
        elif int(inputs[0]) == 3:
            req_3()
        elif int(inputs[0]) == 4:
            req_4()
        elif int(inputs[0]) == 5:
            req_5()
        elif int(inputs[0]) == 8:
            stop_watch = timer.Timer()
            catalog = load()

            time1 = stop_watch.time_function(req1_test)
            time2 = stop_watch.time_function(req2_test)
            time3 = stop_watch.time_function(req3_test)
            time4 = stop_watch.time_function(req4_test)
            time5 = stop_watch.time_function(req5_test)

            print('\n\n')
            print("time req1: " + str(time1) + 's')
            print("time req2: " + str(time2) + 's')
            print("time req3: " + str(time3) + 's')
            print("time req4: " + str(time4) + 's')
            print("time req5: " + str(time5) + 's')

        else:
            print(UFO_ART2)
            print()
            running = False
