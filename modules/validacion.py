from funciones.empresa import buscar_empresas_por_clave_criterio
from funciones.local import buscar_locales_por_clave_criterio
from funciones.reporte import registrar_reporte
from modelos.emision import Emision
from modelos.reporte import Reporte
from modules.emisiones import seleccionar_emision, ver_detalle_emision
from modules.empresa import seleccionar_empresa
from modules.local import seleccionar_local
from utils.consola import limpiar_pantalla

OPCION_EMPRESA = 1
OPCION_LOCAL = 2

def seleccionar_filtro() -> int:
    limpiar_pantalla()
    print("¿Desea buscar por código de empresa o local?")
    print("\n1. Empresa")
    print("2. Local")

    opcion = input("\nSeleccione una opcion: ")

    return int(opcion)

def validar_informacion(emision: Emision):
    print("\n¿Desea validar esta información como correcta?")
    opcion = input("Si (s) / No (n): ")

    if (opcion == "s"):
        
        empresas = buscar_empresas_por_clave_criterio(emision.codigo_empresa, lambda e: e.codigo_empresa)
        locales = buscar_locales_por_clave_criterio(emision.codigo_local, lambda l: l.codigo_local)

        reporte = Reporte(
            codigo_emision=emision.codigo_emision,
            codigo_empresa=empresas[0].codigo_empresa,
            nombre_empresa=empresas[0].razon_social,
            codigo_local=locales[0].codigo_local,
            nombre_local=locales[0].nombre_local,
            codigo_ciiu=empresas[0].codigo_actividad_ciiu,
            descripcion_ciiu=empresas[0].actividad,
            cuerpo_receptor=emision.cuerpo_receptor,
            nombre_cuerpo_receptor=emision.nombre_cuerpo_receptor,
            cantidad=emision.cantidad,
            unidad_medida=emision.unidad_medida,
            sustancia=emision.sustancia,
            metodo_calculo=emision.metodo_calculo
        )

        registrar_reporte(reporte)
        input("La emisión ha sido validada exitosamente. Presione enter para continuar...")
    else:
        input("\nLa emisión no ha sido validada como correcta. Presione enter para continuar...")

def validacion():
    opcion = seleccionar_filtro()

    codigo_empresa = 0
    codigo_local = 0

    if (opcion == OPCION_EMPRESA):
        empresa = seleccionar_empresa()
        codigo_empresa = empresa.codigo_empresa
    else:
        local = seleccionar_local()
        codigo_local = local.codigo_local

    emision_seleccionada = seleccionar_emision(codigo_empresa, codigo_local)

    ver_detalle_emision(emision_seleccionada)
    validar_informacion(emision_seleccionada)