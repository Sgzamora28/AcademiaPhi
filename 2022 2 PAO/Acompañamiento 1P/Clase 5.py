#####################################
############ Ejercicio 1 ############
#####################################
#ISBN condiciones:
#
# 13 digitos

def verificar(isbn):
  #isbn= 9 7 8 3 1 6 1 4 8 4  1  0  0
  #      0 1 2 3 4 5 6 7 8 9 10 11 12
  retorno=False
  #Primeras condiciones
  #isbn.isdigit() and len(isb)==10
  if isbn.isdigit() and len(isbn)==13:
    suma=0
    for i in range(len(isbn)):
      #Modulo es una funcion que retorna el residuo---> 
      if i%2==0:
        x=int(isbn[i])*1
      else:
        x=int(isbn[i])*3
      suma+=x

    residuo=suma%10
    resultado=10-residuo

    if resultado==10:
      verificador=0

    else:
      verificador=resultado
    
    if verificador==int(isbn[-1]):
      retorno=True

    else:
      retorno=False

  else:
    retorno=False

  return retorno


# usuario=input("Ingrese un valor de ISBN: ")
# prueba=verificar(usuario)
# print(prueba)


#####################################
############ Ejercicio 2 ############
#####################################


productos=["Huevos","Carne","Queso","Mantequilla","Leche"]
precios=[2.5,3,3.15,1.20,1]

#Literal a
promedio=sum(precios)/len(precios)

mayores=0
for i in range(len(precios)):
  if precios[i]>promedio:
    mayores+=1

# print(f"Hay {mayores} productos que superan al promedio")



#####################################
############ Ejercicio 3 ############
#####################################
# import random as rd

# cantidad=int(input("Ingrese un valor: "))
# l1=[]
# l2=[]

# for i in range(cantidad):
#   x=rd.randint(1,9)
#   y=rd.randint(1,9)
#   l1.append(x)
#   l2.append(y)

# print(f"Las listas obtenidas son\n{l1}\n{l2}")

# l1_nueva=[]
# l2_nueva=[]

# for i in range(len(l1)):
#   if l1[i]!=l2[i]:
#     l1_nueva.append(l1[i])
#     l2_nueva.append(l2[i])

# l1=l1_nueva
# l2=l2_nueva

# print(f"Listas despues de la modificacion:\n{l1}\n{l2}")

#####################################
############ Ejercicio 4 ############
#####################################
import random as rd
paises=["Ecuador","Argentina","Uruguay","Bolivia","Chile","Colombia","Peru","Brasil","Venezuela","Paraguay"] 
puntos=[9,10,6,1,5,4,3,12,2,7]

#Planificar los partidos
anfitriones=[]
visitantes=[]
#condiciones correctas--> len(anfitriones)==5 and len(visitantes)==5

while not(len(anfitriones)==5 and len(visitantes)==5):
  visitante=rd.choice(paises)
  anfitrion=rd.choice(paises)
  #condicion del visitante y del anfitrion---> visitante!=anfitrion and visitante not in anfitrioones and visitante not in visitantes and 
  #anfitrion not in anfitriones and visitante not in visitantes
  if visitante!=anfitrion and visitante not in anfitriones and visitante not in visitantes and anfitrion not in anfitriones and anfitrion not in visitantes:
    anfitriones.append(anfitrion)
    visitantes.append(visitante)


print("a) Los equipos se enfrentaran de la siguente manera:")
for i in range(len(visitantes)):
  print(f"{anfitriones[i]} vs {visitantes[i]}")
print()


#Goles en partido
golesV=[]
golesA=[]

for i in range(5):
  golA=rd.randint(0,5)
  golV=rd.randint(0,5)
  golesA.append(golA)
  golesV.append(golV)

print(f"b) Goles en partido:\n{golesA}\n{golesV}\n")



#Resultados
pt_actual=puntos.copy()
for i in range(len(golesA)):
  if golesV[i]>golesA[i]:
    print(f"En el partido {anfitriones[i]} vs {visitantes[i]} gano {visitantes[i]}")
    x=paises.index(visitantes[i])
    pt_actual[x]+=3

  elif golesA[i]>golesV[i]:
    print(f"En el partido {anfitriones[i]} vs {visitantes[i]} gano {anfitriones[i]}")
    x=paises.index(anfitriones[i])
    pt_actual[x]+=3
  else:
    print(f"En el partido {anfitriones[i]} vs {visitantes[i]} hubo empate")
    x=paises.index(visitantes[i])
    y=paises.index(anfitriones[i])
    pt_actual[x]+=1
    pt_actual[y]+=1

    
print("\nActualizacion de puntos:\n")
print(f"{puntos}\n{pt_actual}")


#Mas puntos antes de la fecha
mas_puntaje=max(puntos)
i_mp=puntos.index(mas_puntaje)
print(f"\nd) El pais con mayor puntaje antes de la fecha es:\n{paises[i_mp]}\n")


#Top 5
#A la primera copia la ordena
copia_puntos1=pt_actual.copy()
#A la segunda copia la mantengo igual
copia_puntos2=pt_actual.copy()
#[----0,0,10-----]

copia_puntos1.sort(reverse=True)
for i in range(5):
  i_original=copia_puntos2.index(copia_puntos1[i])
  print(paises[i_original],copia_puntos1[i])
  copia_puntos2[i_original]=0
