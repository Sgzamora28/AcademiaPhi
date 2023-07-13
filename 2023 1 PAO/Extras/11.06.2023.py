texto=input("Ingrese un oracion: ")#La raiz cuadrada de 36 es 6
#input()---> str 
palabras=texto.split(" ") #["La","raiz","cuadrada","de","36","es","6"]
# print(palabras)
#for [variable] in [lo que queremos iterar]:

p=0 #contador de palabras
n=0 #contador de numeros

for palabra in palabras:
    if palabra.isalpha():#aqui le estoy preguntando si el str olo tiene caracteres
        p+=1 #si es asi, le sumo uno al contador de palabras
    else:#El caso contrario seria que el str contenga solo numeros
        n+=1 #entonces se le suma uno al contador de numeros

#La oracion contiene unicamente palabras n==0
if n==0:
    print("El texto ingresado solamente contiene palabras")
#La oracion contiene unicamente numeros  p==0
elif p==0:
    print("El texto ingresado solamente contiene numeros")

#La oracion contiene numeros y palabras  
else:
    print("El texto ingresado contiene numeros y palabras")

print(f"Total palabras: {p}")
print(f"Total numeros: {n}")


#################################################################
#################################################################
ingredientes=["jamon","queso","tomate","albahaca","peperoni","aceitunas","champiñones","carne"]

#################################################################
import random as rd
tamanio=input("Ingrese el tamaño de su pizza: ")
cantidad=int(input("Ingrese la cantidad de ingredientes: "))
seleccion=rd.sample(ingredientes,cantidad)

#Depende del tamanio, le asigno un valor a la variable
if tamanio=="personal":
    valor=5
elif tamanio=="mediana":
    valor=7
else:
    valor=10

#Aqui pregunto si hay mas de dos ingredientes
if cantidad>2:
    extra=cantidad-2#Si hay 4 ingredientes, los ingredientes extras seran 4-2=2
    valor+=2*extra#por cada ingrediente extra le sumo dos dolares a la variable valor
valor=round(valor,2)
print("Se selecciono pizza",tamanio)
print("Se eligieron los siguiente ingredientes:")
#Aqui imprimo ingrediente por ingrediente
for ingrediente in seleccion:
    print("*",ingrediente.title())
print("El total a pagar es",valor)
#################################################################
#################################################################
datos=["Juan Perez-18","Julia Ramos-19","Maria Olaya-18","Juan Arcos-20","Ana Perez-16",
       "Kyra Franco-20","Steven Zamora-21"]
#"Nombre-Edad"
#######################################################################
#1
mayores_edad=0#esta variable ira contando uno a uno las personas mayores de edad
for dato in datos:
    nombre,edad=dato.split("-")#"Steven Zamora","21"
    if int(edad)>=18:
        mayores_edad+=1#si encuentra una persona mayor de edad, a la variable le sumara 1

print(f"Hay {mayores_edad} personas mayores de edad")
#2
nombres=[]
edades=[]
for dato in datos:
    nombre,edad=dato.split("-")#"Steven Zamora","21"
    nombres.append(nombre)
    edades.append(int(edad))

edad_mayor=max(edades)#Aqui estoy buscando cual es la edad mayor
indice=edades.index(edad_mayor)#Aqui estoy buscando el indice de la edad mayor
nombre_mayor=nombres[indice]#Con el indice de la edad mayor en la lista de edades 
                            #estoy indexando el nombre de la persona que tiene esa edad
print("El nombre de la persona con mayor edad es",nombre_mayor)

#3
#Como ya tengo la lista de edades, simplemente saco su promedio
promedio=sum(edades)/len(edades)
promedio=round(promedio,2)
print("El promedio de edades es igual a",promedio)