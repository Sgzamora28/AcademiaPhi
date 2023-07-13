#############################################################################
#Ejercicio 1
#############################################################################
import datetime

def calcularFecha(fecha, n):
    f = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
    resta = f - datetime.timedelta(days=n)
    return resta.strftime('%d-%m-%Y')



# TEMA 1 (40 PUNTOS)
# Dado el archivo rutasManejadas2018.txt con información como la que sigue:

# id_ruta, id_chofer, fecha
# Guayaquil-Cuenca,SMSNADOPN,17-05-2018
# Guayaquil-Cuenca,AGBCCAPMP,18-05-2018
# Guayaquil-Daule,EVNTAASFL,17-05-2018
# Guayaquil-Daule,AAQSPTTGL,18-05-2018
# Suponga que dispone de una función calcularFecha(fecha, n) que recibe una fecha y un entero. 
# La función retorna la fecha correspondiente a los n días anteriores a la fecha del parámetro (sin incluirla).
# Implemente lo siguiente:


# 1. (12 puntos) La función cargarDatos(nomA) que recibe el nombre del archivo con los datos anteriores. 
# Esta función retorna una tupla de dos elementos. El primer elemento es un conjunto con los ids de TODOS los choferes mencionados en el archivo. 
# El segundo elemento es un diccionario con la siguiente estructura:
# {id_ruta: {fecha:{ch1,ch2,..., chk}}}. Ejemplo del diccionario:
# {"Guayaquil-Cuenca":{"17-05-2018":{"SMSNADOPN","AGBCCAPMP",...}, "18-05-2018":{"...","...",...},
# ...},
# "Guayaquil-Daule": {"17-05-2018":{"EVNTAASFL","AAQSPTTGL",...}, "18-05-2018":{"...","...",...},
# ...},

# def cargar(nombre):
#   conjunto=set() #---> {}
#   diccionario={}

#   archivo=open(nombre)
#   archivo.readline()

#   for linea in archivo:#id_ruta, id_chofer, fecha
#     # print(linea.strip())
#     ruta,chofer,fecha=linea.strip().split(",")#["id_ruta","id_chofer","fecha"]
#     conjunto.add(chofer)#datos[1]

#     if ruta not in diccionario:
#       diccionario[ruta]={}

#     if fecha not in diccionario[ruta]:
#       diccionario[ruta][fecha]=set()

#     diccionario[ruta][fecha].add(chofer)


#   # print(diccionario)
#   archivo.close()
#   return conjunto,diccionario


def cargar(nombre):
  conjunto=set()
  diccionario={}

  with open(nombre) as archivo:
    archivo.readline()
    for linea in archivo:
      ruta,chofer,fecha=linea.strip().split(",")
      conjunto.add(chofer)

      diccionario[ruta]=diccionario.get(ruta,{})
      diccionario[ruta][fecha]=diccionario[ruta].get(fecha,set())
      diccionario[ruta][fecha].add(chofer)


  return conjunto,diccionario


# ids,viajes=cargar("rutasManejadas2018.txt")


# (16 puntos) La función encontrarChoferes(dicc, fecha, losChoferes, id_ruta, n) que recibe el diccionario del numeral anterior, 
# una fecha (con formato dd-mm-yyyy), el conjunto con los ids de TODOS los choferes, el nombre de una ruta y un entero n. 
# Esta función retorna un conjunto con los ids de todos los choferes que NO hayan manejado la ruta id_ruta en los n días anteriores a
#  fecha (sin incluir fecha). Por ejemplo, si n es 3 y la fecha es "02-05-2018", 
# la función devuelve un conjunto con los ids de choferes que NO hayan manejado id_ruta el 29, 30 de abril y el 1 de mayo de 2018.


def buscar(diccionario:dict,fecha:str,choferes:set,ruta:str,n:int): #3
  conducido=set() #Todos los choferes que si han conducido en esas fechas
  recorrido=diccionario[ruta]
  # print(recorrido)
  for i in range(1,n+1): #1,2,3 ------range(n) [0,1,2]
    f_anterior=calcularFecha(fecha,i)
    # print(f_anterior)
    x=recorrido.get(f_anterior,set())
    conducido.update(x)
    


  sinConducir=choferes-conducido

  return sinConducir


# x=buscar(viajes,"22-05-2018",ids,"Guayaquil-Cuenca",4)
# print(x)



