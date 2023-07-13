d_medicinas={
             'Loratadina': ['Botica Barcia', 'Medicity', 'Pharmacys', 'Santa Martha', 'SuFarmacia'], 
             'Mentol': ['Medicity', 'Pharmacys', 'Sana Sana', 'Santa Martha', 'Botica Barcia'], 
             'Ibuprofeno': ['Genovesa', 'Pharmacys', 'SuFarmacia', 'Ecu-Vida','Medicity'], 
             'Paracetamol': ['Cruz Azul', 'Santa Martha', 'Ecu-Vida', 'FarMed', 'Fybeca', 'Farmacias Economicas', 'Farmacias Comunitarias', 
                             'Medicity', 'SuFarmacia', 'Botica Barcia', 'Sana Sana'], 
             'Omeprazol': ['Cruz Azul', 'Farmacias Economicas', 'FarMed', 'Fybeca','Medicity'], 
             'Metamizol': ['Santa Martha', 'Sana Sana', 'Farmacias Comunitarias', 'Pharmacys', 'Farmacias Economicas', 'Ecu-Vida', 
                           'Fybeca', 'FarMed', 'Cruz Azul', 'Medicity', 'SuFarmacia', 'Genovesa', 'Botica Barcia'], 
             'Diclofenaco': ['Genovesa', 'Santa Martha', 'FarMed', 'Farmacias Economicas', 'Botica Barcia', 'Ecu-Vida', 'Medicity', 'Cruz Azul', 
                             'Farmacias Comunitarias'], 
             'Aspirina': ['FarMed', 'Santa Martha', 'Fybeca', 'Farmacias Economicas', 'Genovesa', 'Medicity', 'Cruz Azul', 'Ecu-Vida', 
                          'Botica Barcia', 'SuFarmacia'], 
             'Amoxicilina': ['Sana Sana', 'Genovesa', 'Farmacias Economicas', 'Farmacias Comunitarias', 'Ecu-Vida', 'Fybeca', 'Pharmacys', 
                             'SuFarmacia', 'Medicity'], 
             'Albendazol': ['Medicity', 'FarMed', 'Genovesa', 'Farmacias Economicas', 'Cruz Azul', 'SuFarmacia', 'Ecu-Vida', 'Pharmacys', 
                            'Botica Barcia', 'Fybeca'], 
             'Vitamina C': ['Genovesa', 'Fybeca', 'Santa Martha', 'Medicity', 'Pharmacys', 'Sana Sana', 'FarMed', 'Ecu-Vida', 'Botica Barcia', 
                            'Farmacias Comunitarias', 'Cruz Azul', 'SuFarmacia'], 
             'Complejo B': ['Santa Martha', 'Cruz Azul', 'Fybeca', 'SuFarmacia', 'Farmacias Economicas', 'Botica Barcia', 
                            'Ecu-Vida', 'Genovesa', 'FarMed', 'Sana Sana', 'Farmacias Comunitarias', 'Medicity'], 
             'Calcio': ['Fybeca', 'Farmacias Comunitarias', 'SuFarmacia', 'Botica Barcia', 'Sana Sana', 'Farmacias Economicas', 
                        'Pharmacys', 'Medicity', 'Santa Martha', 'FarMed', 'Cruz Azul'], 
             'Pharmaton Vitality': ['Cruz Azul', 'Pharmacys', 'Sana Sana', 'Santa Martha', 'Ecu-Vida', 'Genovesa', 'Farmacias Comunitarias', 
                                    'Farmacias Economicas', 'Medicity', 'Botica Barcia', 'SuFarmacia', 'FarMed'], 
             'Suero Oral': ['Medicity','Farmacias Comunitarias', 'Pharmacys', 'Fybeca', 'Sana Sana', 'Ecu-Vida', 'Cruz Azul', 'Santa Martha'], 
             'Pedialyte': ['Farmacias Comunitarias', 'Ecu-Vida', 'Cruz Azul', 'Medicity', 'Santa Martha', 'Sana Sana', 'Farmacias Economicas'], 
             'Ventolin': ['Botica Barcia', 'Farmacias Economicas', 'Genovesa', 'Santa Martha', 'Cruz Azul', 'Fybeca', 'Pharmacys', 
                          'Medicity', 'FarMed', 'Farmacias Comunitarias', 'Sana Sana', 'Ecu-Vida']}

l_medicinas=['Loratadina', 'Mentol', 'Ibuprofeno', 'Paracetamol', 'Omeprazol', 'Metamizol', 'Diclofenaco', 'Aspirina', 'Amoxicilina', 
             'Albendazol', 'Vitamina C', 'Complejo B', 'Calcio', 'Pharmaton Vitality', 'Suero Oral', 'Pedialyte', 'Ventolin']


# 1. [15 puntos] Use el diccionario d_medicinas para mostrar por pantalla los nombres de todas las farmacias. 
# No repita nombres de farmacias. Para resolver este numeral solo debe usar conjuntos 
# (no es permitido usar otras colecciones como diccionarios, listas, tuplas o arreglos de Numpy).
total=set()#es un conjunto con todas las farmacias
for medicina in d_medicinas:
  lista=d_medicinas[medicina]
  total.update(lista)

# print(total)
# 2. [15 puntos] Use el diccionario d_medicinas para mostrar por pantalla los nombres de las 
# farmacias que venden todas las medicinas que se encuentran en una superlista dada, l_medicinas. 
# Para resolver este numeral solo debe usar conjuntos 
# (no es permitido usar otras colecciones como diccionarios, listas, tuplas o arreglos de Numpy).
todas=set()#TODAS LAS FARMACIAS
for farmacia in total:
  validacion=True
  for lista in d_medicinas.values():
    if farmacia in lista:
      validacion=validacion and True
    else:
      validacion=validacion and False
  if validacion:
    todas.add(farmacia)
# print(todas)

# [15 puntos] Usando la información en el primer diccionario, forme un nuevo diccionario con la siguiente estructura:
# Farmacia: [medicina_1, medicina_2, ...]
# Ejemplo:
# d_farmacias = {
# "Sana Sana":["Aspirina", "Mentol", ...],
# "Botica Barcia":["Mentol", "Loratadina", ...],
# ...,
# "Cruz Azul":["Aspirina", "Vitamina C", ...],
# ...,
# }

d_farmacias={}
for farmacia in total:
  d_farmacias[farmacia]=[]
  for medicina in d_medicinas:
    if farmacia in d_medicinas[medicina]:
      d_farmacias[farmacia].append(medicina)
print(d_farmacias)