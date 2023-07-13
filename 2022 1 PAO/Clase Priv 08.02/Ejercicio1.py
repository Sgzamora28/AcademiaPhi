# Asuma que tiene un archivo hospital.csv con la medicación diaria para varios pacientes hospitalizados. El formato del archivo es el siguiente:

# Paciente: Nombre paciente 1,habitación
# Medicacion
# Nombre medicina,Cantidad de Pastillas diarias
# ...
# Paciente: Nombre paciente 2,habitacion
# ...

# Ejemplo:
#################################################################################################################
# Paciente: Juan Andrade,401
# Medicacion
# Enoxaparina,1
# Furosemida,3
# Paciente: Ana Mora,305
# Medicacion
# Acetaminofen,2
# Levofloxacina,2
# Nitazoxanida,1
# ...
# El primer dígito del número de habitación indica el piso donde se encuentra dicha habitación.
#################################################################################################################

#  Restricciones:

# En todo su código (incluyendo programa principal y funciones) sólo podrá abrir el archivo de datos una (1) sola vez, directa o indirectamente.
# Ejemplo: tener el open dentro de una función propia que es invocada varias veces en su programa, se considera como múltiples aperturas del archivo. 
# Ante la duda, pregunte a su profesor si lo que está haciendo es correcto o no.

# El archivo no podrá ser almacenado totalmente a listas, listas de listas o listas paralelas.
# Implemente un programa que:

# Pida el nombre de una medicina y muestre por pantalla:

# [15 puntos] Los números de habitación y los nombres de todos los pacientes que toman la medicina solicitada por teclado.
# [10 puntos] La cantidad total de pastillas necesarias para atender las necesidades de todos los pacientes del hospital que toman esta medicina en un día.
#             Formato de salida para la medicina "XX":

#Habitación   Paciente
# 305         Ana Mora
# 217         Rodrigo Caballero
# 423         Pedro Moreno
# ...
# Total de pastillas de XX requeridas: 14

# [10 puntos] Escriba un archivo con el formato anterior, el archivo debe tener el nombre de la pastila.
# [5 puntos] Muestre por pantalla la habitación y el piso donde se encuentra el paciente Kyra Franco.

# Nota: para este tema usted puede implementar las funciones y estructuras de datos de apoyo que considere oportunas.

# arch=open('hospital.csv')

pastilla=input('Indique el nombre de la pastilla: ')
with open('Clase Priv 08.02\hospital.csv') as arch:
  f=open('Clase Priv 08.02\{}.txt'.format(pastilla),'w')
  encabezado='Habitación   Paciente'
  print(encabezado)
  f.write(encabezado+'\n')
  dosis_diaria=0
  for line in arch:
    if 'Paciente' in line:
      paciente_habitcion=line.strip().split(':')[1]#Paciente: Juan Andrade,401--> ['Paciente','Jose Andrade,401']--->'Jose Andrade,401'
      paciente,habitacion=paciente_habitcion.split(',')#---->['Jose Andrade','401']
      if "Kyra Franco" in paciente:
        kyraHab=habitacion
    
    if pastilla in line:
      datos='{:11s} {}'.format(habitacion,paciente)
      print(datos)
      f.write(datos+'\n')
      medicamento,dosis=line.strip().split(',')
      dosis_diaria+=int(dosis)
  total=f'\nTotal de pastillas de {pastilla} requeridas: {dosis_diaria}'
  print(total)
  f.write(total)
  f.close()
  print('El piso y la habitacion de la paciente Kyra Franco son {} piso, habitacion {}'.format(kyraHab[0],kyraHab))