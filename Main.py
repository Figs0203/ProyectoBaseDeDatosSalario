import csv
import Funciones

archivocsv = open('C:/Users/figue/Desktop/salaries.csv')
salarios = csv.reader(archivocsv, delimiter=';')

matriz = []

for fila in salarios:
    matriz.append(fila)

# Crear una lista para almacenar los diccionarios resultantes
diccionarios = []

# Iterar sobre las filas de la matriz, excluyendo la primera fila que contiene las claves
for fila in matriz[1:]:
    # Crear un diccionario vacío para esta fila
    diccionario_fila = {}
    # Iterar sobre los elementos de la primera fila y los elementos de la fila actual
    for clave, valor in zip(matriz[0], fila):
        # Asignar el valor actual al diccionario usando la clave correspondiente
        diccionario_fila[clave] = valor
    # Agregar el diccionario creado a la lista de diccionarios
    diccionarios.append(diccionario_fila)

print("-"*275)
print("=== Menú de opciones ===")
print("1. Ordenar por residencia (Bubble_sort)")
print("2. Ordenar por salario (Bubble_sort)")
print("3. Ordenar por trabajo (Bubble_sort)")
print("4. Ordenar por residencia (Merge_sort")
print("5. Ordenar por salario (Merge_sort")
print("6. Ordenar por trabajo (Merge_sort")
print("7. Salir\n")

respuesta = int(input("Seleccione el número de la opción que desea ejecutar: "))

if respuesta == 1:
    dic_residence = Funciones.bubble_sort_strings(diccionarios, "employee_residence")
    with open('salida.txt', 'w', encoding='utf-8') as archivo:
        for diccionario in dic_residence:
            # Redirige la salida de print() al archivo
            print(f"Año: {diccionario["work_year"]} | Nivel de experiencia: {diccionario["experience_level"]} "
                  f"| Tipo de empleo: {diccionario["employment_type"]} | Trabajo: {diccionario["job_title"]} "
                  f"| Salario (en usd): {diccionario["salary_in_usd"]} "
                  f"| Residencia del empleado: {diccionario["employee_residence"]} "
                  f"| Ubicación de la compañía: {diccionario["company_location"]} "
                  f"| Tamaño de la compañía: {diccionario["company_size"]}\n", file=archivo)


elif respuesta == 2:
    dic_salary = Funciones.bubble_sort_num(diccionarios, "salary_in_usd")
    with open('salida.txt', 'w', encoding='utf-8') as archivo:
        for diccionario in dic_salary:
            # Redirige la salida de print() al archivo
            print(f"Año: {diccionario["work_year"]} | Nivel de experiencia: {diccionario["experience_level"]} "
                  f"| Tipo de empleo: {diccionario["employment_type"]} | Trabajo: {diccionario["job_title"]} "
                  f"| Salario (en usd): {diccionario["salary_in_usd"]} "
                  f"| Residencia del empleado: {diccionario["employee_residence"]} "
                  f"| Ubicación de la compañía: {diccionario["company_location"]} "
                  f"| Tamaño de la compañía: {diccionario["company_size"]}\n", file=archivo)


elif respuesta == 3:
    dic_job = Funciones.bubble_sort_strings(diccionarios, "job_title")
    with open('salida.txt', 'w', encoding='utf-8') as archivo:
        for diccionario in dic_job:
            # Redirige la salida de print() al archivo
            print(f"Año: {diccionario["work_year"]} | Nivel de experiencia: {diccionario["experience_level"]} "
                  f"| Tipo de empleo: {diccionario["employment_type"]} | Trabajo: {diccionario["job_title"]} "
                  f"| Salario (en usd): {diccionario["salary_in_usd"]} "
                  f"| Residencia del empleado: {diccionario["employee_residence"]} "
                  f"| Ubicación de la compañía: {diccionario["company_location"]} "
                  f"| Tamaño de la compañía: {diccionario["company_size"]}\n", file=archivo)

elif respuesta == 4:
    dic_residence = Funciones.merge_sort_strings(diccionarios, "employee_residence")
    with open('salida.txt', 'w', encoding='utf-8') as archivo:
        for diccionario in dic_residence:
            # Redirige la salida de print() al archivo
            print(f"Año: {diccionario["work_year"]} | Nivel de experiencia: {diccionario["experience_level"]} "
                  f"| Tipo de empleo: {diccionario["employment_type"]} | Trabajo: {diccionario["job_title"]} "
                  f"| Salario (en usd): {diccionario["salary_in_usd"]} "
                  f"| Residencia del empleado: {diccionario["employee_residence"]} "
                  f"| Ubicación de la compañía: {diccionario["company_location"]} "
                  f"| Tamaño de la compañía: {diccionario["company_size"]}\n", file=archivo)

elif respuesta == 5:
    dic_salary = Funciones.merge_sort_num(diccionarios, "salary_in_usd")
    with open('salida.txt', 'w', encoding='utf-8') as archivo:
        for diccionario in dic_salary:
            # Redirige la salida de print() al archivo
            print(f"Año: {diccionario["work_year"]} | Nivel de experiencia: {diccionario["experience_level"]} "
                  f"| Tipo de empleo: {diccionario["employment_type"]} | Trabajo: {diccionario["job_title"]} "
                  f"| Salario (en usd): {diccionario["salary_in_usd"]} "
                  f"| Residencia del empleado: {diccionario["employee_residence"]} "
                  f"| Ubicación de la compañía: {diccionario["company_location"]} "
                  f"| Tamaño de la compañía: {diccionario["company_size"]}\n", file=archivo)

elif respuesta == 6:
    dic_job = Funciones.merge_sort_strings(diccionarios, "job_title")
    with open('salida.txt', 'w', encoding='utf-8') as archivo:
        for diccionario in dic_job:
            # Redirige la salida de print() al archivo
            print(f"Año: {diccionario["work_year"]} | Nivel de experiencia: {diccionario["experience_level"]} "
                  f"| Tipo de empleo: {diccionario["employment_type"]} | Trabajo: {diccionario["job_title"]} "
                  f"| Salario (en usd): {diccionario["salary_in_usd"]} "
                  f"| Residencia del empleado: {diccionario["employee_residence"]} "
                  f"| Ubicación de la compañía: {diccionario["company_location"]} "
                  f"| Tamaño de la compañía: {diccionario["company_size"]}\n", file=archivo)

elif respuesta == 7:
    print("Adiós")

else:
    print("Ingrese un caracter válido")
