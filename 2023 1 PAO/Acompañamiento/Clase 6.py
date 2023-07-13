#########################################
#ESTRUCTURAS DE CONTROL
#########################################


#Esctructuras condicionales
# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un segundo numero: "))
# print("Elegir la operacion\n[0] Sumar\n[1] Restar\n[2] Multiplicar\n[3] Dividir")
# opcion=input("Escoja su opcion: ") # 0 -- str --> "0"
#                                    #  1 -- str --> "1"

# # name="steven"
# # print(name)
# # name="kyra"
# # print(name)

# #if [condicion]: 
#   #bloque de codigo que se ejecutara si se cumple la condicion
#   #bloque de codigo que se ejecutara si se cumple la condicion
#   #bloque de codigo que se ejecutara si se cumple la condicion

# if opcion=="0": #suma
#     print("Usted va a sumar los dos numeros")
#     resultado=num1+num2


# elif opcion=="1": #resta
#     print("Usted va a restar los dos numeros")
#     resultado=num1-num2

# elif opcion=="2":
#     print("Usted va a multiplicar los dos numeros")
#     resultado=num1*num2

# elif opcion=="3":
#     print("Usted va a dividr los dos numeros")
#     resultado=num1/num2

# else: #caso basura
#     print("Opcion no valida")
#     resultado="Syntaxis Error"



# print(resultado)
############################################
############################################

# numero=int(input("Ingrese un numero: "))

# #100%2 --> 0


# if numero%2==0:
#    print("Opcion 1")
#    resultado=numero**2 

# elif numero>=40:
#    print("Opcion 2")
#    resultado=numero**3

# else:
#    print("Opcion 3")  
#    resultado=numero//3

# print(resultado)
############################################
############################################
# numero=int(input("Ingrese un numero: "))
# opcion=""
# ###################
# if numero>40:
#     opcion="a"

# else:
#     opcion="b"
# ###################

# ###################
# if opcion=="a":
#     if numero==100:
#       print("Hola mundo")
#     else:
#         print("Hola luna")

# else:
#     if numero==5:
#       print("Me gusta programar")
#     else:
#        print("No me gusta programar")

#################################################
#################################################
#################################################

#Esctructuras iterativas/repiticion



#FOR

# for [variable] in [lo que queremos iterar/repetir]:

#OBJETOS ITERABLE
#str ---> "Hola"  ---> "H"+"o"+"l"+"a"
#listas-> ["Steven",21,"Mecatronica"]---> "Steven"  21 "Mecatronica"
#rango -> range(10) [0,10) ---> 0 1 2 3 4 5 6 7 8 9


# for i in range(10):
#    print(i)


# for x in "Hola":
#     print(x)

lista=["Steven",21,"Mecatronica","Zamora"]
#len---> 4
#         0      1      2           3
#                               len(lista)-1
# for elemento in lista:
#     print(elemento)


##################################

#FOR POR CONTENIDO 
# for elemento in lista:
#   print(elemento)

#FOR POR INDICE
#Cuando me interesa el indice del objeto
#Cuando tengo listas paralelas

#for [i] in range(len([objeto a iterar]))
# for i in range(len(lista)): #range(4)
#     print(i,lista[i])


#LISTAS PARALELAS
#Listas donde la informacion esta relacionada por el indice
#Las listas paralelas tienen todas la misma longitud
nombres=["Karen","Steven","Fernando","Azucena"]
edades =[20,21,20,19]
carreras=["Computacion","Mecatronica","Electricidad","Oceanografia"]

#Quiero mostrar la info de las personas que sean mayores a 20 anios

for i in range(len(edades)):
    if edades[i]>20:
      print("nombre:",nombres[i])
      print("carrera:",carreras[i])
