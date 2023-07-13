# Suponga que se le da un bloque de texto con diferentes palabras. Estas palabras están separadas por un espacio en
# blanco o un punto. No habrán dos o más espacios en blanco seguidos o combinaciones de espacios en blanco y
# puntos. No habrán vocales con tildes en el texto. Pueden haber números en el texto pero no se consideran palabras
# en esta misión (una mezcla de letras y dígitos no es una palabra tampoco).
# Usted debe contar el número de palabras que tienen la misma cantidad de vocales y consonantes. Las mayúsculas y
# minúsculas no son significativas para esta misión.
# Desarrolle un programa en Python que pida un bloque de texto por teclado y muestre por pantalla la cantidad de
# palabras que cumplen con la descripción anterior.

vocales="aeiou"
consonantes="bcdfghjklmnpqrstvwxyz"

ingreso=input("Ingrese una palabra o una oracion por teclado: ").lower().replace(" ",".")
# print(ingreso)


oracion=ingreso.split(".")
# print(oracion)

contador=0
for palabra in oracion:
  if palabra.isalpha():
    # print(palabra)
    total_consonantes=0
    total_vocales=0
    for letra in palabra:
      if letra in vocales:
        total_vocales+=1

      else:
        total_consonantes+=1

    if total_consonantes==total_vocales:
      contador+=1

print("La oracion tiene {} palabras que cumplen la condicion".format(contador))