import pandas as pd

from modelos.sustancia import Sustancia
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_sustancia_desde_excel() -> list:
    df = pd.read_excel("documents/sustancias_químicas.xlsx")
    return [
        Sustancia(
            int(row["Codigo"]),
            row["Sustancia"],
            row["CAS"]
        )
        
        for _, row in df.iterrows()
    ]

def obtener_sustancias_ordenadas_por_criterio(criterio) -> list:
    sustancias = cargar_sustancia_desde_excel()
    sustancias = quicksort(sustancias, criterio)

    return sustancias

def buscar_sustancia_por_clave_criterio(clave, criterio, sustancias: list = []) -> list:
    if not sustancias:
        sustancias = obtener_sustancias_ordenadas_por_criterio(criterio)
        
    sustancias = busqueda_binaria(sustancias, clave, criterio)

    return sustancias