class Emision:
    def __init__(
        self,
        codigo_emision: int,
        codigo_empresa: int,
        codigo_local: int,
        sustancia: str,
        cuerpo_receptor: str,
        nombre_cuerpo_receptor: str,
        unidad_medida: str,
        cantidad: float,
        metodo_calculo: str
    ):
        self.codigo_emision = codigo_emision
        self.codigo_empresa = codigo_empresa
        self.codigo_local = codigo_local
        self.sustancia = sustancia
        self.cuerpo_receptor = cuerpo_receptor
        self.nombre_cuerpo_receptor = nombre_cuerpo_receptor
        self.unidad_medida = unidad_medida
        self.cantidad = cantidad
        self.metodo_calculo = metodo_calculo
