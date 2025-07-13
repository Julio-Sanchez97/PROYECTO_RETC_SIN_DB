from modelos.local import Local
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_locales_desde_csv() -> list:
    locales = []
    with open("documents/locales.csv", "r", encoding="utf-8") as f:
        for linea in f:
            campos = linea.strip().split(",")
            local = Local(
                codigo_local=int(campos[0]),
                codigo_empresa=int(campos[1]),
                nombre_local=campos[2],
                departamento=campos[3],
                ciudad=campos[4],
                distrito=campos[5],
                coordenadas=campos[6]
            )
            locales.append(local)
    return locales

def obtener_locales_ordenadas_por_criterio(criterio) -> list:
    locales = cargar_locales_desde_csv()
    locales = quicksort(locales, criterio)

    return locales

def buscar_locales_por_clave_criterio(clave, criterio) -> list:
    locales = obtener_locales_ordenadas_por_criterio(criterio)
    locales = busqueda_binaria(locales, clave, criterio)

    return locales