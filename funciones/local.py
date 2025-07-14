import pandas as pd

from modelos.local import Local
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_locales_desde_excel() -> list:
    df = pd.read_excel("documents/locales.xlsx")
    return [
        Local(
            int(row["Codigo Local"]),
            row["Codigo Empresa"],
            row["Nombre Local"],
            row["Departamento"],
            row["Ciudad"],
            row["Distrito"],
            row["Coordenada X"],
            row["Coordenada Y"]
        )
        
        for _, row in df.iterrows()
    ]

def obtener_locales_ordenadas_por_criterio(criterio) -> list:
    locales = cargar_locales_desde_excel()
    locales = quicksort(locales, criterio)

    return locales

def buscar_locales_por_clave_criterio(clave, criterio, locales: list = []) -> list:
    if not locales:
        locales = obtener_locales_ordenadas_por_criterio(criterio)
    
    locales = busqueda_binaria(locales, clave, criterio)

    return locales

def generar_codigo_local() -> int:
    locales = obtener_locales_ordenadas_por_criterio(lambda e: e.codigo_local)
    posicion_final = len(locales) - 1

    return locales[posicion_final].codigo_local + 1

def registrar_local(local: Local):
    nueva_fila = {
        "Codigo Local": local.codigo_local,
        "Codigo Empresa": local.codigo_empresa,
        "Nombre Local": local.nombre_local,
        "Departamento": local.departamento,
        "Ciudad": local.ciudad,
        "Distrito": local.distrito,
        "Coordenada X": local.coordenadas_x,
        "Coordenada Y": local.coordenadas_y
    }

    ruta_fichero = "documents/locales.xlsx"

    df = pd.read_excel(ruta_fichero)
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_excel(ruta_fichero, index=False)