import pandas as pd

from modelos.ciiu import Ciiu
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_ciius_desde_excel() -> list:
    df = pd.read_excel("documents/ciiu.xlsx")
    return [
        Ciiu(
            int(row["Código CIIU"]),
            row["CIIU"]
        )
        
        for _, row in df.iterrows()
    ]

def obtener_ciius_ordenadas_por_criterio(criterio) -> list:
    ciius = cargar_ciius_desde_excel()
    ciius = quicksort(ciius, criterio)

    return ciius

def buscar_ciius_por_clave_criterio(clave, criterio, ciius: list = []) -> list:
    if not ciius:
        ciius = obtener_ciius_ordenadas_por_criterio(criterio)
        
    ciius = busqueda_binaria(ciius, clave, criterio)

    return ciius