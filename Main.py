import csv
import Funciones

archivocsv = open('C:/Users/figue/Desktop/salaries.csv')
salarios = csv.reader(archivocsv, delimiter=';')

trabajo = []
salario = []

for fila in salarios:
    trabajo.append(fila[3])
    salario.append(fila[6])

trabajo.pop(0)
salario.pop(0)

salarioordenado = Funciones.merge_sort_num(salario)

trabajoordenado = Funciones.merge_sort_strings(trabajo)

#for i in trabajoordenado:
    #print(i)

for i in salarioordenado:
    print(i)


