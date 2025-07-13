from funciones.emision import buscar_emisiones_por_clave_criterio, cargar_emisiones_desde_csv
from funciones.empresa import obtener_empresas_ordenadas_por_criterio
from funciones.local import obtener_locales_ordenadas_por_criterio
from modelos.emision import Emision
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

def seleccionar_empresa() -> int:
    limpiar_pantalla()
    empresas = obtener_empresas_ordenadas_por_criterio(criterio=lambda e: e.codigo_empresa)

    print("\n{:^10} | {:<25} | {:<11} | {:<12} | {:<15}".format(
        "Código", "Razón Social", "RUC", "Actividad", "Representante"
    ))
    print("-" * 85)

    for e in empresas:
        print("{:^10} | {:<25} | {:<11} | {:<12} | {:<15}".format(
            e.codigo_empresa,
            e.razon_social,
            e.ruc,
            e.codigo_tipo_actividad,
            e.representante_legal
        ))

    empresa_seleccionada = input("\nSeleccione el código de la empresa: ")

    return int(empresa_seleccionada)

def seleccionar_local() -> int:
    limpiar_pantalla()
    locales = obtener_locales_ordenadas_por_criterio(criterio=lambda l: l.codigo_local)

    print("\n{:^10} | {:^10} | {:<30} | {:<15} | {:<15} | {:<20}".format(
        "Cod Local", "Cod Emp", "Nombre Local", "Departamento", "Distrito", "Coordenadas"
    ))
    print("-" * 120)

    for l in locales:
        print("{:^10} | {:^10} | {:<30} | {:<15} | {:<15} | {:<20}".format(
            l.codigo_local,
            l.codigo_empresa,
            l.nombre_local,
            l.departamento,
            l.distrito,
            l.coordenadas
        ))

    local_seleccionado = input("\nSeleccione el código del local: ")

    return int(local_seleccionado)

def seleccionar_emision(codigo_empresa: int, codigo_local: int) -> Emision:
    limpiar_pantalla()
    emisiones = []

    if codigo_empresa != 0:
        emisiones = buscar_emisiones_por_clave_criterio(codigo_empresa, criterio=lambda e: e.codigo_empresa)
    else:
        emisiones = buscar_emisiones_por_clave_criterio(codigo_local, criterio=lambda e: e.codigo_local)

    print("\n{:^5} | {:^10} | {:^10} | {:<30} | {:<15} | {:<25} | {:<8} | {:^10} | {:<12}".format(
        "ID", "Cod Emp", "Cod Loc", "Sustancia", "Cuerpo", "Nombre Receptor", "U.Med", "Cantidad", "Método"
    ))
    print("-" * 150)

    for e in emisiones:
        print("{:^5} | {:^10} | {:^10} | {:<30} | {:<15} | {:<25} | {:<8} | {:^10.2f} | {:<12}".format(
            e.codigo_emision,
            e.codigo_empresa,
            e.codigo_local,
            e.sustancia,
            e.cuerpo_receptor,
            e.nombre_cuerpo_receptor,
            e.unidad_medida,
            e.cantidad,
            e.metodo_calculo
        ))

    while True:
        try:
            emision_seleccionada = int(input("\nSeleccione una emisión: "))
            for e in emisiones:
                if e.codigo_emision == emision_seleccionada:
                    return e
    
            print("La emisión no ha sido encontrada en la lista mostrada.")
        except ValueError:
            print("Por favor, ingrese un valor válido.")


def ver_detalle_emision(emision: Emision):
    limpiar_pantalla()
    print(f"{'Código de Emisión:':<25} {emision.codigo_emision}")
    print(f"{'Código de Empresa:':<25} {emision.codigo_empresa}")
    print(f"{'Código de Localidad:':<25} {emision.codigo_local}")
    print(f"{'Sustancia:':<25} {emision.sustancia}")
    print(f"{'Cuerpo receptor:':<25} {emision.cuerpo_receptor}")
    print(f"{'Nombre receptor:':<25} {emision.nombre_cuerpo_receptor}")
    print(f"{'Unidad de medida:':<25} {emision.unidad_medida}")
    print(f"{'Cantidad:':<25} {emision.cantidad:.2f}")
    print(f"{'Método de cálculo:':<25} {emision.metodo_calculo}")

def validar_informacion(emision: Emision):
    print("\n¿Desea validar esta información como correcta?")
    opcion = input("Si (s) / No (n): ")

    if (opcion == "s"):
        pass
    else:
        input("\nLa emisión no ha sido validada como correcta. Presione enter para continuar...")


def validacion():
    opcion = seleccionar_filtro()

    empresa_seleccionada = 0
    local_seleccionado = 0

    if (opcion == OPCION_EMPRESA):
        empresa_seleccionada = seleccionar_empresa()
    else:
        local_seleccionado = seleccionar_local()

    emision_seleccionada = seleccionar_emision(empresa_seleccionada, local_seleccionado)

    ver_detalle_emision(emision_seleccionada)
    validar_informacion(emision_seleccionada)