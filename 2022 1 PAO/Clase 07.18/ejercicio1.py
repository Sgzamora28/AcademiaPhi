#####################################################################################################################################
#Se necesita programar una manera de codificar y decodificar mensajes utilizando el alfabeto radiofonico, el cual es muy utilizado por los
#cuerpos policiales y militares. Para esto se dispone de una lista que contiene varias sublistas con cada una de las letras del alfabeto
#y su codificacion.  
from dataclasses import replace


radiofonico = [['A','Alfa'],   ['B','Bravo'], ['C','Charlie'],
               ['D','Delta'],  ['E','Echo'],  ['F','Foxtrot'],
               ['G','Golf'],   ['H','Hotel'], ['I','India'],
               ['J','Juliet'], ['K','Kilo'],  ['L','Lima'],
               ['M','Mike'],   ['N','November'],['O','Oscar'],
               ['P','Papa'],   ['Q','Quebec'],['R','Romeo'],
               ['S','Sierra'], ['T','Tango'], ['U','Uniform'],
               ['V','Victor'], ['W','Whiskey'],['X','X-ray'],
               ['Y','Yankee'], ['Z','Zulu']]
#HOLA MUNDO---> Hotel Oscar Lima Alfa*Mike Uniform Novembre Oscar
#hotel oscar lima alfa

radiofonico=dict(radiofonico)
# print(radiofonico)
#Implemente lo siguiente:

##########################################################################################################################################################################################################
#Una funcion llamada coderadio(secuencia, alfabeto) que recibe la secuencia de caracteres a codificar y el diccionario con el alfabeto radiofonico. La funcion debe entregar el
#mensaje codificado    
def coderadio(secuencia:str,alfabeto:dict):
  secuencia=secuencia.upper().replace(" ","")
  codificacion=""
  for letra in secuencia:
    x=alfabeto[letra]
    codificacion+=x+" "

  return codificacion.strip(" ")
##########################################################################################################################################################################################################
#Una funcionn llamada decoderadio(cadena,alfabeto) que recibe una cadena de texto codificada y el diccionario con el alfabeto radiofonico. 
#La funcion retornara la cadena decodificada.  

#HOLA MUNDO---> Hotel Oscar Lima Alfa * Mike Uniform Novembre Oscar
def decoderadio(cadena:str,alfabeto:dict):
  l_cadena=cadena.title().split(" ")
  values_codes=list(alfabeto.values())
  keys_codes=list(alfabeto.keys())
  decode=""
  for code in l_cadena:
    if code!="*":
      i=values_codes.index(code)
      decode+=keys_codes[i]
    else:
      decode+=" "

  return decode.title()


##########################################################################################################################################################################################################
#main

# mensaje=input("Ingrese un mensaje para codificar: ")
# codificado=coderadio(mensaje,radiofonico)
# print("El mensaje codificado es",codificado)
decodificacion=decoderadio("Hotel Oscar Lima Alfa * Mike Uniform November Delta Oscar",radiofonico)
print("El mensaje decodificado es",decodificacion)