def bubble_sort_num(lista, clave):
    length = len(lista)
    for i in range(length):
        for j in range(0, (length - i) - 1):
            # Obtener los valores asociados con la clave en los diccionarios j y j + 1
            valor_j = lista[j][clave]
            valor_j1 = lista[j + 1][clave]

            # Convertir los valores a cadenas y obtener su longitud
            valor_j_str = str(valor_j)
            valor_j1_str = str(valor_j1)
            len_j = len(valor_j_str)
            len_j1 = len(valor_j1_str)

            # Comparar los valores teniendo en cuenta su longitud
            if len_j > len_j1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            elif len_j == len_j1 and valor_j > valor_j1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_strings(lista, clave):
    length = len(lista)
    for i in range(length):
        for j in range(0, (length - i) - 1):
            # Obtener los valores asociados con la clave en los diccionarios j y j + 1
            valor_j = lista[j][clave]
            valor_j1 = lista[j + 1][clave]

            # Comparar las cadenas alfabéticamente
            if valor_j > valor_j1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def merge_sort_num(lista, clave):
    if len(lista) < 2:
        return lista

    else:
        middle = len(lista) // 2
        right = merge_sort_num(lista[:middle], clave)
        left = merge_sort_num(lista[middle:], clave)
        return merge_num(right, left, clave)


def merge_num(lista1, lista2, clave):
    i, j = 0, 0
    result = []

    while i < len(lista1) and j < len(lista2):
        # Comparar por el número de dígitos primero
        if len(str(lista1[i][clave])) > len(str(lista2[j][clave])):
            result.append(lista1[i])
            i += 1
        elif len(str(lista1[i][clave])) < len(str(lista2[j][clave])):
            result.append(lista2[j])
            j += 1
        else:
            # Si tienen el mismo número de dígitos, comparar los valores
            if lista1[i][clave] > lista2[j][clave]:
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1

    result += lista1[i:]
    result += lista2[j:]

    return result


def merge_sort_strings(lista, clave):
    if len(lista) < 2:
        return lista

    else:
        middle = len(lista) // 2
        right = merge_sort_strings(lista[:middle], clave)
        left = merge_sort_strings(lista[middle:], clave)
        return merge_strings(right, left, clave)


def merge_strings(lista1, lista2, clave):
    i, j = 0, 0
    result = []

    while i < len(lista1) and j < len(lista2):
        # Comparar las palabras completas en función de la clave
        if lista1[i][clave] < lista2[j][clave]:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    result += lista1[i:]
    result += lista2[j:]

    return result
