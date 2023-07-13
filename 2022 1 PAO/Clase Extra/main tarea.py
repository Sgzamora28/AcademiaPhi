from funciones_tarea import buscar_por_edades

nombres = ["Morty", "Venus", "Pikachu", "Piolin", "Chumi"] 
especie = ["Gato", "Perro", "Hamster", "Ave", "Tortuga"] 
peso = [4.6, 11.0, 0.04, 0.3, 1] 
edad = [4, 3, 1.5, 3, 2]

# resultado=buscar_por_edades(2,3,nombres,edad)
# print(resultado)

#ejemplo verificacion
#verifique que una cedula ingresada por el usuario cumple las condiciones de la misma.
#condiciones correctas----> cedula.isdigt() and len(cedula)==10
# cedula=input('Ingrese su cedula: ')#---->'1303408189'
#not(cedula.isdigit() and len(cedula)==10)
# while not cedula.isdigit() or len(cedula)!=10:
#     cedula=input('No seas mamerto, ingresa bien la cedula: ')

# cedula=int(cedula)



#MAIN
nombre=input('Ingrese el nombre de su mascota')
#condiciones---->nombre in nombres
while nombre not in nombres:
    nombre=input('Acaso no conoces el nombre de tu mascota, mmvrg: ')

i=nombres.index(nombre)
e=especie[i]
p=peso[i]
ed=edad[i]
print('Para la mascota {}:\nSu especie es {}\nSu edad es {}\nSu peso es {}\n'.format(nombre,e,ed,p))
