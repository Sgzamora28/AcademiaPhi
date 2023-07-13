#metodo 1
# arch=open('Clase 07.13\\ejercicio1.txt')
# for line in arch:
#   line=line.strip()
#   line=line.replace('chi','')
#   print(line)

# arch.close()


#metodo 2
with open('Clase 07.13\\ejercicio1.txt') as f:
  for line in f:
    line=line.strip()
    line=line.replace('chi','')
    print(line)