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


print("-"*275)
print("=== Menú de opciones ===")
print("1. Ordenar por residencia")
print("2. Ordenar por salario")
print("3. Ordenar por trabajo")
print("4. Salir\n")
print("Seleccione el número de la opción que desea ejecutar")

respuesta = int(input())


