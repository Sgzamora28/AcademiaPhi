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
# Se requiere implementar las siguientes funciones:

#  calcularPrecio(codigo,C,P,D) que recibe un código y los arreglos C,P,D y retorna el precio final del producto, aplicando el descuento correspondiente.
# Para calcular el precio final, aplique las siguiente fórmula:

#precio_final= precio-precio(descuento/100)

def calcularPrecio(codigo:str,c:np.ndarray,p:np.ndarray,d:np.ndarray):
  # verif=c==codigo
  verificador=np.where(c==codigo)
  v_precios=p[verificador][0]
  v_descuentos=d[verificador][0]
  precio_final=v_precios-v_precios*(v_descuentos/100)
  return precio_final



x=calcularPrecio('COD001',c,p,d)
print(x)


# 2. calcularTotal(compras,C,P,D) que recibe una lista de compras con los códigos de los productos, 
# los arreglos C,P,D y aplicando todos los descuentos calcula el valor total a pagar 

def total(compras,codigos,p,d):
  total=0
  for compra in compras:
    x=calcularPrecio(compra,codigos,p,d)
    total+=x
  return total

compras=['COD001','COD002','COD003']
x=total(compras,c,p,d)
print(x)

# 3. hallarSecciones(compras,C,S) que recibe una lista de compras con los códigos de los productos, 
# los arreglos C y S y determina las secciones que deberán visitar durante las compras. La lista de visitas no tiene elementos repetidos.
def hallarSeccion(compras:list,codigos:np.ndarray,secciones:np.ndarray):
  visitas=set()
  for compra in compras:
    x=np.where(codigos==compra)
    i_secciones=secciones[x][0]
    visitas.add(i_secciones)
  return list(visitas)


x=hallarSeccion(compras,c,s)
print(x)