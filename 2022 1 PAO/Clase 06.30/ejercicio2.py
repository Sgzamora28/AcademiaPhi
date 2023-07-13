# Una compañía propietaria de una tarjeta de crédito tiene almacenadas las transacciones realizadas por los usuarios de dicha tarjeta y 
# requiere hacer un análisis por barrio. Para esto asuma que tiene la siguiente tupla:

# #tipo de artículo comprado
tipo = ("V:Vestimenta", "A:Alimentacion", "E:Educación", "N:Entretenimiento", "S:Salud")
# Asuma que también tiene la lista transacciones con la información de las transacciones del 2019 y 2020 hechas por los clientes. 
# Los tipos de artículos se pueden repetir para un mismo barrio en un mismo año. La lista tiene el siguiente formato:

# Barrio:Fecha,Local,Tipo_articulo,Valor
transacciones=[ "Alborada:21-12-2019,Veris,S,$35.40",
                "Alborada:22-12-2019,FrutaBar,A,$42.00",
                "La Floresta:19-12-2020,Dipiur,V,$48.00",
                "Sauces IV:8-12-2019,Farmacia Trebol Verde,S,$309.78",
                "9 de Octubre:12-12-2020,La Esquina de Alex,A,$22.00",
                "Centenario:01-01-2020,LAN,T,$420"]
# Implemente las siguientes funciones:

# 1. ventas_tipos(lista_transac, tupla_tipos) que recibe la lista de transacciones y la tupla de tipos. 
# La función retorna una lista de tuplas de dos elementos: el primer elemento de la tupla es el tipo de artículo (el nombre, no la inicial) 
# y el segundo elemento es el total de cuánto se ha consumido (en dólares) para ese tipo de artículo.

# 2. barrios(lista_transac, año) que recibe la lista de transacciones y un año (2019 o 2020). La función debe retornar una colección con los barrios 
# donde se han realizado las transacciones en ese año, sin repeticiones.



#implementacion
def ventas_tipos(lista:list,tupla:tuple):
  resultado=[]
  for tipo in tupla:
    x=[]
    cod,nombre_cod=tipo.split(':')
    total=0
    for trans in lista:
      cod2,valor=trans.split(',')[-2:]
      if cod==cod2:

        total+=float(valor.strip('$'))
    
    total=round(total,2)
    x.append(nombre_cod)
    x.append(total)
    x=tuple(x)
    resultado.append(x)
  
  return resultado


x=ventas_tipos(transacciones,tipo)
print(x)