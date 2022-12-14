import os
#import agregarValores as av
import funciones as F

def mostrar_menu(opciones):
    os.system("clear")
    print("Grupo 03 - Cowabunga\nChristian Romero - Nicolas Goires - Victor Craigdallie")
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    os.system("clear")
    opciones = {
        '1': ('Agregar Valores a la lista', agregarValores),
        '2': ('Borrar Valores de la lista', eliminarValores),
        '3': ('Buscar valores en la lista', buscarValores),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')

def agregarValores():
    F.agregarValores(num_list)

def eliminarValores():
    F.eliminarValores(num_list)

def buscarValores():
    F.buscarValores(num_list)

def salir():
    print('Saliendo')

if __name__ == '__main__':
  
  num_list = []
  menu_principal()
