class Emision:
    def __init__(
        self,
        codigo_emision: int,
        codigo_empresa: int,
        codigo_local: int,
        cuerpo_receptor: str,
        nombre_cuerpo_receptor: str,
        cantidad: float,
        unidad_medida: str,
        sustancia: str,
        metodo_calculo: str
    ):
        self.codigo_emision = codigo_emision
        self.codigo_empresa = codigo_empresa
        self.codigo_local = codigo_local
        self.cuerpo_receptor = cuerpo_receptor
        self.nombre_cuerpo_receptor = nombre_cuerpo_receptor
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
        self.sustancia = sustancia
        self.metodo_calculo = metodo_calculo
