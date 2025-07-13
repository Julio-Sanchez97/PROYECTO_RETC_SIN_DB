class Local:
    def __init__(
        self,
        codigo_local: int,
        codigo_empresa: int,
        nombre_local: str,
        departamento: str,
        ciudad: str,
        distrito: str,
        coordenadas: str,
    ):
        self.codigo_local = codigo_local
        self.codigo_empresa = codigo_empresa
        self.nombre_local = nombre_local
        self.departamento = departamento
        self.ciudad = ciudad
        self.distrito = distrito
        self.coordenadas = coordenadas