from modelos.emision import Emision
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_emisiones_desde_csv() -> list:
    emisiones = []
    with open("documents/emisiones.csv", "r", encoding="utf-8") as f:
        next(f)
        for linea in f:
            campos = linea.strip().split(",")
            emision = Emision(
                codigo_emision=int(campos[0]),
                codigo_empresa=int(campos[1]),
                codigo_local=int(campos[2]),
                sustancia=campos[3],
                cuerpo_receptor=campos[4],
                nombre_cuerpo_receptor=campos[5],
                unidad_medida=campos[6],
                cantidad=float(campos[7]),
                metodo_calculo=campos[8]
            )
            emisiones.append(emision)
    
    return emisiones

def obtener_emisiones_ordenadas_por_criterio(criterio) -> list:
    emisiones = cargar_emisiones_desde_csv()
    emisiones = quicksort(emisiones, criterio)

    return emisiones

def buscar_emisiones_por_clave_criterio(clave, criterio) -> list:
    emisiones = obtener_emisiones_ordenadas_por_criterio(criterio)
    emisiones = busqueda_binaria(emisiones, clave, criterio)

    return emisiones