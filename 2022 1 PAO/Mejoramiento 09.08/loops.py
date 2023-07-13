import random as rd
i=0

# x=rd.randint(0,2)
# print(x)
# x=rd.randrange(30)
#repetir hasta que imprima 15


# while i!=15:
#   print(i)
#   i+=1


edad=""
#condiciones correctas---> edad.isdigit()
while not(edad.isdigit()):
  edad=input("Ingrese su edad: ")


edad=int(edad)



nacimiento=2022-edad
print(nacimiento)
