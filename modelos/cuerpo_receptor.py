class CuerpoReceptor:
    def __init__(
        self,
        codigo_cuerpo_receptor: int,
        nombre_cuerpo_receptor: str,
        codigo_tipo: str,
    ):
        if codigo_tipo not in ("E", "T"):
            raise ValueError("codigo_tipo debe ser 'E' o 'T'")
        
        self.codigo_cuerpo_receptor = codigo_cuerpo_receptor
        self.nombre_cuerpo_receptor = nombre_cuerpo_receptor
        self.codigo_tipo = codigo_tipo
