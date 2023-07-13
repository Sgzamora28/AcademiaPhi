conjunto=set() #{1,2,3,4}

# diccionario={"Nombre":"Steven","Edad":20,"Matricula":202101713}

# #Obtener valores
# # print("La edad del ejemplo es",diccionario['Edad'])

# #Editar valores
# print("El nombre original es",diccionario['Nombre'])
# diccionario['Nombre']="Domenica"
# print("El nombre modificado es",diccionario['Nombre'])



# #Crear entradas en el diccionario
# diccionario["Direccion"]="Sergio Toral 2"
# print(diccionario['Direccion'])


# #Mal acceso a los valores
# # diccionario["Nombres"]="Kyra"
# # print(diccionario["Nombres"])



# #Acceso correcto a los valores sin modificarlos
# x=diccionario.get("Nombres",-1)
# print(x)
####################################################################################################################################################################
# Para administrar la nueva matriz energética del Ecuador, se dispone de un diccionario con la información 
# de las plantas de energía y las ciudades que atienden cada una.
# Cada ciudad tiene: una tupla con los consumos mensuales (12) del año en megavatios-hora (MWh) y 
# la tarifa de consumo en dólares por megavatio-hora (MWh) que le cobra la planta eléctrica.
# Una ciudad puede estar servida por más de una planta eléctrica. 
# No todas las ciudades son servidas por todas las plantas eléctricas.

consumo_energia={
									'Coca Codo Sinclair':{
																				'Quito': { 'consumos':(400, 432, 213, 440, 432, 300, 200, 432, 300, 400, 400, 420),'tarifa': 65},
																				'Guayaquil': { 'consumos': (120, 55, 32, 70, 120, 75, 150, 32, 55, 97, 32, 100),'tarifa': 84}},
									'Sopladora':{
															'Guayaquil':{ 'consumos': (310, 220, 321, 200),'tarifa':55},
															'Quito': { 'consumos': (400, 432, 587),'tarifa': 79},
															'Loja': { 'consumos': (50, 32, 32, 40),'tarifa': 32}}
                }

# Además, dispone del siguiente diccionario con información de ciudad por región :

informacion={
							'costa': ('Guayaquil', 'Manta'),
							'sierra': ('Quito', 'Ambato'),
							'oriente': ('Tena', 'Nueva Loja')}
# Implemente lo siguiente:

####################################################################################################################################################################
# Una función total_anual(consumo_energia, planta, ciudad) que recibe el diccionario consumo_energia, 
# el nombre de una planta y el nombre de una ciudad. La función debe calcular y retornar el total anual de 
# megavatios-hora servido por planta a ciudad. (7 puntos)

def total_anual(consumo:dict,planta:str,ciudad:str):

  for key in consumo:
    if key==planta:
      for key_ciudad in consumo[key]:
        if ciudad==key_ciudad:
          return sum(consumo[key][ciudad]["consumos"])



####################################################################################################################################################################
# Una función total_plantas_ciudad(consumo_energia, ciudad) que recibe el diccionario consumo_energia 
# y el nombre de una ciudad. La función debe devolver un diccionario cuyas claves corresponden a 
# los nombres de las plantas generadoras que proveen energía a ciudad y los valores corresponden al 
# total anual de megavatios-hora servido por cada planta a ciudad. (13 puntos)

def plantasXciudad(consumo:dict,ciudad:str):
  resultado={}
  for key in consumo:
    if ciudad in consumo[key]:
      valores=total_anual(consumo,key,ciudad)
      resultado[key]=valores
  
  return resultado

####################################################################################################################################################################
# Una función megavatios_hora(consumo_energia, informacion) que recibe el diccionario consumo_energia 
# y el diccionario informacion. La función retorna el total anual de megavatios-hora 
# consumido por todas las ciudades de la región COSTA. (15 puntos)

def megavatiosHora(consumo:dict,info:dict):
  consumoRegional=0

  for region in info:
    if region=="costa":
      for ciudad in info[region]:
        valor=list(plantasXciudad(consumo,ciudad).values())
        consumoRegional+=sum(valor)
  
  return consumoRegional


####################################################################################################################################################################
# Una función facturacion(consumo_energia) que recibe el diccionario consumo_energia y 
# genera un archivo con la facturación total en dólares de los seis primeros meses de cada planta 
# generadora. El archivo resultante se llamará 'facturacion.txt' y tendrá la siguiente estructura: (15 puntos)





####################################################################################################################################################################

#MAIN
x=total_anual(consumo_energia,'Coca Codo Sinclair','Quito')
# print(x)

diccionario={"valor 1":10,"valor 2":20,"valor 3":100}

# x=list(diccionario.keys())
# # print(x)
# y=list(diccionario.values())
# # print(y)

# z=list(diccionario.items())
# # print(z)

y=plantasXciudad(consumo_energia,"Guayaquil")
print(y)

z=megavatiosHora(consumo_energia,informacion)
print(z)