# (12 puntos) La función grabarArchivo(fecha, diccionario, losChoferes, n) que recibe una fecha, el diccionario del numeral 1, 
# un conjunto con los IDs de todos los choferes y un número entero n. Esta función crea un archivo, cuyo nombre tiene el formato idRuta_fecha.txt, 
# para cada ruta con los choferes que NO han manejado la ruta id_ruta en los n días anteriores a la fecha (sin incluir fecha). 
# El formato para este archivo es el siguiente:
# Para la ruta Guayaquil-Cuenca, los choferes disponibles para la fecha 19-05-2018 que no hayan manejado 2 dias anteriores son:
# VSSUIMCMS SJMPYSANL
# ...


def grabar(fecha,diccionario,choferes,n):
  for recorrido,datos in diccionario.items():
    nombre=f"{recorrido}_{fecha}.txt"
    with open(nombre,"w") as arch:
      arch.write(f"Para la ruta {recorrido}, los choferes disponibles para la fecha {fecha} que no hayan manejado los {n} dias anteriores son:\n")
      no_manejado=buscar(diccionario,fecha,choferes,recorrido,n)
      for chofer in no_manejado:
        arch.write(f"{chofer}\n")




# grabar("22-05-2018",viajes,ids,4)



#############################################################################
#Ejercicio 2
#############################################################################
# TEMA 2 (30 PUNTOS)
# Como asistente de médico, usted tiene la tarea de generar un informe de indicadores a partir de un examen
# de sangre. El resultado se lo entregan como una cadena de texto. Los indicadores los puede identificar
# porque estos siempre estarán en mayúsculas , por ejemplo INR, WBC, RBC, TA, etc. Todo indicador va
# seguido de un espacio, luego un número con decimales, seguido de otro espacio en blanco y finalmente las
# unidades. Al final del reporte se encuentra el nombre del médico. Ejemplos de resultados:
resultado = "Resultado de Laboratorio 'Su Salud' Nombre del paciente: José Aimas E-mail \
del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT \
180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC \
123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firma \
médico responsable Dr. Juan Pozo"

# INFORME DE LABORATORIO
# **********************
# INR 1.25 segundos
# BGT 180.12 mmol/dL
# HGB 13 g/dL **
# ESR 3.2 mm/hora
# RBC 4000024.2 cel/uL
# TA 1.5 ng/dL
# WBC 123233.23 cel/uL
# Médico: Juan Pozo
# **Su nivel de hemoglobina es bajo, se recomienda ir al hematólogo.
# No es

# resultado = "Resultado de Laboratorio 'Sana' Nombre del paciente: Ginger Irene Cruz\
# Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL\
# Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth\
# Plaza"

# La cantidad de indicadores puede variar. Los puntos no solo aparecen en los decimales, sino
# también para separar párrafos o en otras ocasiones como las direcciones de e-mail.
# Escriba un programa que nos muestre la información desglosada, el nombre del médico y una
# recomendación de si el paciente debe ir al Hematólogo. Un paciente debe ir al Hematólogo si su nivel de
# hemoglobina (HGB), está por debajo de los 14 g/dL. En caso de dar la recomendación, mostrar doble
# asterisco en el indicador HGB y la recomendación al final.

resultado=resultado.split(" ")
# print(resultado)
with open("Acompañamiento 2P\\resultados.txt","w") as arch:
  arch.write("INFORME DE LABORATORIO \n**********************\n")
  recomendacion=""
  for i in range(len(resultado)):
    if resultado[i].isupper():
      indicador=resultado[i]
      valor=resultado[i+1]
      unidades=resultado[i+2]
      if indicador=="HGB" and float(valor)<14:
        arch.write("{} {} {} **\n".format(indicador,valor,unidades))
        recomendacion="**Su nivel de hemoglobina es bajo, se recomienda ir al hematologo."

      else:
        arch.write("{} {} {}\n".format(indicador,valor,unidades))

    if resultado[i]=="Dr." or resultado[i]=="Dra.":
      medico=" ".join(resultado[i+1:])#["Dra.", 'Karina', 'Elizabeth', "Plaza"]

  arch.write("\nMedico: {}\n".format(medico))
  if len(recomendacion)!=0:
    arch.write("Recomendacion: {}".format(recomendacion))

      