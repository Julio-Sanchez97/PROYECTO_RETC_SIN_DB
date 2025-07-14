import pandas as pd

class Emision:
    _contador_emisiones = 1  # Valor por defecto si el archivo no existe o está vacío

    @classmethod
    def inicializar_contador_desde_excel(cls):
        try:
            df = pd.read_excel("documents/emisiones_generadas.xlsx")
            if not df.empty and 'COD_EMISION' in df.columns:
                cls._contador_emisiones = df['COD_EMISION'].max() + 1
                print(f"Contador de emisiones iniciado en {cls._contador_emisiones}")
            else:
                print("Excel vacío o sin columna 'COD_EMISION', contador inicia en 1.")
        except Exception as e:
            print(f"[ERROR] No se pudo leer el archivo: {e}")

    def __init__(
        self,
        codigo_empresa: int,
        codigo_local: int,
        codigo_sustancia: int,
        codigo_cuerpo_receptor: int,
        nombre_cuerpo_receptor: str,
        unidad_medida: str,
        cantidad: float,
        metodo_calculo: str
    ):
        self.codigo_emision = Emision._contador_emisiones
        Emision._contador_emisiones += 1

        self.codigo_empresa = codigo_empresa
        self.codigo_local = codigo_local
        self.codigo_sustancia = codigo_sustancia
        self.codigo_cuerpo_receptor = codigo_cuerpo_receptor
        self.nombre_cuerpo_receptor = nombre_cuerpo_receptor
        self.unidad_medida = unidad_medida
        self.cantidad = cantidad
        self.metodo_calculo = metodo_calculo