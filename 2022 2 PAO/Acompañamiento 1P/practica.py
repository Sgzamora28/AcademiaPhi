#para importar random
import random as rd

# apellido=input("ingrese su apellido: ")
# edad=input("Ingrese su edad: ")
# print()


# print("nombre:",nombre)
# print("apellido:",apellido)
# print("edad:",edad)

print()

# print(edad,nombre,apellido,edad)


#funciones de random
nombre=input("Ingrese un nombre: ") #Azucena
# print(len(nombre))
#generar numero aleatorio desde a hasta b
#A z u c e n a ---> len()=7
#0 1 2 3 4 5 6
# aleatorio=rd.randint(0,len(nombre)) #----> 0,1,2,3,4,5,6,len()  --->7   [0,len()]
# aleatorio=rd.randrange(len(nombre)) #---> 0,1,2,3,4,5,6 [0,len())
#nombre[aleatorio]
# print("El numero aleatorio es:",aleatorio)
# print("La letra en el indice aleatorio es",nombre[aleatorio])

# letra=rd.choice(nombre) #Damino
# print(letra)
lista=[nombre,"Steven",20,"Kyra","Isabel"]
rd.shuffle(lista)
print(lista)