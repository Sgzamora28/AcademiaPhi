# Asuma que se tiene un archivo por cada partido jugado en el Sudamericano Sub-20. Cada archivo tiene información
# con datos de los jugadores que participaron en el partido con el siguiente formato:
# Pais,Jugador,Tarjetas_Amarillas,Tarjetas_Rojas,Goles,Minutos,KM_recorridos
# Ejemplo:


# Pais,Jugador,Tarjetas_Amarillas,Tarjetas_Rojas,Goles,Minutos,KM_recorridos
# ...
# Ecuador,José Cifuentes,1,0,0,75,6.3
# Uruguay,Sebastián Cáceres,2,1,0,90,7
# Ecuador,Leonardo Campana,0,0,1,87,10
# ...
# Implemente las siguientes funciones:

dic={}

# 1. [15 puntos] actualizaDiccionario(nomArchivo, dic) que recibe el nombre de un archivo con datos del partido y
# actualiza el diccionario de totales por jugador que tiene el siguiente formato:
# dic = {'Ecuador':{'Leonardo Campana':{'TA':3,'TR':0,'Goles':6,'Minutos':800,'KM':75},
#  ...
#  },
#  'Argentina':{...},
#  ...
#  }


def actualizar(archivo,diccionario):
  with open(archivo) as arch:
    arch.readline()
    for line in arch:
      datos=line.strip().split(",")#[Pais,Jugador,Tarjetas_Amarillas,Tarjetas_Rojas,Goles,Minutos,KM_recorridos]
      diccionario[datos[0]][datos[1]]["TA"]+=int(datos[2])
      diccionario[datos[0]][datos[1]]["TR"]+=int(datos[3])
      diccionario[datos[0]][datos[1]]["Goles"]+=int(datos[4])
      diccionario[datos[0]][datos[1]]["Minutos"]+=int(datos[5])
      diccionario[datos[0]][datos[1]]["KM"]+=int(datos[6])




# [9 puntos] buenDeportista(jugador, dic) que recibe el nombre de un jugador y el diccionario de totales. La
# función retorna True o False dependiendo si ese jugador puede ser catalogado como un "buen deportista". Un
# jugador se considera un "buen deportista" si ha recibido menos de 2 tarjetas por cada 270 minutos de juego.

def buenDeportista(jugador,diccionario):
  tarjetas=0
  minutos_jugados=0

  for nomina in diccionario.values():
    if jugador in nomina:
      tarjetas=nomina[jugador]["TA"]+nomina[jugador]["TR"]
      minutos_jugados=nomina[jugador]["Minutos"]

  x=minutos_jugados/270
  tarjetasXpartido=x//tarjetas

  if tarjetasXpartido<2:
    return True

  else:
    return False



# [9 puntos] jugadorAtleta(jugador, dic) que recibe el nombre de un jugador y el diccionario de totales. Si el
# jugador ha corrido como mínimo el promedio de lo que han corrido los jugadores de su país y ha anotado al
# menos un gol, retorna True. En caso contrario, retorna False



# dic = {'Ecuador':{'Leonardo Campana':{'TA':3,'TR':0,'Goles':6,'Minutos':800,'KM':75},
#  ...
#  },
#  'Argentina':{...},
#  ...
#  }
def atleta(jugador,diccionario):
  sumatoria=0
  for nomina in diccionario.values():
    if jugador is nomina:
      for player in nomina:
        sumatoria+=player['KM']
      promedio=sumatoria/len(nomina)
      if nomina[jugador]["KM"]>=promedio and nomina[jugador]["Goles"]>=1:
        return True

      else:
        return False

  

# dic = {'Ecuador':{'Leonardo Campana':{'TA':3,'TR':0,'Goles':6,'Minutos':800,'KM':75},
#  ...
#  },
#  'Argentina':{...},
#  ...
#  }

# [9 puntos] paisBuenasPracticas(pais, dic) que recibe el nombre de un país y el diccionario de totales. La función
# retorna True o False dependiendo si ese país puede ser nominado para el "Best Practices award". Un país
# puede ser nominado a este premio si TODOS los jugadores del país pueden ser catalogados como "buen
# deportista".


def buenasPracticas(pais,diccionario):
  final=True
  for jugador in diccionario[pais]:
    x=buenDeportista(jugador,diccionario)
    final=final and x


  return final

