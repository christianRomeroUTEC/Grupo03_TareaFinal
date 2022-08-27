import os
import agregarValores as av

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
  os.system("clear")
  print('Agregar Valores a la lista')
  while True:
    try:
      numero = int(input("Ingrese un numero: "))
    #av.pido_numero("Ingrese un numero: ")
      if(numero != 0):
        av.agregar_valor(num_list, numero)
      condicion = input("Para continuar agrgando a la lista precione enter en caso contrario precione (N)") 
      
      if("N" == condicion.upper()):
        break
    except:
      print("No se ingreso ningun valor")
  
  print(num_list)
  input("Preciona enter para volver al menu principal")



def eliminarValores():
  os.system("clear")
  cantidad = len(num_list)
  print('Eliminar valor de la lista')
  print('Cantidad de registros en la lista: ' , cantidad)
  if(cantidad > 0):
    print('Valores Actuales: ', num_list)
    numero = input("Ingrese valor a buscar: ")
    try:
        numero = int(numero)
        av.eliminarValores(num_list, numero)
        print('Valores nuevos: ', num_list)
      
    except:
      print("No ingreso valores")
  else:
    print('No hay valores ingresados en la lista')
  input("Preciona enter para volver al menu principal")
  

  


def buscarValores():
  os.system("clear")
  print("Buscar cantidad de veces que aparece el valor\n")
  if(len(num_list) > 0):
    numero = input("Ingrese valor a buscar: ")
    try:
      numero = int(numero)
      result = av.buscar_valor(num_list, numero)
      print("El valor buscado ", numero, " aparece ", result, " veces en la lista")
    
    except:
      print("No ingreso un número")
  else:
    print("No hay valores ingresados en la lista")
  input("Preciona enter para volver al menu principal")

    


def salir():
    print('Saliendo')

if __name__ == '__main__':
  
  num_list = []
  menu_principal()