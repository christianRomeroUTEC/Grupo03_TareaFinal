import os
import agregarValores as av

def mostrar_menu(opciones):
    print("Grupo 13 - Cowabunga\nChristian Romero - Nicolas Goires - El Victor")
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
        os.system("clear")
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
  os.system("clear")
  print('Agregar Valores a la lista')
  while True:
    try:
      numero = int(input("Ingrese un numero: "))
    #av.pido_numero("Ingrese un numero: ")
      if(numero != 0):
        av.agregar_valor(num_list, numero)
      condicion = input("Continuar: (N)o ") 
      if("N" == condicion.upper()):
        break
    except:
      print("No se ingreso ningun valor")
  
  print(num_list)
  input()



def eliminarValores():
    print('Has elegido la opción 2')


def buscarValores():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')

if __name__ == '__main__':
  
  num_list = []
  menu_principal()