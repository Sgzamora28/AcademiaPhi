# import random as rd
# #Ejercicio 1
# lst_valores=[0,0,0,0,0,0,0,0]
# n=rd.randint(1,10) #---> valor fijo
# print(n)
# print()



# x=[]
# for i in range(n):
#   numero=input("Ingrese un numero entre 10 y 100 (sin incluir extremos): ") #nota ---> todo lo que ingresa es str '100' '10'
#   #dato ----> numero entre 10 y 100 
#   # condicion de correcta del dato: int(numero) in range(11,100)  
#   while not(int(numero) in range(11,100)):
#     numero=input("El numero debe estar entre 10 y 100: ")

#   x.append(int(numero))


# datos=x+lst_valores
# print(datos)

# #El valor mas grande de la lista---> max(datos)--> valor mayor

# #Ordenando la lista
# datos.sort(reverse=True)
# print(datos[1])

#Ejercicio 2

vocales=['a','e','i','o','u']
consonantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#mi.familia.es.numerosa --replace--> mi familia es numerosa
texto=input("Ingrese una oracion separada por puntos o por espacios: ").lower().replace("."," ").split(" ") #mi|familia|es|numerosa ---> ['mi','familia','es','numerosa']
# print(texto)
resultado=[]
for palabra in texto:
  if palabra.isalpha():
    # print(palabra)
    c_vocales=0
    c_consonantes=0
    for letra in palabra:
      if letra in vocales:
        #letra es una vocal
        c_vocales+=1

      else:
        c_consonantes+=1

    if c_vocales==c_consonantes:
      resultado.append(palabra)

print(len(resultado))


#Ejercicio 3
#num_mesa/codigo/unidades
ordenes=["8/832/3","8/910/3","1/910/2","8/211/1"]

#codigo/nombre/PVU
productos=["832/Arroz con Menestra y Carne/5.50","910/Gaseosa Mediana/1.00","211/Seco de Pollo/6.00"]



x=["Steven","Mecatronica","202101713"]

nombre,carrera,matricula=x

def facturar(mesa:int,ordenes:list[str],productos:list[str]):
  total=0
  for orden in ordenes:
    num_mesa,codigo1,unidades=orden.split("/") #['num_mesa','codigo','unidades']
    if int(num_mesa)==mesa:
      #codigo1--> 832
      for producto in productos: #codigo/nombre/pvu
        codigo2,nombre,pvu=producto.split("/")
        if codigo1==codigo2:
          subtotal=float(pvu)*int(unidades)
          print(nombre,unidades,subtotal)
          total+=subtotal


  return total


#main
nombre=input("Ingrese su nombre: ")
cedula=input("Ingrese su cedula: ")
direccion=input("Ingrese su direccion: ")
telefono=input("Ingrese su telefono: ")
num_mesa=int(input("Ingrese su numero de mesa: "))
subtotal=facturar(num_mesa,ordenes,productos)
servicio=subtotal*0.1
total=(subtotal+servicio)*1.12

print(f"Nombre: {nombre}\nCedula: {cedula}\nDireccion: {direccion}\nTelefono: {telefono}\nNumero de Mesa: {num_mesa}")
print("Subtotal: {}\nValor por Servicio: {:.2f}\nTotal+Iva: {:.2f}".format(subtotal,servicio,total))


#Ejercicio 4
ganador=74852


# A  z  u  c  e  n  a
# 0  1  2  3  4  5  6
#-7 -6 -5 -4 -3 -2 -1

for i in range(4):
  boleto=input("Ingrese los 5 digitos de su boleto: ")
  #condiciones correctas: boleto sea un numero y numero del boleto debe tener 5 digitos
  #condiciones correctas: boleto.isdigit() and len(boleto)==5
  while not(boleto.isdigit() and len(boleto)==5):
    boleto=input("Su valor debe ser un numero y debe contener 5 digitos.\nPor favor, intente nuevamente: ")

  if int(boleto)==ganador:
    print("Mi loco, te has llevado 5000 lucas")

  elif boleto[-2:]==str(ganador)[-2:]:
    print("Has ganado 100 dolares por tu boleto")
  
  elif boleto[-1]==str(ganador)[-1]:
    print("Has ganado solamente 10 dolares")

  else:
    print("No has ganado ningun premio para este boleto")