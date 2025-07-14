import pandas as pd

from modelos.reporte import Reporte

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
        "Cantidad": reporte.cantidad,
        "Unidad de Medida": reporte.unidad_medida,
        "Sustancia Química": reporte.sustancia,
        "Método de cálculo": reporte.metodo_calculo
    }

    ruta_fichero = "documents/reporte.xlsx"

    df = pd.read_excel(ruta_fichero)
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_excel(ruta_fichero, index=False)