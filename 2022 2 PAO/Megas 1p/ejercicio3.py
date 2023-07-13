# Para el siguiente ejercicio:
# Implemente la función extraer_datos(listatweets, ciudad) que recibe una lista de
# cadenas, el formato de cada cadena se describe abajo, y el nombre de una ciudad. La función
# retorna tres listas de cadenas paralelas. La primera con las fechas, la segunda con las
# temperaturas mínimas y la tercera con las temperaturas máximas para la ciudad especificada.
# Ejemplo: (Recuerde que los datos del ejemplo son solo demostrativos y pueden cambiar
# para las pruebas finales cuando revisemos su solución).
# Si tenemos la siguiente lista de cadenas llamada tweets:
# tweets = ['El DIA 2021-05-17 en la CIUDAD Guayaquil se registró una TEMP_MIN
# 18.3 grados centígrados y una TEMP_MAX 27.7 grados centígrados.', ..., 'El DIA
# 2018-01-11 en la CIUDAD Guayaquil se registró una TEMP_MIN 21.2 grados
# centígrados y una TEMP_MAX 32.3 grados centígrados.', ..., 'El DIA 2018-01-11
# en la CIUDAD Salinas se registró una TEMP_MIN 20.3 grados centígrados y una
# TEMP_MAX 26.5 grados centígrados.', ..., 'El DIA 2020-04-09 en la CIUDAD
# Guayaquil se registró una TEMP_MIN 17.5 grados centígrados y una TEMP_MAX 24.2
# grados centígrados.', ...]

def extraer(tweets,ciudad):
  fechas=[]
  mininmas=[]
  maximas=[]

  for tweet in tweets: #'El DIA 2021-05-17 en la CIUDAD Latacunga se registró una TEMP_MIN 18.3 grados centígrados y una TEMP_MAX 27.7 grados centígrados.'
    c2=""
    tweet=tweet.split(" ")

    for i in range(len(tweet)):
      if tweet[i]=="DIA":
        fecha=tweet[i+1]

      if tweet[i]=="CIUDAD":
        c2=tweet[i+1]

      if c2==ciudad:
        if tweet[i]=="TEMP_MIN":
          temMin=float(tweet[i+1])
          mininmas.append(temMin)

        if tweet[i]=="TEMP_MAX":
          temMax=float(tweet[i+1])
          maximas.append(temMax)

        if fecha not in fechas:
          fechas.append(fecha)
        

  return fechas,mininmas,maximas


#main
# Llame a la función extraer_datos para generar las tres listas paralelas con la información para la ciudad de Latacunga. 
# (Para el resto de este tema trabaje solo con estas temperaturas y fechas que acaba de extraer).
# • Genere una cuarta lista paralela con la temperatura promedio para cada fecha, utilizando la siguiente formula:
# promedio=(temp_min+temp_max)/2
# • Pide al usuario que ingrese un numero de mes. Validar que sea un número de mes correcto, caso contrario, continue pidiendo al usuario que lo ingrese. 
# Luego considere las temperaturas promedio (calculadas en el punto anterior) solo para fechas que correspondan a ese mes (sin importar el día o el año) y
#  muestre por pantalla la menor temperatura promedio.


tweets = ['El DIA 2021-05-17 en la CIUDAD Latacunga se registró una TEMP_MIN 18.3 grados centígrados y una TEMP_MAX 27.7 grados centígrados.',
          'El DIA 2018-01-11 en la CIUDAD Latacunga se registró una TEMP_MIN 21.2 grados centígrados y una TEMP_MAX 32.3 grados centígrados.',
          'El DIA 2018-01-11 en la CIUDAD Salinas se registró una TEMP_MIN 20.3 grados centígrados y una TEMP_MAX 26.5 grados centígrados.',
          'El DIA 2020-05-09 en la CIUDAD Latacunga se registró una TEMP_MIN 17.5 grados centígrados y una TEMP_MAX 24.2 grados centígrados.']




fechas,minimas,maximas=extraer(tweets,"Latacunga")


promedios=[]
for i in range(len(fechas)):
  promedio=(minimas[i]+maximas[i])/2
  promedios.append(promedio)

mes=input("Ingrese un mes: ")#str
#reconocer las condiciones correctas del dato---> mes.isdigit() and 1<=int(mes)<=12

while not(mes.isdigit() and 1<=int(mes)<=12):
  mes=input("Ingrese un mes: ")#str

mes=int(mes)

promedio_menor=10000000

for i in range(len(fechas)):#"2021-05-17" ---> ["2021","05","17"]
  anio,mes2,dia=fechas[i].split("-")
  if mes==int(mes2):
    if promedios[i]<promedio_menor:
      promedio_menor=promedios[i]


print(fechas)
print(promedios)
print(f"La menor temperatura promedio para el mes {mes} es igual a {promedio_menor}")