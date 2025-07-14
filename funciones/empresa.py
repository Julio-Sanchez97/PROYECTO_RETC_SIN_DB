import pandas as pd

from modelos.empresa import Empresa
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_empresas_desde_excel() -> list:
    df = pd.read_excel("documents/empresas.xlsx")
    return [
        Empresa(
            int(row["Codigo Empresa"]),
            row["Razon Social"],
            row["Ruc"],
            int(row["Codigo Ciiu"]),
            row["Descripción Ciiu"],
            row["Representante Legal"],
            row["Correo"],
            row["Telefono"]
        )
        
        for _, row in df.iterrows()
    ]

def obtener_empresas_ordenadas_por_criterio(criterio) -> list:
    empresas = cargar_empresas_desde_excel()
    empresas = quicksort(empresas, criterio)

    return empresas

def buscar_empresas_por_clave_criterio(clave, criterio, empresas: list = []) -> list:
    if not empresas:
        empresas = obtener_empresas_ordenadas_por_criterio(criterio)
    
    empresas = busqueda_binaria(empresas, clave, criterio)

    return empresas

def generar_codigo_empresa() -> int:
    empresas = obtener_empresas_ordenadas_por_criterio(lambda e: e.codigo_empresa)
    posicion_final = len(empresas) - 1

    return empresas[posicion_final].codigo_empresa + 1

def registrar_empresa(empresa: Empresa):
    nueva_fila = {
        "Codigo Empresa": empresa.codigo_empresa,
        "Razon Social": empresa.razon_social,
        "Ruc": empresa.ruc,
        "Codigo Ciiu": empresa.codigo_actividad_ciiu,
        "Descripción Ciiu": empresa.actividad,
        "Representante Legal": empresa.representante_legal,
        "Correo": empresa.correo_electronico,
        "Telefono": empresa.telefono
    }

    ruta_fichero = "documents/empresas.xlsx"

    df = pd.read_excel(ruta_fichero)
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_excel(ruta_fichero, index=False)