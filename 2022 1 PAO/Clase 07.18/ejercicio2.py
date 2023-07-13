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
															'Loja': { 'consumos': (50, 32, 32, 40),'tarifa': 32}}}

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
	for central in consumo:
		if planta==central:
			for city in consumo[planta]:
				if city==ciudad:
					consumo_anual=sum(consumo[planta][ciudad]["consumos"])

	return consumo_anual
####################################################################################################################################################################
# Una función total_plantas_ciudad(consumo_energia, ciudad) que recibe el diccionario consumo_energia 
# y el nombre de una ciudad. La función debe devolver un diccionario cuyas claves corresponden a 
# los nombres de las plantas generadoras que proveen energía a ciudad y los valores corresponden al 
# total anual de megavatios-hora servido por cada planta a ciudad. (13 puntos)

def totalPlantas_ciudad(consumo:dict,ciudad:str):
	plantasXciudad={}
	for central in consumo:
		if ciudad in consumo[central]:
			consumo_anual=total_anual(consumo,central,ciudad)
			plantasXciudad[central]=consumo_anual
	return plantasXciudad
####################################################################################################################################################################
# Una función megavatios_hora(consumo_energia, informacion) que recibe el diccionario consumo_energia 
# y el diccionario informacion. La función retorna el total anual de megavatios-hora 
# consumido por todas las ciudades de la región COSTA. (15 puntos)
def megavatios_hora(consumo:dict,info:dict):
	totalXregion=0
	for ciudad in info["costa"]:
		plantas_ciudad=totalPlantas_ciudad(consumo,ciudad)
		total_megavatios=sum(list(plantas_ciudad.values()))
		totalXregion+=total_megavatios

	return totalXregion	


####################################################################################################################################################################
# Una función facturacion(consumo_energia) que recibe el diccionario consumo_energia y 
# genera un archivo con la facturación total en dólares de los seis primeros meses de cada planta 
# generadora. El archivo resultante se llamará 'facturacion.txt' y tendrá la siguiente estructura: (15 puntos)
def facturacion(consumo:str):
	arch=open('Clase 07.18\\facturacion.txt','w')
	arch.write("Facturacion\n")
	for central in consumo:
		arch.write(central+'\n')
		for ciudad in consumo[central]:
			totalAnual=total_anual(consumo,central,ciudad)
			arch.write("{}: {} megavatiosXhora consumidos\n".format(ciudad,totalAnual))
			totalDolares=totalAnual*consumo[central][ciudad]['tarifa']
			arch.write("Total a pagar por el consumo: ${}\n".format(totalDolares))
			arch.write("\n")
		arch.write("*"*20+"\n")
	
	arch.close()
	print('Archivo creado')

####################################################################################################################################################################
#main

#Funcion 1
# x=total_anual(consumo_energia,'Coca Codo Sinclair','Quito')
# print(x)


#Funcion 2
# x=totalPlantas_ciudad(consumo_energia,'Guayaquil')
# print(x)


#Funcion 3
# x=megavatios_hora(consumo_energia,informacion)
# print(x)


#Funcion 4
x=facturacion(consumo_energia)