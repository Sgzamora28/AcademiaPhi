# Dado el siguiente programa parcial:

# funciones
def obtener_tarifas(informacion_tarifas:list[str]):
  Paises_destino = []
  Tarifas_envio_xkg = []

  for info in informacion_tarifas:
    pais,tarifa=info.split("-")
    tarifa = int(tarifa)
    Paises_destino.append(pais)
    Tarifas_envio_xkg.append(tarifa)

  return Paises_destino, Tarifas_envio_xkg

# programa principal

catalogo = ["Colombia-5","USA-10","Peru-7","Brasil-12"]
# Complete el programa principal donde utilice (llame a) la función obtener_tarifas para crear 
# listas paralelas con los nombres de los países y su correspondiente tarifa de envío por kilogramo.
paises,tarifas=obtener_tarifas(catalogo)

#["Colombia","USA","Peru","Brasil"]
#[5,10,7,12]

# Luego, pida al usuario que ingrese un destino por teclado. Usando otro input, pida al usuario 
# que ingrese un peso en kilogramos. Muestre por pantalla el valor a pagar por enviar el paquete con la 
# información ingresada. El usuario podrá seguir ingresando datos de paquetes hasta que escriba FINALIZADO como destino. 
# Asegúrese que su programa no se caiga (genere un error o una excepción) si el usuario ingresa un país que no 
# existe en el catálogo.

pais=""
total=0
while pais!="FINALIZADO":
  pais=input("Ingrese un pais: ")
  if pais in paises:
    peso=float(input("Ingrese el peso en kg del paquete que desea enviar: "))
    i=paises.index(pais)
    costo=tarifas[i]*peso
    total+=costo
  
  elif pais=="FINALIZADO":
    print("Vamos a calcular el total de su envio")

  else:
    print("El pais no se encuentra en la lista")


print("El total de su envio es",total)
# Finalmente, muestre el total a pagar.