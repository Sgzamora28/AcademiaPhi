import f_ejercicio2 as ej2

nombre=input('Ingrese su nombre: ')
promedios=ej2.solicitar()
# print(promedios)
promedio=ej2.promedio(promedios)
categoria=ej2.categoria(promedio)

print('Par el estudiante {}, el promedio es {:.2f} que correscompe a la categoria {}'.format(nombre,promedio,categoria))
