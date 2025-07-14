from funciones.reporte import buscar_reportes_por_clave_criterio, obtener_reportes_ordenadas_por_criterio
from utils.consola import limpiar_pantalla

def filtro_por_codigo(label: str, attr_lambda) -> list:
    try:
        clave = int(input(f"Ingrese código de {label}: "))
        return buscar_reportes_por_clave_criterio(clave, attr_lambda)
    except ValueError:
        print("Código inválido.")
        input("Presione Enter para continuar...")
        return []
        
def seleccionar_criterio_ordenamiento():
    print("\nOrdenar por:")
    print("1. Código de emisión")
    print("2. Nombre de empresa")
    print("3. Nombre de local")
    print("4. CIIU")
    print("5. Cantidad")
    print("6. Sustancia")
    opcion = input("Seleccione el campo de ordenamiento: ")

    return {
        "1": lambda r: r.codigo_emision,
        "2": lambda r: r.nombre_empresa.lower(),
        "3": lambda r: r.nombre_local.lower(),
        "4": lambda r: r.descripcion_ciiu.lower(),
        "5": lambda r: r.cantidad,
        "6": lambda r: r.sustancia
    }.get(opcion, lambda r: r.codigo_emision)

def seleccionar_opcion_menu():
    print("\nOpciones:")
    print("1. Cambiar ordenamiento")
    print("2. Buscar por código de empresa")
    print("3. Buscar por código de local")
    print("4. Buscar por código de CIIU")
    print("5. Restablecer listado original")
    print("6. Salir")

    return input("\nSeleccione una opción: ")

def mostrar_reportes(reportes: list):
    limpiar_pantalla()
    print("\n{:<20} | {:<25} | {:<65} | {:^10} | {:<15} | {:^10} | {:^10} | {:<10} | {:<15}".format(
        "Nombre Empresa", "Nombre Local", "Descripción CIIU", "Cuerpo", "Nombre Cuerpo", "Cantidad", "Unidad", "Sustancia", "Método"
    ))
    print("-" * 200)

    for r in reportes:
        print("{:<20} | {:<25} | {:<65} | {:^10} | {:<15} | {:^10.2f} | {:<10} | {:<10} | {:<15}".format(
            r.nombre_empresa,
            r.nombre_local,
            r.descripcion_ciiu,
            r.cuerpo_receptor,
            r.nombre_cuerpo_receptor or "-",
            r.cantidad,
            r.unidad_medida or "-",
            r.sustancia,
            r.metodo_calculo
        ))

def reporte():
    criterio_por_default = lambda r: r.codigo_emision
    criterio = criterio_por_default
    descendente = False

    reportes = obtener_reportes_ordenadas_por_criterio(criterio, descendente)

    while True:
        limpiar_pantalla()
        mostrar_reportes(reportes)

        opcion = seleccionar_opcion_menu()

        if opcion == "1":
            criterio = seleccionar_criterio_ordenamiento()
            descendente = input("¿Orden descendente? (s/n): ").lower() == "s"
            reportes = obtener_reportes_ordenadas_por_criterio(criterio, descendente)

        elif opcion == "2":
            resultado = filtro_por_codigo("empresa", lambda r: r.codigo_empresa)
            if resultado:
                reportes = resultado

        elif opcion == "3":
            resultado = filtro_por_codigo("local", lambda r: r.codigo_local)
            if resultado:
                reportes = resultado

        elif opcion == "4":
            resultado = filtro_por_codigo("ciiu", lambda r: r.codigo_ciiu)
            if resultado:
                reportes = resultado

        elif opcion == "5":
            reportes = obtener_reportes_ordenadas_por_criterio(criterio_por_default)

        elif opcion == "6":
            break

        else:
            input("Opción inválida. Presione Enter para continuar...")