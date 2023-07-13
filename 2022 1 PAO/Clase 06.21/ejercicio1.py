import funciones_ej1 as ej1
nombres = ["Morty", "Venus", "Pikachu", "Piolin", "Chumi"] 
especie = ["Gato", "Perro", "Hamster", "Ave", "Tortuga"] 
peso = [4.6, 11.0, 0.04, 0.3, 1] 
edad = [4, 3, 1.5, 1, 2]

n_mascotas=ej1.buscar_por_edades(2,5,nombres,edad)
print(n_mascotas)