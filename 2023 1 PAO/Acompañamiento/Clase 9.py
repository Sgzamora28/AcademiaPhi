# import random as rd
# def crearLista(numero:int):
#   lista=[]
#   for i in range(numero):
#       cedula=""
#       for i in range(10):
#           cedula+=str(rd.randint(0,9))
#       generos=["M","F"]
#       genero=rd.choice(generos)
#       estatura=1
#       if genero=="F":
#         estatura+=round(rd.uniform(0.4,0.7),2)
#       else:
#          estatura+=round(rd.uniform(0.6,1),2)
#       peso=round(rd.uniform(50,70),2)
#       lista.append("{}|{}|{}|{}".format(cedula,genero,estatura,peso))
#   return lista
# ##########################################################################
datos=['0706017522|F|1.53|56.4','1306607647|M|1.64|70',...]
# print(datos)


#1. Estatura promedio de mujeres
estatura_m=[]
#2. Estatura promedio de varones
estatura_h=[]
for dato in datos:
  cedula,sexo,estatura,peso=dato.split("|")#["0328669318","M","1.71","58.69"]
                                            #['8756093550','F','1.63','64.71']
  if sexo=="M":
     estatura_h.append(float(estatura))
  else:
     estatura_m.append(float(estatura))


promedio_m=sum(estatura_m)/len(estatura_m)
promedio_h=sum(estatura_h)/len(estatura_h)
print("El promedio de altura de hombres es",round(promedio_h,2))
print("El promedio de altura de mujeres es",round(promedio_m,2))


#top 3 de alturas entre hombres y mujeres
estaturas=estatura_h+estatura_m
#.sort ordena de menor a mayor
#cuando quiero tops quiero los valores del mayor al menor, entonces al sort le agrego el ---> reverse=True
estaturas.sort(reverse=True)
top3=estaturas[:3]   #[0,3) 0 1 2
print(top3)


############################################################
############################################################
#Solicitar un presupuesto y luego pedir precios de productos y el programa finaliza cuando el total de los precios 
#alcance el presupuesto inicial

presupuesto=float(input("Ingrese su presupuesto: "))
#total de productos alcance al presupuesto
#Hasta cuando se repite el programa?
#total>=presupuesto
#2. negarlo
#not(total>=presupuesto)
#total<presupuesto
total=0
while not(total>=presupuesto):
    precio_producto=float(input("Ingrese el precio del producto a comprar: "))
    total+=precio_producto
    saldo=presupuesto-total
    print("Usted ha gastado",total)
    print("A usted le quedan",saldo)


###############################################################
###############################################################
# Implementar un programa en Python que solicite al usuario ingresar el tiempo disponible que 
# tiene para su rutina de ejercicios, y generar una combinación de ejercicios que puede hacer en dicho tiempo o menos, 
# sin excederlo. Al finalizar se muestra una lista de ejercicios y la suma total de tiempo. 
# La rutina no puede tener ejercicios repetidos. 
# Usted dispone de las siguientes listas con los ejercicios y con el tiempo en minutos de cada ejercicio. 
# Ejemplo de las listas: 
ejercicios = ['sentadillas', 'flexiones', 'trotar', 'abdominales','suicidio','plancha','saltar cuerda'] 
#                  0                                                                       len()-1
minutos = [10, 12, 22, 15,20,7,23] 
# Ejemplo: 
# Ingrese un tiempo mínimo: 40 
# Rutina sugerida: ['sentadillas', 'flexiones', 'abdominales'] 
# Total de minutos: 37 
# En el ejemplo se puede observar que no se recomienda trotar porque su tiempo es de 22 minutos, 
# que sumados a los ejercicios anteriores, pasa de los 40 mínimos que solicita el usuario.
import random as rd
tiempo_minimo=int(input("Ingrese un tiempo minimo: "))#30
total=0#25
rutina=[]
#Tengo que repetir el programa HASTA que la lista de ejercicios no tenga elementos o 
# el total sea igual o cercano a al tiempo que ingresa el usuario
#total>=minutos
while not(len(ejercicios)==0):
    aleatorio=rd.randrange(len(ejercicios)) #[0,len()-1]
    ejercicio=ejercicios[aleatorio]
    t=minutos[aleatorio]#7
    ejercicios.pop(aleatorio)
    minutos.pop(aleatorio)  
    if (total+t)<=tiempo_minimo:
      total+=t
      rutina.append(ejercicio)


    
print("Rutina sugerida:",rutina)
print("Total de minutos:",total)