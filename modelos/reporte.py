class Reporte:
    def __init__(
        self,
        codigo_emision: int,
        codigo_empresa: int,
        nombre_empresa: str,
        codigo_local: int,
        nombre_localidad: str,
        sustancia: str,
        cuerpo_receptor: str,
        nombre_cuerpo_receptor: str,
        unidad_medida: str,
        cantidad: float,
        metodo_calculo: str
    ):
        self.codigo_emision = codigo_emision
        self.codigo_empresa = codigo_empresa
        self.nombre_empresa = nombre_empresa
        self.codigo_local = codigo_local
        self.nombre_localidad = nombre_localidad
        self.sustancia = sustancia
        self.cuerpo_receptor = cuerpo_receptor
        self.nombre_cuerpo_receptor = nombre_cuerpo_receptor
        self.unidad_medida = unidad_medida
        self.cantidad = cantidad
        self.metodo_calculo = metodo_calculo
