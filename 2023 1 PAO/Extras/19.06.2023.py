
#crear la variable de confirmacion
#numero=0
#crear la estructura condicional
#numero==-1
#negamos
#not(numero==-1)
#Creas el while y dentro del while tienes que actualizar la variable

#while [estructura condicional]:


#repetir HASTA que el numero que ingrese el usuario sea -1
numero=int(input("Ingrese un numero: "))#20
sumatoria=numero
while not(numero==-1):
  numero=int(input("Ingrese un numero: "))
  if numero!=-1:
    sumatoria+=numero 

print(sumatoria)


#1. crear la variable
cedula=input("Ingrese cedula: ")
#2. saber cuales son las condiciones de la variable
#cedula debe ser numerica y debe tener 10 digitos
#cedula.isgidit() and len(cedula)==10
#3. negar las condiciones dentro de la estructura while
# while not(cedula.isgidit() and len(cedula)==10):
#     #4. actualizar la variable dentro del while
#     cedula=input("Ingrese una cedula correcta: ")
