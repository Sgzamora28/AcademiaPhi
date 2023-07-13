#estructuras logicas

#Ejercicio 1
# peso=float(input("Ingrese su peso en kg"))
# altura=float(input("Ingrese una altura en m"))
# imc=peso/altura**2
# print(imc)
# if imc<18.5:
#   print("Usted tiene un peso bajo")

# elif 18.5<=imc<=25:
#   print("Usted tiene un peso regular")

# else:
#   print("Usted tiene sobrepeso")






#estrucutras de repeticion---> loops o iterativas

#cuando conozcono el numero de repeticiones

#---> for por indices
palabra="parangaricutirimicuaro"
# for i in range(len(palabra)):
#   print(i,palabra[i])


#---> for por contenido
i=0
for letra in palabra:
  # print(i,palabra[i])
  i=i+1

#cuando no conozco el numero de repeticiones
# lista_prueba=[]
# while len(lista_prueba)!=5:
#   numero=input("Ingrese un numero correspondiente: ")
#   lista_prueba.append(numero)

# print("Continue utilizando nuestros servicios...")


# #comprobaciones
# cedula=input("ingrese una cedula: ")
# #condiciones validas--> cedula.isdigit() and len(cedula)==10
# while not(cedula.isdigit() and len(cedula)==10):
#   cedula=input("ingrese un numero de CI adecuado: ")




# tabla=int(input("Ingrese un numero para generar su tabla de multplicar: "))

# for i in range(12):
#   multplicacion=(i+1)*tabla
#   print("{}x{}={:>d}".format(tabla,i+1,multplicacion))



#ejercicio 4
pokemons= ["omanyte","blastoise","venomoth","alakazam","vulpix","rapidash"]
puntosCombate=[]
for i in range(len(pokemons)):
  print("Ingrese los puntos de Ataque y defensa para el pokemon {}".format(pokemons[i]))
  pa=float(input("Puntos de Ataque: "))
  pd=float(input("Puntos de Defensa: "))
  pc=(pa+pd)*1.2
  puntosCombate.append(pc)

promedio=sum(puntosCombate)/len(puntosCombate)
masAlto=max(puntosCombate)
i_masAlto=puntosCombate.index(masAlto)
pokemonGanador=pokemons[i_masAlto]
print("El promedio de los puntos de combate es igual a {:.2f}".format(promedio))
print("Los puntos de combate mas altos son {} y pertenecen al pokemon {}".format(masAlto,pokemonGanador))



