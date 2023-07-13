import numpy as np

x=np.array([1,2,3,4,6,7,True])
y=np.array(['Steven','Kyra','Fernando','Daniel',3])
z=np.array([[2.5,6.2,3.4,2.0],[5,3,4,2.5]])

#Propiedades

# #tipo de datos
# tipo=z.dtype
# print(tipo)

# #cantidad de elementos
# elementos=y.size
# print(elementos)


# #dimension

# dimension=z.ndim
# print(dimension)


# #filas y columnas

# filas,columnas=z.shape
# print(filas,columnas)


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

def calcular(codigo,codigos,precios,descuentos):
  # i=codigos.index(codigo)
  # precio_final=precios[i]-(precios[i]*(descuentos[i]/100))
  # return precio_final

# x=calcular('COD001',c.tolist(),p.tolist(),d.tolist())
# print(x)
  comprobador=codigos==codigo
  preciofinal=precios[comprobador]-(precios[comprobador]*(descuentos[comprobador]/100))
  return preciofinal

print(calcular('COD002',c.tolist(),p.tolist(),d.tolist()))



# 2. calcularTotal(compras,C,P,D) que recibe una lista de compras con los códigos de los productos, 
# los arreglos C,P,D y aplicando todos los descuentos calcula el valor total a pagar 

def calcularTotal(compras:list,codigos:np.ndarray,precios:np.ndarray,descuentos:np.ndarray):
  valorTotal=0
  for compra in range(compras.size):
    x=calcular(codigos[compra],codigos,precios,descuentos)
    valorTotal+=x

  return valorTotal


# 3. hallarSecciones(compras,C,S) que recibe una lista de compras con los códigos de los productos, 
# los arreglos C y S y determina las secciones que deberán visitar durante las compras. La lista de visitas no tiene elementos repetidos.

def hallarSecciones(compras:list,codigos:np.ndarray,secciones:np.ndarray):
  tour=set()
  for compra in compras:
    i=np.where(codigos==compra)
    x=secciones[i][0]
    tour.add(x)
  
  return list(tour)


x=hallarSecciones(['COD001','COD003',"COD005"],c,s)
print(x)