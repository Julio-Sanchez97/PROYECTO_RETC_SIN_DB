import pandas as pd

from modelos.cuerpo_receptor import CuerpoReceptor
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_cuerpo_receptor_desde_excel() -> list:
    df = pd.read_excel("documents/cuerpos_receptores.xlsx")
    return [
        CuerpoReceptor(
            int(row["CODIGO"]),
            row["DESCRIPCION"],
            row["COD_TIPO"]
        )
        
        for _, row in df.iterrows()
    ]

def obtener_cuerpos_receptores_ordenadas_por_criterio(criterio) -> list:
    cuerpos_receptores = cargar_cuerpo_receptor_desde_excel()
    cuerpos_receptores = quicksort(cuerpos_receptores, criterio)

    return cuerpos_receptores

def buscar_cuerpo_receptor_por_clave_criterio(clave, criterio, cuerpos_receptores: list = []) -> list:
    if not cuerpos_receptores:
        cuerpos_receptores = obtener_cuerpos_receptores_ordenadas_por_criterio(criterio)
        
    cuerpos_receptores = busqueda_binaria(cuerpos_receptores, clave, criterio)

    return cuerpos_receptores