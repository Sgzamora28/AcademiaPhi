def menu():
 print("1. ver listado ")
 print("2. Calcular factura ")
 print("3. Buscar cliente ")
 print("4. Salir")
 print("Ingresa una opción de 1-4: ")
 opcion = int(input())
 return opcion

def ver_listado(clientes,consumo): 
  listconsum=[]
  listcli=[]
  for x in range(len(clientes)):
    consumo2 = consumo[x]
    cliente = clientes[x]
    listconsum.append(consumo2)
    listcli.append(cliente)
    print(cliente,consumo2)
  return listcli,listconsum
  
def calculos(listcli,listconsum):
  listtot=[]
  for i in range(len(listconsum)):
    listc=listcli[i]
    listcon=listconsum[i]
    valor=float(input("ingrese el valor del litro:"))
    if listcon<140:
      total=listcon*0.90*valor      
    elif listcon>300:
      total=listcon*1.10*valor      
    else:
      total=listcon*valor
      
    totall=total*1.13
    listtot.append(totall)
    print("Se hicieron los cálculos......")
    return listc,listtot

def salir():
  print("Eso es todo amigos....")
  exit(0)