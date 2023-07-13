dregistros = {
('CPG001', 1): { 'Josué Lucas', 'Naomi Quimis' },
('ALG001', 6): { 'Mabel Hidalgo', 'Sheila Pincay' },
('ALG001', 7): { 'Diana Mendoza', 'Josué Lucas','Frank Malo' },
('CPG001', 2): { 'Frank Malo', 'Mabel Hidalgo' },
('CPG001', 3): { 'Kevin Magallanes', 'Joselyn Rojas' },
('ALG001', 10): { 'Lisbeth Pacha', 'Margarita Campoverde' },
('CAL001', 1): { 'Frank Malo', 'Margarita Campoverde','Naomi Quimis' },
}

# genere un conjunto que contenga los estudiantes que est;an viendo calculo y algebra al mismo tiempo
estudiantes={}
for key,value in dregistros.items():
  if key[0] not in estudiantes:
    estudiantes[key[0]]=set()
  
  estudiantes[key[0]]=estudiantes[key[0]].union(dregistros[key])



materias=set()
cod_materia=''
while cod_materia!='*':
  cod_materia=input('Ingrese el codigo de la materia')
  if cod_materia!='*':
    materias.add(cod_materia)

interseccion=set()
for key,value in estudiantes.items():
    if key in materias:
      
      if len(interseccion)==0:
        interseccion.update(value)

      else:
        interseccion=interseccion&value

print(interseccion)