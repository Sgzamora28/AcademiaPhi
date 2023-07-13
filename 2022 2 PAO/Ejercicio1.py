consumo_energia = {
'Coca Codo Sinclair': {
                       'Quito': { 'consumos':(400, 432, 213),'tarifa': 65},
                       'Guayaquil': { 'consumos': (120, 55, 32, 70),'tarifa': 84},
                      },
         'Sopladora': {
                       'Guayaquil':{ 'consumos': (310, 220, 321, 200),'tarifa':55},
                       'Quito': { 'consumos': (400, 432, 587),'tarifa': 79},
                       'Loja': { 'consumos': (50, 32, 32, 40),'tarifa': 32},
                      }
}


informacion = {
'costa': ('Guayaquil', 'Manta'),
'sierra': ('Quito', 'Ambato'),
'oriente': ('Tena', 'Nueva Loja')}


# Implemente lo siguiente:
# 1) Una función total_anual(consumo_energia, planta, ciudad) que recibe el diccionario consumo_energia ,
# el nombre de una planta y el nombre de una ciudad. La función debe calcular y retornar el total anual de
# megavatios-hora servido por planta a ciudad . (7 puntos)
# 2) Una función total_plantas_ciudad(consumo_energia, ciudad) que recibe el diccionario
# consumo_energia y el nombre de una ciudad. La función debe devolver un diccionario cuyas claves
# corresponden a los nombres de las plantas generadoras que proveen energía a ciudad y los valores
# corresponden al total anual de megavatios-hora servido por cada planta a ciudad . (13 puntos)
# 3) Una función megavatios_hora(consumo_energia, informacion) que recibe el diccionario
# consumo_energia y el diccionario informacion . La función retorna el total anual de megavatios-hora
# consumido por todas las ciudades de la región COSTA.




def total_anual(consumo:dict,planta:str,ciudad:str):
  total=0
  for empresa,ciudades in consumo.items():
    if empresa==planta:
      for city,valores in ciudades.items():
        if city==ciudad:
          tarifa=valores["tarifa"]
          consumos=valores["consumos"]
          for mensual in consumos:
            total+=mensual*tarifa

  return total




def total_plantas(consumos:dict[str:dict],ciudad:str):
  plantas={}
  for planta,ciudades in consumos.items():
    if ciudad in ciudades:
      plantas[planta]=total_anual(consumos,planta,ciudad)

  
  return plantas


def mwh(consumos:dict,info:dict):
  total=0
  for ciudad in info['costa']:
    plantas=total_plantas(consumos,ciudad)
    total+=sum(plantas.values())

  return total


total=mwh(consumo_energia,informacion)
print(total)



# x={'nombre':"Steven",'apellido':"Zamora","edad":20,"matricula":202101713}
#Recorrer por clave
# for clave in x:
#   print(clave)

# claves=list(x.keys())
# print(claves)

# for clave in x.keys():
#   print(clave)


#Recorrer por valores
# valores=list(x.values())
# print(valores)

# for valor in x.values():
#   print(valor)

#Recorrer clave,valor
# elementos=list(x.items())
# print(elementos)

# for clave,valor in x.items():
#   if clave=="matricula":
#     print(valor)