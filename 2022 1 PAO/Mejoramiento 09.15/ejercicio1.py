# Asuma que tiene una lista T de términos. Un término puede ser una palabra o uno de los siguientes tres símbolos:
# punto (.), coma (,) y guión (-). Desarrolle un programa que forme un texto usando las siguientes reglas:
# ● El texto debe estar compuesto de 73 términos seleccionados aleatoriamente 
# ● El primer término debe ser una palabra
# ● No se puede seleccionar dos símbolos de manera consecutiva. Si eso pasa, seleccione un nuevo término
# aleatoriamente hasta que sea una palabra
# ● Dos palabras seguidas deben estar separadas por un espacio. Ejemplo: palabra1 palabra2
# ● La coma debe estar pegada a la palabra a su izquierda y separada por un espacio de la palabra a su derecha.
# Ejemplo: palabra1, palabra2
# ● El guión debe estar pegado a sus dos palabras. Ejemplo: palabra1-palabra2
# ● El punto debe estar pegado a la palabra de la izquierda y seguido de un salto de línea. Ejemplo: palabra1.
# ● No elimine términos de la lista T.
# Escriba este texto resultante en un archivo de nombre literatura.txt

import random as rd

terminos=["azul", "efimero", "magico",".",",","-","manzana","aprobacion"]

secuencia=""
comprobador=False#comprobador de si el termino anterior fue un simbolo
comprobador2=False
for i in range(73):
  x=rd.choice(terminos) #"." "," "-"
  while comprobador and (x=="," or x=="-" or x=="."):
    x=rd.choice(terminos)
    if x!="," and x!="-" and x!=".":
      comprobador=False


  #para la primera vuelta
  if i==0:
    while x=="," or "x"=="." or x=="-":
      x=rd.choice(terminos)


  #si el termino fue un simbolo
  if x=="," or x=="." or x=="-":
    comprobador=True
  
  
  #espaciado
  if x==",":
    secuencia=secuencia[:-1]
    secuencia+=f"{x} "

  elif x=="-":
    secuencia=secuencia[:-1]
    secuencia+=x
  
  elif x==".":
    secuencia=secuencia[:-1]
    secuencia+=f"{x}\n"
    comprobador2=True

  else:
    if comprobador2:
      secuencia+=f"{x.title()} "
      comprobador2=False

    else:
      secuencia+=f"{x} "



print(secuencia)


# arch=open("literatura.txt","w")
# arch.write(secuencia)
# arch.close()


with open("literatura.txt","w") as arch:
  arch.write(secuencia)