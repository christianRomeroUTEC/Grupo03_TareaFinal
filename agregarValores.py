def agregar_valor(list, item):
  try:
    list.append(int(item))
  except:
    print("No ingreso valores")
  return list


def eliminarValores(list, item):
  try:
    i=0
    while i < len(list):
      if i == item:
        list.remove(i)
      else:
        i = i+1
  except:
    print("No se pudo borrar el elemento")
  return list


def buscar_valor(list, item):
  cant=0
  for index in list:
    if index == item:
      cant = cant + 1
  return cant
    
  