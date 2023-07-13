# Asuma que tiene un diccionario con el siguiente formato:
# Clave: [Nombre, Carrera, tupla de notas]
# Ejemplo:
d_valores = {
             202212345:["Juan Romero", "Computacion", (100, 75, 69)],
             201854832:["Gabriela Herrera", "Turismo",(94, 99, 86, 89)],
             202101713:["Fernando Suarez","Electronica y Automatizacion",(90,60,83,66,74)]
            }
# Escriba la información del diccionario en un archivo con nombre dataset.csv con el siguiente formato:
# Matricula,Nombre,Carrera,Promedio de notas

with open("2ndo Examen\\dataset1.csv","w") as arch:
  for matricula,datos in d_valores.items():
    promedio=sum(datos[2])/len(datos[2])
    arch.write("{},{},{},{:.2f}\n".format(matricula,datos[0],datos[1],promedio))