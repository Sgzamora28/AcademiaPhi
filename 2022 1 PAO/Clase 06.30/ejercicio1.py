# Dado el siguiente programa parcial:

# funciones
catalogo = ["Colombia-5","USA-10","Peru-7","Brasil-12"]
def obtener_tarifas(informacion_tarifas):
  Paises_destino = []
  Tarifas_envio_xkg = []

  for info in informacion_tarifas:
    pais,tarifa=info.split("-")#['Colombia','5']
    tarifa = int(tarifa)
    Paises_destino.append(pais)
    Tarifas_envio_xkg.append(tarifa)

  return Paises_destino, Tarifas_envio_xkg

# programa principal


# Complete el programa principal donde utilice (llame a) la función obtener_tarifas para crear listas paralelas con los nombres de los países y su correspondiente tarifa de envío 
# por kilogramo.
# Luego, pida al usuario que ingrese un destino por teclado. Usando otro input, pida al usuario que ingrese un peso en kilogramos. 
# Muestre por pantalla el valor a pagar por enviar el paquete con la información ingresada. 
# El usuario podrá seguir ingresando datos de paquetes hasta que escriba FINALIZADO como destino. ---->while
# Asegúrese que su programa no se caiga (genere un error o una excepción) si el usuario ingresa un país que no existe en el catálogo.---->verificaciones
# Finalmente, muestre el total a pagar.

#['Colombia','USA','Peru','Brasil']
#[5,10,7,12]
paises,tarifas=obtener_tarifas(catalogo)
pais=''
total_envios=0
while pais!='FINALIZADO':
  pais=input('Ingrese el pais: ').title()#Usa
  if pais.upper()!='FINALIZADO':
    #condiciones correctas---> pais.title() in paises or pais.upper() in paises
    while not(pais.title() in paises or pais.upper() in paises):
      pais=input('Ingrese un pais que se encuentre en la lista: ')
    if pais=='Usa':
      pais=pais.upper()
    kg=input('Ingrese el peso de su producto: ')
    i=paises.index(pais)
    tarifa=tarifas[i]
    total=tarifa*float(kg)
    print('El total a pagar por el peso de su paquete es',total)
    total_envios+=total
    

  else:
    pais=pais.upper()

print('Total:',total_envios)