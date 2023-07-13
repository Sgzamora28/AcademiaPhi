# TEMA 4
# Implemente la función justificar(linea, tamaño) que recibe una línea de texto y un entero. 
# Suponga que la línea está compuesta por dos o más palabras separadas por un espacio en blanco y 
# que su longitud es menor a tamaño. En la línea no hay dígitos ni símbolos especiales (solo letras y espacios en blanco).
# Entonces, su función debe completar la longitud de la línea hasta llegar a ser exactamente igual a tamaño. 
# Para esto, agregue lo más equitativamente posible espacios en blanco entre las palabras de la línea empezando 
# desde la izquierda. Observe que la nueva línea no puede empezar ni terminar con espacios en blanco.
# La función debe retornar esta nueva línea.
# Si se pide justificar a tamaño 61 la frase:
# "Este es un buen día para aprobar fundamentos"
# La función retornaría:
# "Este--- es--- un--- buen-- día-- para-- aprobar-- fundamentos"
# #Observe que estamos usando "-" en nuestro ejemplo para representar los espacios en blanco añadidos. 
# # En la solución final no se debe de usar "-" sino espacios en blanco

#Forma 1
# def justificar(linea:str,tamanio:int):
#   justificacion=""
#   lista=linea.split(" ")#[Este,es,un,buen,día,para,aprobar,fundamentos]  len--> 8
#   i=0
#   while len(justificacion)!=tamanio:
#     lista[i]+=" "#lista[i]=lista[i]+"-" ----> "Este-"
#     justificacion=" ".join(lista)#"Este- es un buen día para aprobar fundamentos"

#     if i==(len(lista)-2):
#       i=0
#     else:
#       i+=1

#   return justificacion


#Forma 2
def justificar(linea:str,tamanio:int):#8 palabras
  longitud=len(linea)
  vacios=linea.count(" ")#7 espacios
  faltantes=tamanio-longitud #17
  lista=linea.split(" ")#[Este-,es-,un-,buen,día,para,aprobar,fundamentos]
  agregar=faltantes//vacios #2
  sobrante=faltantes%vacios #residuo de 17/7 ---> 3
  espacios=" "*(agregar+1)
  for i in range(sobrante):
    lista[i]+=" "

  justicacion=espacios.join(lista)

  return justicacion
  





#main
palabra="Este es un buen día para aprobar fundamentos"
nueva=justificar(palabra,61)
print(palabra,len(palabra))
print(nueva,len(nueva))