# Implemente la función palabras_coincidentes(lista_refranes) que recibe una lista con varias frases como texto. 
# Cada frase de la lista está compuesta solo de palabras separadas por un espacio en blanco entre palabras 
# (no hay comas, puntos o ningún otro tipo de símbolos). 
# La función retorna una lista con las palabras repetidas entre pares adyacentes de frases. 
# Asegúrese que cada elemento de la lista resultante se incluya UNA sola vez en el resultado.

# Ejemplo, dada la lista refranes:

refranes = ["Al que madruga Dios lo ayuda", "Al pan pan y al vino vino", "Soy espejo y me reflejo", 
            "Programar es lo más parecido a un superpoder"]


def coincidentes(l_refranes):
  repetidas=[]
  for i in range(len(refranes)-1):#---->0 2
    r1=refranes[i].split(' ')#lista con el primer refran
    r2=refranes[i+1].split(' ')#lista con el segundo refran
    for palabra in r1:
      for palabra2 in r2:
        if palabra.lower()==palabra2.lower() and palabra not in repetidas:
          repetidas.append(palabra)
  
  return repetidas


x=coincidentes(refranes)
print(x)

