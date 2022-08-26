def pido_numero(mensaje):
  numero = input(mensaje)
  try:
    numero = int(numero)
  except:
    numero = input("No ha ingresado un número")
    
  return numero


def agregar_valor(list, item):
  try:
    list.append(int(item))
  except:
    print("No ingreso valores")
  return list
  
  