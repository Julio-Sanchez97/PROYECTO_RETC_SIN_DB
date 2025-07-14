from funciones.emision import buscar_emisiones_por_clave_criterio, cargar_emisiones_nuevas_desde_excel
from funciones.cuerpo_receptor import obtener_cuerpos_receptores_ordenadas_por_criterio,buscar_cuerpo_receptor_por_clave_criterio
from funciones.sustancia import obtener_sustancias_ordenadas_por_criterio,buscar_sustancia_por_clave_criterio
from funciones.empresa import buscar_empresas_por_clave_criterio
from funciones.local import buscar_locales_por_clave_criterio
from modelos.emision import Emision
from utils.consola import limpiar_pantalla

def seleccionar_emision(codigo_empresa: int, codigo_local: int) -> Emision:
    limpiar_pantalla()
    sustancias = obtener_sustancias_ordenadas_por_criterio(criterio=lambda s: s.codigo_sustancia)
    cuerpos_receptores = obtener_cuerpos_receptores_ordenadas_por_criterio(criterio=lambda c: c.codigo_cuerpo_receptor)
    emisiones = []

    if codigo_empresa != 0:
        emisiones = buscar_emisiones_por_clave_criterio(codigo_empresa, criterio=lambda e: e.codigo_empresa)
    else:
        emisiones = buscar_emisiones_por_clave_criterio(codigo_local, criterio=lambda e: e.codigo_local)

    print("\n{:^5} | {:^10} | {:^10} | {:<30} | {:<25} | {:<25} | {:<8} | {:^10} | {:<12}".format(
        "ID", "Cod Emp", "Cod Loc", "Sustancia", "Cuerpo Receptor", "Nombre Receptor", "U.Med", "Cantidad", "Método"
    ))
    print("-" * 150)

    # Funciones locales para buscar por código en listas
    def get_nombre_sustancia(cod):
        for s in sustancias:
            if s.codigo_sustancia == cod:
                return s.nombre_sustancia
        return "?"

    def get_nombre_cuerpo_receptor(cod):
        for c in cuerpos_receptores:
            if c.codigo_cuerpo_receptor == cod:
                return c.nombre_cuerpo_receptor
        return "?"
    #Ordenar por codigo de emision
    emisiones = sorted(emisiones, key=lambda e: e.codigo_emision)
    for e in emisiones:
        print("{:^5} | {:^10} | {:^10} | {:<30} | {:<25} | {:<25} | {:<8} | {:^10.2f} | {:<12}".format(
            e.codigo_emision,
            e.codigo_empresa,
            e.codigo_local,
            get_nombre_sustancia(e.codigo_sustancia),
            get_nombre_cuerpo_receptor(e.codigo_cuerpo_receptor),
            e.nombre_cuerpo_receptor,
            e.unidad_medida,
            float(e.cantidad),
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
    empresa = buscar_empresas_por_clave_criterio(emision.codigo_empresa, lambda e: e.codigo_empresa)
    local = buscar_locales_por_clave_criterio(emision.codigo_local, lambda l: l.codigo_local)
    sustancia = buscar_sustancia_por_clave_criterio(emision.codigo_sustancia, lambda s: s.codigo_sustancia)
    cuerpo_receptor = buscar_cuerpo_receptor_por_clave_criterio(emision.codigo_cuerpo_receptor, lambda c: c.codigo_cuerpo_receptor)

    print(f"{'Código de Emisión:':<25} {emision.codigo_emision}")
    print(f"{'Código de Empresa:':<25} {empresa[0].razon_social}")
    print(f"{'Código de Localidad:':<25} {local[0].nombre_local}")
    print(f"{'Sustancia:':<25} {sustancia[0].nombre_sustancia}")
    print(f"{'Cuerpo receptor:':<25} {cuerpo_receptor[0].nombre_cuerpo_receptor}")
    print(f"{'Nombre receptor:':<25} {emision.nombre_cuerpo_receptor}")
    print(f"{'Unidad de medida:':<25} {emision.unidad_medida}")
    print(f"{'Cantidad:':<25} {emision.cantidad:.2f}")
    print(f"{'Método de cálculo:':<25} {emision.metodo_calculo}")


def cargar_emisiones():
    limpiar_pantalla()
    Emision.inicializar_contador_desde_excel()
    nuevas = cargar_emisiones_nuevas_desde_excel()
    if nuevas:
        print(f"\n✅ Se cargaron {len(nuevas)} emisiones nuevas:\n")
        print("{:^5} | {:^10} | {:^10} | {:<30} | {:<15} | {:<25} | {:<8} | {:^10} | {:<12}".format(
            "ID", "Cod Emp", "Cod Loc", "Sustancia", "Cuerpo", "Nombre Receptor", "U.Med", "Cantidad", "Método"
        ))
        print("-" * 150)
        for e in nuevas:
            print("{:^5} | {:^10} | {:^10} | {:<30} | {:<15} | {:<25} | {:<8} | {:^10.2f} | {:<12}".format(
                e.codigo_emision,
                e.codigo_empresa,
                e.codigo_local,
                e.codigo_sustancia,
                e.codigo_cuerpo_receptor,
                e.nombre_cuerpo_receptor,
                e.unidad_medida,
                e.cantidad,
                e.metodo_calculo
            ))
    else:
        print("⚠️  No se cargaron emisiones.")
    input("\nPresione ENTER para continuar...")

def emisiones():
    while True:
        limpiar_pantalla()
        print("=== MÓDULO DE EMISIONES ===")
        print("1. Cargar emisiones desde Excel")
        print("2. Salir al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_emisiones()
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")
            input("Presione ENTER para continuar...")