import numpy as np

# Tema 3. (50 puntos) El Black Friday inaugura la temporada de compras navideñas con significativas rebajas en muchas tiendas minoristas y grandes almacenes.
# Sucede después de la celebración de Acción de Gracias en Estados Unidos.
# Suponga que posee los datos de los productos de una tienda en los siguientes arreglos:
# C: códigos de todos los productos (cadenas de caracteres)
c=np.array(['COD001','COD002','COD003','COD004','COD005','COD006'])
# P: precios en dólares para cada uno de los productos (valores con decimales).
p=np.random.randint(20,50,6,int)
# D: descuentos asociados a cada producto (enteros entre 0 y 100)
d=np.random.randint(0,100,6,int)
# S: nombre de la sección donde se encuentra cada producto (cadenas de caracteres)
s=np.array(['Electrodomestico','Enlatados','Electrodomestico','Calzado','Ropa','Automovil'])
# Se requiere implementar las siguientes funciones

#  calcularPrecio(codigo,C,P,D) que recibe un código y los arreglos C,P,D y retorna el precio final del producto, aplicando el descuento correspondiente.
# Para calcular el precio final, aplique las siguiente fórmula:

#precio_final= precio-precio(descuento/100)