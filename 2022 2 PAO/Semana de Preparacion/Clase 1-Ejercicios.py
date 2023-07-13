# Ejercicio1
# Escriba un programa, que pida el numero de galones de gasolina, y nos muestre sus equivalencias de litros, barriles de petróleo, 
# libras de CO2, precio en dólares. Las equivalencias son:
# 1. Un galon son 3.785 litros   
# 2. Un barril de petróleo produce 19.5 galones de gasolina
# 3. Un galon de gasolina produce 20 libras de CO2
# 4. Un galon de gasolina cuesta$2.98


# Por ejemplo:
# Numero de galones: 57
# 57 galones equivalen a:
# - 215.75 litros
# - 2.92 barriles de petróleo
# - 1140 libras de CO2
# - $169.86


# galones=float(input("ingese el numero de galones: "))
# litros=galones*3.785
# barriles=round(galones/19.5,2)
# librasCO2=galones*20
# precio=galones*2.98

# print(galones,"galones equivalen a:",litros,"litros")#60 galones equivalen a: ### litros
# print(galones,"galones equivalen a:",barriles,"barriles")
# print(galones,"galones equivalen a:",librasCO2,"libras de CO2")
# print(galones,"galones equivalen a:",round(precio,2),"dolares")




#Ejercicio 2
#Calcule el IMC de una persona. Para ello, pida por teclado al usuario que ingrese su estatura y su peso
#La formula del IMC peso/altura**2

peso=input("Ingrese su peso en kg: ")
altura=input("Ingrese su altura en m: ")
imc=float(peso)/(float(altura)**2)
print("El imc de la persona es igual a:",round(imc,2))