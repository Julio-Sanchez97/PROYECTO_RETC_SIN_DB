from funciones.emision import buscar_emisiones_por_clave_criterio
from funciones.reporte import buscar_reportes_por_clave_criterio
from modelos.emision import Emision
from utils.consola import limpiar_pantalla

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
            codigo_emision = int(input("\nSeleccione una emisión: "))
            emision_encontrada = None

            for e in emisiones:
                if e.codigo_emision == codigo_emision:
                    emision_encontrada = e
                    break
    
            if not emision_encontrada:
                print("La emisión no ha sido encontrada en la lista mostrada.")
                continue

            reportes = buscar_reportes_por_clave_criterio(emision_encontrada.codigo_emision, lambda e: e.codigo_emision)

            if reportes:
                print("La emisión ya fue validada como correcta, por favor seleccione otra.")
                continue

            return emision_encontrada
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

def emisiones():
    print("Ingrese al modulo de emisiones")