import csv

def guardar_emisiones_reporte_csv(emisiones_reporte: list, ruta_archivo: str):
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        writer.writerow([
            "Codigo_Emision",
            "Codigo_Empresa", "Nombre_Empresa",
            "Codigo_Local", "Nombre_Local",
            "Sustancia", "Cuerpo receptor", "Nombre del cuerpo receptor",
            "Unidad de medida", "Cantidad", "Método de cálculo"
        ])
        
        for e in emisiones_reporte:
            writer.writerow([
                e.codigo_emision,
                e.codigo_empresa, e.nombre_empresa,
                e.codigo_local, e.nombre_localidad,
                e.sustancia,
                e.cuerpo_receptor,
                e.nombre_cuerpo_receptor,
                e.unidad_medida,
                e.cantidad,
                e.metodo_calculo
            ])