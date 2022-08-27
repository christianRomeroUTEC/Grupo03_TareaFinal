def agregar_valor(list, item):
  try:
    list.append(int(item))
  except:
    print("No ingreso valores")
  return list


def eliminarValores(list, item):
  try:
    i=0
    while i <= len(list)-1:
      if list[i] == item:
        list.pop(i)
      else:
        i = i+1
  except Exception as e:
    print("\nOcurrio un error: ", e)
  return list


def buscar_valor(list, item):
  cant=0
  try:
    i=0
    while i <= len(list)-1:
      if list[i] == item:
        cant = cant + 1
        i = i + 1
      else:
        i = i + 1
  except Exception as e:
    print("\nOcurrio un error: ", e)
  return cant
    
  
