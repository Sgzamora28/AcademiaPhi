# def imprimir(tab):
#   print(tab[0],"|",tab[1],"|",tab[2])
#   print(tab[3],"|",tab[4],"|",tab[5])
#   print(tab[6],"|",tab[7],"|",tab[8])

# def victoria(casillas):
#   #[0,7,8]
#   win=False
#   for casilla in casillas:
#     # 0 | 1 | 2
#     # 3 | 4 | 5
#     # 6 | 7 | 8
#     h1=0
#     h2=0
#     h3=0
#     v1=0
#     v2=0
#     v3=0
#     d1=0
#     d2=0
#     if casilla in [0,1,2]:
#       h1+=1
#     if casilla in [3,4,5]:
#       h2+=1
#     if casilla in [6,7,8]:
#       h3+=1
#     if casilla in [0,3,6]:
#       v1+=1
#     if casilla in [1,4,7]:
#       v2+=1
#     if casilla in [2,5,8]:
#       v3+=1
#     if casilla in [0,4,8]:
#       d1+=1
#     if casilla in [2,4,6]:
#       d2+=1

#     if h1==3 or h2==3 or h3==3 or v1==3 or v2==3 or v3==3 or d1==3 or d2==3:
#       win=True
    
#     return win
    
    

# import random as rd
# tablero=["_"]*9
# jugadas_m=[]
# jugadas_u=[]
# victoria_m=victoria(jugadas_m)
# victoria_j=victoria(jugadas_u)
# while not(victoria_m or victoria_j or "_" not in tablero):
#   victoria_m=victoria(jugadas_m)
#   victoria_j=victoria(jugadas_u)
#   if not(victoria_j or victoria_m or "_" not in tablero):
#     maquina=rd.randrange(9)
#     while not(tablero[maquina]=="_"):
#       maquina=rd.randrange(9) 
#     jugadas_m.append(maquina)
#     simbolo="X"
#     tablero[maquina]=simbolo
#     imprimir(tablero)
#     print()
#     victoria_m=victoria(jugadas_m)    
#     if not(victoria_m or "_" not in tablero):
#       usuario=input("Ingrese un numero del tablero para jugar: ")
#       while not(usuario.isdigit() and int(usuario)-1 in range(9) and tablero[int(usuario)-1]=="_"):
#         usuario=input("Casilla no valida o ya jugada. Intente nuevamente: ")
#       usuario=int(usuario)-1
#       jugadas_u.append(usuario)
#       simbolo="O"
#       tablero[usuario]=simbolo
#       imprimir(tablero)
#       print()

# if victoria_j:
#   print("Usted gano la partida")
# elif victoria_m:
#   print("La maquina gano la partida")
# elif "_" not in tablero:
#   print("Ya no quedan mas movimientos")


for i in range(1,10,2):
  print(i)