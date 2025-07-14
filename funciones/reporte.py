import pandas as pd

from modelos.reporte import Reporte
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_reportes_desde_excel() -> list:
    df = pd.read_excel("documents/reporte.xlsx")
    return [
        Reporte(
            int(row["Codigo Emision"]),
            int(row["Codigo Empresa"]),
            row["Nombre Empresa"],
            int(row["Codigo Local"]),
            row["Nombre Local"],
            int(row["Codigo Ciiu"]),
            row["Descripcion Ciiu"],
            row["Sustancia Química"],
            row["Cuerpo Receptor"],
            row["Nombre Cuerpo Receptor"],
            row["Unidad de Medida"],
            int(row["Cantidad"]),
            row["Método de cálculo"]
        )
        
        for _, row in df.iterrows()
    ]

def obtener_reportes_ordenadas_por_criterio(criterio, descendente: bool = False) -> list:
    reportes = cargar_reportes_desde_excel()
    reportes = quicksort(reportes, criterio, descendente)

    return reportes

def buscar_reportes_por_clave_criterio(clave, criterio, reportes: list = []) -> list:
    if not reportes:
        reportes = obtener_reportes_ordenadas_por_criterio(criterio)
    
    reportes = busqueda_binaria(reportes, clave, criterio)

    return reportes

def registrar_reporte(reporte: Reporte):
    nueva_fila = {
        "Codigo Emision": reporte.codigo_emision,
        "Codigo Empresa": reporte.codigo_empresa,
        "Nombre Empresa": reporte.nombre_empresa,
        "Codigo Local": reporte.codigo_local,
        "Nombre Local": reporte.nombre_local,
        "Codigo Ciiu": reporte.codigo_ciiu,
        "Descripcion Ciiu": reporte.descripcion_ciiu,
        "Cuerpo Receptor": reporte.cuerpo_receptor,
        "Nombre Cuerpo Receptor": reporte.nombre_cuerpo_receptor,
        "Cantidad": reporte.cantidad,
        "Unidad de Medida": reporte.unidad_medida,
        "Sustancia Química": reporte.sustancia,
        "Método de cálculo": reporte.metodo_calculo
    }

    ruta_fichero = "documents/reporte.xlsx"

    df = pd.read_excel(ruta_fichero)
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_excel(ruta_fichero, index=False)