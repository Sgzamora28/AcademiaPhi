#Tema 1
def buscar_palindromos(mensaje):
    resultado=[]
    for palabra in mensaje.split(" "):
        if len(palabra)>=3 and palabra==palabra[::-1]:
            resultado.append(palabra)

    return resultado


#main
mensaje='ana y yo somos amigos y trabajamos en la torre del radar'
# print(palindromos(mensaje))


##############################################################################
##############################################################################
#Tema 2
#todos los strings los vamos a trabajar en minuscula
palabra=input("Ingresa tu palabra: ").lower()#"hola"
#crear una variable pivote
frase=""
#crear una condicion
#"final" not in frase
#while frase!="final"
#hasta
contador=0
while not(frase=="final"):
    #actualizar la varaible pivote
    frase=input("Ingrese una frase: ").lower().replace(",","").replace(".","")#"Hola, estoy bien"---> "hola estoy bien"
    if frase!="final":
        palabras=frase.split(" ")#['hola','estoy','bien']
        contador+=palabras.count(palabra)

print(f"La palabra {palabra} se repitio {contador} veces")

##############################################################################
##############################################################################

#Tema 3
#comunes=["el","y","la","son"]
def siglas(frase, comunes):#"el ying y el yang..."
    sigla=""
    palabras=frase.split(" ")#['el','ying','y','el','yang',...]---> len()=10
                             #len()-1
                             #10
            #range(10) -----> [0,10) ---> [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(palabras)):
        if i==0 or i==(len(palabras)-1):#'el'
            sigla+=palabras[i][0]#'e'

        else:
            if palabras[i] not in comunes:
                sigla+=palabras[i][0]

    return sigla.upper()

'EYYCFCC'
##############################################################################
##############################################################################

#Tema 4
def rotacion_parcial(numeros,n):
    nueva=numeros.copy()
    escogido=nueva.pop(n-1)#2
    nueva.insert(escogido,0)
    return nueva

##############################################################################
##############################################################################

#Tema 5
def divisores(numeros,divisor):
    divisibles=[]
    for numero in numeros:
        if numero%divisor==0:
            divisibles.append(numero)

    return divisibles

#main
import random as rd
aleatorios=rd.sample(range(5,421),32)
aleatorios=[]
# while len(aleatorios)!=32:
#     n=rd.randint(5,420)
#     if n not in aleatorios:
#         aleatorios.append(n)

print(f"aleatorios={aleatorios}")
numero=rd.randint(6,19)
print(f"numero aleatorio={numero}")
lista=divisores(aleatorios,numero)
print("divisores",lista)

            



