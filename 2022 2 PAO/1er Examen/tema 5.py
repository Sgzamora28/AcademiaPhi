# TEMA 5
# Implemente la función calcular_puntajes(l_partidos,l_goles) que recibe dos listas paralelas. 
# La lista l_partidos es una lista de strings con los nombres de los equipos que se enfrentan en 
# cada partido de la primera etapa del mundial de Catar. La lista l_goles es también una lista de strings con 
# los goles marcados por cada uno de los equipos en los partidos representados en la lista l_partidos. Ejemplo:
# ['CAT-ECU', ..., 'ARG-MEX', ..., 'BRA-SUI', ..., 'ECU-SEN', ...] # Ejemplo de l_partidos 
# ['0-2', ..., '1-1', ..., '4-1', ..., '1-2', ...] # Ejemplo de l_goles
# La función debe retornar una nueva lista de tuplas con los puntos obtenidos 
# por cada selección en esta fase del mundial. Recuerde que una victoria otorga 3 puntos al equipo ganador. 
# Un empate otorga 1 punto a ambos equipos y, la derrota 0 puntos al equipo perdedor. Ejemplo del retorno:
# [('ECU', 7), ..., ('BRA', 9), ..., ('ARG', 5), ...]


l_partidos = ['CAT-ECU','CAT-SEN','ARG-MEX','CAT-HOL','BRA-SUI','ECU-SEN','ECU-HOL','HOL-SEN'] # Ejemplo de l_partidos
l_goles = ['0-2','1-3','1-1','0-2','4-1','1-2','1-1','2-0'] # Ejemplo de l_goles

def puntajes(partidos:list[str],goles:list[str]):
  paises=[] #[ECU,CAT,HOL]
  puntajes=[] #[4,0,7]
  

  for i in range(len(partidos)):#'CAT-ECU'
    e1,e2=partidos[i].split("-") #["CAT","ECU"]
    g1,g2=goles[i].split("-")

    if e1 not in paises:#si el equipo no esta en la lista
      paises.append(e1)#lo agrego en la lista de paises
      puntajes.append(0)#y le pongo sus puntos iniciales en la lista de puntajes

    if e2 not in paises:
      paises.append(e2)
      puntajes.append(0)

    i_e1=paises.index(e1)
    i_e2=paises.index(e2)

    if g1>g2:
      puntajes[i_e1]+=3

    elif g2>g1:
      puntajes[i_e2]+=3

    else:
      puntajes[i_e1]+=1
      puntajes[i_e2]+=1

  # resultados=[]
  # for i in range(len(paises)):
  #   resultado=(paises[i],puntajes[i])
  #   resultados.append(resultados)


  resultados=list(zip(paises,puntajes))#[(ECU,4),(CAT,0),(HOL,7)]
  return resultados



x=puntajes(l_partidos,l_goles)
print(x)

  
  


