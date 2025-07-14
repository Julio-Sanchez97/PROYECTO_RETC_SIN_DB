def quicksort(lista, key, descendente: bool = False):
    if len(lista) <= 1:
        return lista
    else:
        pivote = key(lista[0])
        if descendente:
            menores = [x for x in lista[1:] if key(x) > pivote]
            mayores = [x for x in lista[1:] if key(x) <= pivote]
        else:
            menores = [x for x in lista[1:] if key(x) <= pivote]
            mayores = [x for x in lista[1:] if key(x) > pivote]
        return quicksort(menores, key, descendente) + [lista[0]] + quicksort(mayores, key, descendente)

def busqueda_binaria(lista: list, clave, key) -> list:
    resultado = []
    izquierda = 0
    derecha = len(lista) - 1

    if lista:
        muestra = key(lista[0])
        if isinstance(muestra, int):
            clave = int(clave)
        elif isinstance(muestra, str):
            clave = str(clave)

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor = key(lista[medio])

        if valor == clave:
            i = medio
            while i >= 0 and key(lista[i]) == clave:
                resultado.insert(0, lista[i])
                i -= 1

            i = medio + 1
            while i < len(lista) and key(lista[i]) == clave:
                resultado.append(lista[i])
                i += 1
            break
        elif valor < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return resultado
