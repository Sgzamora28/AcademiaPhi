# En un restaurante, el sistema informático que lleva las cuentas almacena los pedidos de los clientes en una lista “ordenes” y 
# tiene también una lista “productos” de los productos que ofrece. Ambas listas mantienen un formato de valores separados por / y se describen a continuación:

# Número de Mesa/Código del Producto/Unidades Consumidas
ordenes=["8/832/3", "8/910/3", "1/910/2"]

# Código del Producto/Nombre del Producto/Precio Unitario
productos=["832/Arroz con Menestra y Carne/5.50", "910/Gaseosa Mediana/1.00", "211/Seco de Pollo/6.00"]

# Usted Usted debe implementar:

# 1. La función facturar(mesa, ordenes, productos)

# La función recibe: El número de mesa del cliente que desea pagar su orden y las listas “ordenes” y “productos”.
# Dentro de la función se debe mostrar por pantalla todos los productos consumidos por dicha mesa, indicando: cantidad, nombre del producto y el subtotal.
# Al finalizar se debe retornar el total consumido (que es el subtotal de la factura).
# 2. Un programa principal que:

# Solicite los datos del cliente (nombre, cédula, dirección y teléfono) para imprimir la cabecera de la factura.
# Pregunte al usuario la mesa correspondiente.
# Llame a la función facturar 
# Calcule los valores que debe añadir por servicio (10%) y por IVA (12% del subtotal de la orden incluido servicio).
# Muestre la factura por pantalla.


def factura(mesa,ordenes,productos):
    subtotal=0
    nom_productos=[]
    for orden in ordenes:
        n_mesa,cod,unidades=orden.split('/')
        if int(n_mesa)==mesa:
            for producto in productos:
                codigo,nombre,precio=producto.split('/')
                if codigo==cod:
                    pago=float(precio)*int(unidades)
                    subtotal+=pago
                    print('Producto: {}. Cantidad: {}'.format(nombre,unidades))
    print(subtotal)
    return subtotal

#MAIN
nombre=input('Ingrese su nombre: ').title()
cedula=input('Ingrese su cedula: ')
direccion=input('Ingrese su direccion: ')
telefono=input('Ingrese su numero de telefono: ')
mesa=int(input('Ingrese su numero de mesa: '))
subtotal=factura(mesa,ordenes,productos)
total_pagar=(subtotal*1.1)*1.12
print('Nombre del cliente: {}\nCedula: {}\nDireccion: {}\nTelefono: {}'.format(nombre,cedula,direccion,telefono))
print('Subtotal: {:.2f}\nTotal a pagar: {:.2f}'.format(subtotal,total_pagar))
#pago por servicio---> subtotal+subtoral*0.1