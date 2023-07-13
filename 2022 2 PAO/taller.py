archivo=open("Estudiantes.txt")
diccionario={}
for line in archivo:
  nombres,matricula,facultad,carrera,cedula=line.strip().split(":")
  nombres=nombres.split("-")
  nombres=nombres[2]+" "+nombres[0]+" "+nombres[1]

  diccionario[cedula]=[nombres,matricula,facultad,carrera]

archivo.close()
print(diccionario)



# Pregunta 2
materias={}
archivo=open("Materias.csv")
for line in archivo:
  codigo,nombre,facultad,paralelo=line.strip().split(",")
  valor="{}-{}#{}".format(nombre,facultad,paralelo)
  materias[codigo]=valor
print(materias)


#Pregunta 3


f1="-"
f2=""
while f1!=f2:
  cedula=input("Escriba la cedula del estudiante: ")
  codigo=input("Escriba el codigo de su materia")
  while cedula not in diccionario:
    cedula=input("El estudiante no esta registrado. Ingrese de nuevo: ")
  while codigo not in materias:
    codigo=input("La materia no esta registrada. Intente de nuevo: ")
  
  f1=materias[codigo].split("-")[1].split("#")[0]
  f2=diccionario[cedula][-2]

