import pandas as pd
from modelos.emision import Emision
from funciones.empresa import buscar_empresas_por_clave_criterio, obtener_empresas_ordenadas_por_criterio
from funciones.local import buscar_locales_por_clave_criterio, obtener_locales_ordenadas_por_criterio
from funciones.cuerpo_receptor import buscar_cuerpo_receptor_por_clave_criterio, obtener_cuerpos_receptores_ordenadas_por_criterio
from funciones.sustancia import buscar_sustancia_por_clave_criterio, obtener_sustancias_ordenadas_por_criterio
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_emisiones_generadas_desde_excel() -> list:
    df = pd.read_excel("documents/emisiones_generadas.xlsx")
    return [
        Emision(
            int(row["COD_EMISION"]),
            int(row["COD_EMPRESA"]),
            int(row["COD_LOCAL"]),
            int(row["Cod_Sustancia"]),
            int(row["Cod_Cuerpo receptor"]),
            row["Nombre del cuerpo receptor"],
            row["Unidad de medida"],
            float(row["Cantidad"]),
            row["Método de cálculo"]
        )
        for _, row in df.iterrows()
    ]

def obtener_emisiones_ordenadas_por_criterio(criterio) -> list:
    emisiones = cargar_emisiones_generadas_desde_excel()
    emisiones = quicksort(emisiones, criterio)

    return emisiones

def buscar_emisiones_por_clave_criterio(clave, criterio) -> list:
    emisiones = obtener_emisiones_ordenadas_por_criterio(criterio)
    emisiones = busqueda_binaria(emisiones, clave, criterio)

    return emisiones

def obtener_ultima_codigo_emision_registrada() -> int:
    emisiones = obtener_emisiones_ordenadas_por_criterio(lambda e: e.codigo_emision)
    posicion_final = len(emisiones) - 1

    return emisiones[posicion_final].codigo_emision

def cargar_emisiones_nuevas_desde_excel() -> list:
    path_entrada = "documents/emisiones_nuevas.xlsx"
    path_salida = "documents/emisiones_generadas.xlsx"
    
    empresas = obtener_empresas_ordenadas_por_criterio(criterio=lambda e: e.codigo_empresa)
    locales = obtener_locales_ordenadas_por_criterio(criterio=lambda e: e.codigo_local)
    sustancias = obtener_sustancias_ordenadas_por_criterio(criterio=lambda e: e.codigo_sustancia)
    cuerpos_receptores = obtener_cuerpos_receptores_ordenadas_por_criterio(criterio=lambda e: e.codigo_cuerpo_receptor)
    emisiones_validas = []

    try:
        df = pd.read_excel(path_entrada, skiprows=3)
    except Exception as e:
        print(f"[ERROR] No se pudo leer '{path_entrada}': {e}")
        return []
    
    ultimo_codigo_emision = obtener_ultima_codigo_emision_registrada()

    for idx, row in df.iterrows():
        fila_excel = idx + 5

        try:
            cod_empresa = int(row["COD_EMPRESA"])
            cod_local = int(row["COD_LOCAL"])
            cod_sustancia = int(row["Cod_Sustancia"])
            cod_cuerpo_receptor = int(row["Cod_Cuerpo receptor"])

            if not buscar_empresas_por_clave_criterio(cod_empresa, lambda c: c.codigo_empresa, empresas):
                raise ValueError(f"Empresa no encontrada (fila {fila_excel})")

            if not buscar_locales_por_clave_criterio(cod_local, lambda c: c.codigo_local, locales):
                raise ValueError(f"Local no encontrado (fila {fila_excel})")

            if not buscar_sustancia_por_clave_criterio(cod_sustancia, lambda c: c.codigo_sustancia,sustancias):
                raise ValueError(f"Sustancia no encontrada (fila {fila_excel})")

            if not buscar_cuerpo_receptor_por_clave_criterio(cod_cuerpo_receptor, lambda c: c.codigo_cuerpo_receptor,cuerpos_receptores):
                raise ValueError(f"Cuerpo receptor no encontrado (fila {fila_excel})")

            ultimo_codigo_emision += 1

            emision = Emision(
                codigo_emision=ultimo_codigo_emision,
                codigo_empresa=cod_empresa,
                codigo_local=cod_local,
                codigo_sustancia=cod_sustancia,
                codigo_cuerpo_receptor=cod_cuerpo_receptor,
                nombre_cuerpo_receptor=row["Nombre del cuerpo receptor"],
                unidad_medida=row["Unidad de medida"],
                cantidad=float(row["Cantidad"]),
                metodo_calculo=row["Método de cálculo"]
            )

            emisiones_validas.append(emision)

        except Exception as e:
            print(f"[ERROR] {e}")
            print("[ABORTADO] No se cargó ninguna emisión.")
            return []

    if emisiones_validas:
        try:
            df_existente = pd.read_excel(path_salida)
        except FileNotFoundError:
            df_existente = pd.DataFrame()

        nuevas_filas = [{
            "COD_EMISION": em.codigo_emision,
            "COD_EMPRESA": em.codigo_empresa,
            "COD_LOCAL": em.codigo_local,
            "Cod_Sustancia": em.codigo_sustancia,
            "Cod_Cuerpo receptor": em.codigo_cuerpo_receptor,
            "Nombre del cuerpo receptor": em.nombre_cuerpo_receptor,
            "Unidad de medida": em.unidad_medida,
            "Cantidad": em.cantidad,
            "Método de cálculo": em.metodo_calculo
        } for em in emisiones_validas]

        df_final = pd.concat([df_existente, pd.DataFrame(nuevas_filas)], ignore_index=True)
        df_final.to_excel(path_salida, index=False)
        print(f"[OK] Se guardaron {len(emisiones_validas)} emisiones en '{path_salida}'")

    return emisiones_validas