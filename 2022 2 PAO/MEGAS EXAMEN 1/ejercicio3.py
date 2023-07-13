# Una compañía propietaria de una tarjeta de crédito tiene almacenadas las transacciones realizadas por los 
# usuarios de dicha tarjeta y requiere hacer un análisis por barrio. Para esto asuma que tiene la siguiente lista:
# #tipo de artículo comprado
lista_tipos = ["V:Vestimenta", "A:Alimentacion", "E:Educación", "N:Entretenimiento", "S:Salud"]

# Asuma que también tiene la lista transacciones con la información de las transacciones del 2019 y 2020 hechas 
# por los clientes. Los tipos de artículos se pueden repetir para un mismo barrio en un mismo año. 
# La lista tiene el siguiente formato:
# Barrio:Fecha,Local,Tipo_articulo,Valor
lista_transac=["Alborada:21-12-2019,Veris,S,$35.40",
               "Alborada:22-12-2019,FrutaBar,A,$42.00",
               "La Floresta:19-12-2020,Dipiur,V,$48.00",
               "Sauces IV:8-12-2019,Farmacia Trebol Verde,S,$309.78",
               "9 de Octubre:12-12-2020,La Esquina de Alex,A,$22.00",
               "Centenario:01-01-2020,LAN,T,$420"]
# Implemente las siguientes funciones:
# 1. ventas_tipos(lista_transac, lista_tipos) que recibe la lista de transacciones y de tipos. 
# La función retorna dos elementos: el primer elemento es una lista con el tipo de artículo (el nombre, no la inicial) 
# y el segundo elemento es una lista con el total de cuánto se ha consumido (en dólares) para ese tipo de artículo.
def ventas_tipos(transacciones:list[str],tipos:list[str]):
  codigos=[]
  totales=[]
  for tipo in tipos:
    codigo,nombre=tipo.split(":")#["V","Vestimenta"]
    codigos.append(nombre)
    total=0
    for trans in transacciones:
      datos=trans.split(",")#["Alborada:21-12-2019","Veris","S","$35.40"]
      # print(datos)
      c=datos[-2]
      if c==codigo:
        valor=float(datos[-1].strip("$"))#"35.40"----> 35.40
        total+=valor

    totales.append(round(total,2))

  return codigos,totales


x,y=ventas_tipos(lista_transac,lista_tipos)
# print(x)
# print(y)

# 2. barrios(lista_transac, año) que recibe la lista de transacciones y un año (2019 o 2020). 
# La función debe retornar una lista con los barrios donde se han realizado las transacciones en ese año, 
# sin repeticiones.

def barrios(transacciones:list[str],anio:int):
  lista=[]

  for trans in transacciones:
    datos=trans.split(",")#["Alborada:21-12-2019","Veris","S","$35.40"]
    barrio,fecha=datos[0].split(":")#["Alborada","21-12-2019"]
    anio2=fecha.split("-")[-1]
    if anio==int(anio2) and barrio not in lista:
      lista.append(barrio)

  return lista


lista=barrios(lista_transac,2019)
print(lista)