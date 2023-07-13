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

# [15 puntos] Los números de habitación y los nombres de todos los pacientes que toman la medicina.
# [10 puntos] La cantidad total de pastillas necesarias para atender las necesidades de todos los pacientes del hospital que toman esta medicina en un día.
#             Formato de salida para la medicina "XX":

#Habitación   Paciente
# 305         Ana Mora
# 217         Rodrigo Caballero
# 423         Pedro Moreno
# ...
# Total de pastillas de XX requeridas: 14
# [5 puntos] Muestre por pantalla la habitación y el piso donde se encuentra el paciente Kyra Franco.

# Nota: para este tema usted puede implementar las funciones y estructuras de datos de apoyo que considere oportunas.

# arch=open('hospital.csv')







# arch.close()
med=input('Ingrese el nombre de una medicina: ').title()
with open('hospital.csv') as arch:
  pacientes=[]
  dosis_total=0
  for line in arch:
    if 'Paciente' in line:
      l_paciente=line.strip().split(' ')#----> ['Paciente:','Juan', 'Andrade,401']---> Juan Andrade,401
      paciente,habitacion=(l_paciente[1]+' '+l_paciente[2]).split(',')#----->['Juan Andrade','401']
      
    if med in line:
      pacientes.append((paciente,habitacion))
      dosis=line.strip().split(',')[1]#---->['nomPastilla','dosis']
      dosis_total+=int(dosis)

    if 'Kyra Franco' in line:
      piso=habitacion[0]
      print("La paciente Kyra Fracno esta en la habitacion: {} en el piso {}\n".format(habitacion,piso))

print("{:^12} {}".format('Habitacion','Paciente'))
for paciente in pacientes:
  nombre,habitacion=paciente
  print("{1:^12} {0:}".format(nombre,habitacion))

print("\nTotal de pastillas de {} requeridas: {}".format(med,dosis_total))