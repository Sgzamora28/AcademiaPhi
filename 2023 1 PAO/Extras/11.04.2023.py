#Como desempaquetar datos
#IMPORTANTE PARA ARCHIVOS

familia=["Steven Zamora","Kyra Franco","Isa Zamora Franco"]
papa,mama,hijo=familia #["Steven Zamora","Kyra Franco","Isa Zamora Franco"]


#Ejercicio
# Escriba un programa que pida los nombre, apellidos y edad de una persona separados por comas, 
# y los muestre con formato:
# Información: juAn,peREz,44
# La persona es Juan Perez, de 44 años.

# "steven zamora" ----.upper---> "STEVEN ZAMORA"
# "steven zamora" ----.lower---> "steven zamora"
# "steven zamora" -.capitalize-> "Steven zamora"
# "steven zamora" ----.title---> "Steven Zamora"

# informacion=input("Por favor, ingrese sus datos: ").title()
# datos=informacion.split(",")
# # print("La persona es",datos[0],datos[1],", tiene",datos[2],"anios.")
# print("La persona es {} {}, tiene {} anios.".format(datos[0],datos[1],datos[2]))



# Quieres escribir un programa para manipular el DNA, que son secuencias de letras A, T, C y G. 
# Quieres extraer un parte de una secuencia, y buscar si esta aparece en otra secuencia. 
# Por ejemplo:
# Secuencia original: ATCCGTAGCGTAATCCATGCATTATC
# Extraer desde posición: 4
# Extraer hasta posición 9
# Secuencia extraída: GTAGCG
# Secuencia a BUSCAR: TTGACTATAGCCAAGCGTAGCGAAAAAATTC
# Se encontró la secuencia extraída en la secuencia a buscar: true

secuencia=input("Por favor ingrese la secuencia: ")
inicial=int(input("Extraer desde posicion: "))
final=int(input("Extraer hasta posicion: "))
extraida=secuencia[inicial:final+1]
print("Secuencia extraida:",extraida)
buscar=input("Secuencia a BUSCAR: ")
busqueda=extraida in buscar
print("Se encontró la secuencia extraída en la secuencia a buscar:",busqueda)
