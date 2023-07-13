# En un restaurante, el sistema informático que lleva las cuentas almacena los pedidos de los clientes en una lista “ordenes” y 
# tiene también una lista “productos” de los productos que ofrece. Ambas listas mantienen un formato de valores separados por / y se describen a continuación:

# Número de Mesa/Código del Producto/Unidades Consumidas
l_ordenes=["8/832/3", "8/910/3", "1/910/2"]

# Código del Producto/Nombre del Producto/Precio Unitario
l_productos=["832/Arroz con Menestra y Carne/5.50", "910/Gaseosa Mediana/1.00", "211/Seco de Pollo/6.00"]

# Usted Usted debe implementar:
# 1. La función facturar(mesa, ordenes, productos)
# La función recibe: El número de mesa del cliente que desea pagar su orden y las listas “ordenes” y “productos”.
# Dentro de la función se debe mostrar por pantalla todos los productos consumidos por dicha mesa, indicando: cantidad, nombre del producto y el costo total por ese producto.
# Al finalizar se debe retornar el total consumido (que es el subtotal de la factura).

# 2. Un programa principal que:
# Solicite los datos del cliente (nombre, cédula, dirección y teléfono) para imprimir la cabecera de la factura. Verifique la cedula y telefono
# Pregunte al usuario la mesa correspondiente.
# Llame a la función facturar 
# Calcule los valores que debe añadir por servicio (10%) y por IVA (12% del subtotal de la orden incluido servicio).
# Muestre la factura por pantalla.



def facturar(mesa: int, ordenes: list, productos: list):
  subtotal=0
  for orden in ordenes:
    num_mesa,prod,unidades=orden.split('/')
    if int(num_mesa)==mesa:
      for producto in productos:
        cod,nombre,costo=producto.split('/')
        if cod==prod:
          pago=int(unidades)*float(costo)
          subtotal+=pago
          print('{} {} {}'.format(unidades,nombre,pago))


  return subtotal



# x=facturar(8,l_ordenes,l_productos)
# print(x)

#main

#solicitud de datos
nombre=input('Ingrese su nombre: ')
cedula=input('Ingrese su cedula: ')
#condiciones correctas: cedula.isdigit() and len(cedula)==10
while not(cedula.isdigit and len(cedula)==10):
  cedula=input('Ingresa bien tu cedula: ')

telefono=input('Ingrese su numero de telefono: ')
#condiciones telefono.isdigit() and len(telefono)==10 and telefono[:2]=='09'
while not(telefono.isdigit() and len(telefono)==10 and telefono[:2]=='09'):
  telefono=input('Ingrese un numero de telefono valido: ')
direccion=input('Ingrese su direccion de domicilio: ')
mesa=input('Ingrese su numero de mesa: ')
mesa=int(mesa)


print('Cliente {}\nCedula: {}\nTelefono: {}\nDireccion: {}'.format(nombre,cedula,telefono,direccion))
subtotal=round(facturar(mesa,l_ordenes,l_productos),2)
valorXservicio=round(subtotal*1.1,2) #subtototal+subtotal*0.1
total=valorXservicio*1.12
print('Subtotal mas servicios (%10):',valorXservicio)
print('Total mas IVA(12%): {:.2f}'.format(total))