# Escriba un programa en Python que calcule el puntaje de las películas contenidas en la lista de películas del año para determinar la mejor pelicula: 
films = ["logan","alien","la bella y la bestia","rapidos y furiosos", "star wars","spiderman","piratas del caribe"]
#puntos=[3.5, 3.9, 3.3, 7.1, 6.1, 3.9, 5.8]
# El programa pide al usuario que ingrese sus puntos en libreto (L), música (M) y efectos especiales (E) de cada película. 
# Los puntos deberán estar dados por valores entre 0 y 10, lo que permitirá realizer la conversion a estrellas posteriormente. 
# El programa que usted diseñe calcula los puntos de la película (PP) a través de la siguiente fórmula:
# PP = 0.5*L + 0.3*M + 0.2*E
# Usted debe ir añadiendo los puntos a una nueva lista llamada lista_pts

lista_pts=[]
# for pelicula in films:
#     print('Ingrese el puntaje para la pelicula',pelicula)
#     #condiciones correctas l.isdigit() and 0<=l<=10
#     l=input('Ingrese el puntaje por libreto: ')
#     while not(l.isdigit() and 0<=int(l)<=10):
#         l=input('Ingrese el puntaje por libreto: ')
#     l=int(l)

#     m=input('Ingrese el puntaje para la musica: ')
#     while not(m.isdigit() and 0<=int(m)<=10):
#         m=input('Ingrese el puntaje para la musica: ')
#     m=int(m)

#     e=input('Ingrese el puntaje para los efectos especiales: ')
#     while not(e.isdigit() and 0<=int(e)<=10):
#         e=input('Ingrese el puntaje para los efectos especiales: ')
#     e=int(e)

#     pp=0.5*l+0.3*m+0.2*e
#     lista_pts.append(pp)
# print(lista_pts)
lista_pts=[3.5, 3.9, 3.3, 7.1, 6.1, 3.9, 5.8]
mejor=max(lista_pts)
stars=mejor//2
indice_mayor=lista_pts.index(mejor)
mejor_pelicula=films[indice_mayor]
promedio=sum(lista_pts)/len(lista_pts)
print('La pelicula con mayor puntacion fue {} con una cantidad de {} estrellas. El promedio de todas las peliculas fue {:.2f}'.format(mejor_pelicula,stars,promedio))
#pelicula: puntaje
# muestra=[]
# for i in range(len(films)):
#     pelicua_pp=films[i]+': '+str(lista_pts[i])
#     muestra.append(pelicua_pp)

# print(muestra)