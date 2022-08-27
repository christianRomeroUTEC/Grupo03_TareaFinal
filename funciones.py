import os
import agregarValores as AV

def agregarValores(list):
  os.system("clear")
  print('Agregar Valores a la lista')
  while True:
    try:
      numero = int(input("\nIngrese un numero: "))
      if(numero != 0):
        AV.agregar_valor(list, numero)
      condicion = input("\nDesea continuar ingresando valores (Y/n): ") 
      
      if("N" == condicion.upper()):
        break
    except:
      print("\nNo se ingreso ningún valor")
  
  print(list)
  input("\nPresione Enter para volver al menu principal")
  return list


def eliminarValores(list):
  os.system("clear")
  cantidad = len(list)
  print('\nEliminar valor de la lista')
  print('\nCantidad de registros en la lista: ' , cantidad)
  if(cantidad > 0):
    print('Lista actual: ', list)
    numero = input("\nIngrese valor a eliminar: ")
    try:
        numero = int(numero)
        AV.eliminarValores(list, numero)
        print('\nLista resultante: ', list)
      
    except:
      print("\nNo ingreso valores")
  else:
    print('\nNo hay valores ingresados en la lista')
  input("\nPresione enter para volver al menu principal")
  return list

  


def buscarValores(list):
  os.system("clear")
  print("\nBuscar cantidad de veces que aparece el valor")
  if(len(list) > 0):
    numero = input("\nIngrese valor a buscar: ")
    try:
      numero = int(numero)
      result = AV.buscar_valor(list, numero)
      print("\nEl valor buscado ", numero, " aparece ", result, " veces en la lista")
    
    except:
      print("\nNo ingreso un número")
  else:
    print("\nNo hay valores ingresados en la lista")
  input("\nPresione Enter para volver al menú principal")

    
