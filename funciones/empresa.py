from modelos.empresa import Empresa
from utils.algoritmos import busqueda_binaria, quicksort

def cargar_empresas_desde_csv() -> list:
    empresas = []
    with open("documents/empresas.csv", "r", encoding="utf-8") as f:
        for linea in f:
            campos = linea.strip().split(",")
            empresa = Empresa(
                codigo_empresa=int(campos[0]),
                razon_social=campos[1],
                ruc=campos[2],
                codigo_actividad_ciiu=int(campos[3]),
                codigo_tipo_actividad=campos[4],
                representante_legal=campos[5],
                correo_electronico=campos[6],
                telefono=campos[7]
            )
            empresas.append(empresa)
    return empresas

def obtener_empresas_ordenadas_por_criterio(criterio) -> list:
    empresas = cargar_empresas_desde_csv()
    empresas = quicksort(empresas, criterio)

    return empresas

def buscar_empresas_por_clave_criterio(clave, criterio) -> list:
    empresas = obtener_empresas_ordenadas_por_criterio(criterio)
    empresas = busqueda_binaria(empresas, clave, criterio)

    return empresas