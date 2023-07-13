import funciones_main as fm
# from funciones_main import 
#definir una funcion que recibe una lista de valores marcados en un radar y un valor de kilometros maximo. La funcion retorna una tupla que contenga aquellos valores
#que superen el valor maximo  
#[100, 110, 90, 85, 60]
#90
# 0     1    2   3   4
#main
l_radar=[100, 110, 90, 85, 60]
# km_maximo=80
multados=fm.multas(maximo=80,lista=l_radar)
print(multados)

#desempaquedo
l1=('Steven','Zamora',20)
nombre,apellido,edad=l1
print(nombre)

#operaciones con tuplas