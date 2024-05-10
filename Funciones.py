def bubble_sort(lista):
    length = len(lista)
    for i in range(length):
        for j in range(0, (length - i) - 1):

            if lista[j] > lista[j + 1]:
                auxiliar = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = auxiliar
    return lista


def merge_sort_num(lista):
    if len(lista) < 2:
        return lista

    else:
        middle = len(lista) // 2
        right = merge_sort_num(lista[:middle])
        left = merge_sort_num(lista[middle:])
        return merge_num(right, left)


def merge_num(lista1, lista2):
    i, j = 0, 0
    result = []

    while i < len(lista1) and j < len(lista2):
        # Comparar por el número de dígitos primero
        if len(str(lista1[i])) > len(str(lista2[j])):
            result.append(lista1[i])
            i += 1
        elif len(str(lista1[i])) < len(str(lista2[j])):
            result.append(lista2[j])
            j += 1
        else:
            # Si tienen el mismo número de dígitos, comparar los valores
            if lista1[i] > lista2[j]:
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1

    result += lista1[i:]
    result += lista2[j:]

    return result


def merge_sort_strings(lista):
    if len(lista) < 2:
        return lista

    else:
        middle = len(lista) // 2
        right = merge_sort_strings(lista[:middle])
        left = merge_sort_strings(lista[middle:])
        return merge_strings(right, left)


def merge_strings(lista1, lista2):
    i, j = 0, 0
    result = []

    while i < len(lista1) and j < len(lista2):
        # Comparar las palabras completas
        if lista1[i] < lista2[j]:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    result += lista1[i:]
    result += lista2[j:]

    return result
