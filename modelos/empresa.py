class Empresa:
    def __init__(
        self,
        codigo_empresa: int,
        razon_social: str,
        ruc: str,
        codigo_actividad_ciiu: int,
        actividad: str,
        representante_legal: str,
        correo_electronico: str,
        telefono: str,
    ):
        self.codigo_empresa = codigo_empresa
        self.razon_social = razon_social
        self.ruc = ruc
        self.codigo_actividad_ciiu = codigo_actividad_ciiu
        self.actividad = actividad
        self.representante_legal = representante_legal
        self.correo_electronico = correo_electronico
        self.telefono = telefono