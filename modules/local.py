from funciones.local import buscar_locales_por_clave_criterio, generar_codigo_local, obtener_locales_ordenadas_por_criterio, registrar_local
from modelos.local import Local
from modules.empresa import seleccionar_empresa
from utils.consola import limpiar_pantalla

def seleccionar_local() -> Local:
    limpiar_pantalla()
    locales = obtener_locales_ordenadas_por_criterio(criterio=lambda l: l.codigo_local)

    print("\n{:^10} | {:^10} | {:<30} | {:<15} | {:<15}".format(
        "Cod Local", "Cod Emp", "Nombre Local", "Departamento", "Distrito"
    ))
    print("-" * 120)

    for l in locales:
        print("{:^10} | {:^10} | {:<30} | {:<15} | {:<15}".format(
            l.codigo_local,
            l.codigo_empresa,
            l.nombre_local,
            l.departamento,
            l.distrito
        ))

    while True:
        try:
            empresa_seleccionado = int(input("\nSeleccione el código del local: "))
            resultado = buscar_locales_por_clave_criterio(empresa_seleccionado, lambda c: c.codigo_local, locales)
            
            if not resultado:
                print("El código no ha sido encontrado. Intente nuevamente.")
            else:
                return resultado[0]
        except ValueError:
            print("Por favor, ingrese un valor válido.")

def local():
    empresa = seleccionar_empresa()

    limpiar_pantalla()

    nombre_local = input("Ingrese el nombre: ")
    departamento = input("Ingrese el departamento: ")
    ciudad = input("Ingrese la ciudad: ")
    distrito = input("Ingrese el distrito: ")
    coordenadas_x = input("Ingrese las coordenadas x: ")
    coordenadas_y = input("Ingrese las coordenadas y: ")

    codigo_local = generar_codigo_local()

    local = Local(
        codigo_local=codigo_local,
        codigo_empresa=empresa.codigo_empresa,
        nombre_local=nombre_local,
        departamento=departamento,
        ciudad=ciudad,
        distrito=distrito,
        coordenadas_x=coordenadas_x,
        coordenadas_y=coordenadas_y,
    )

    registrar_local(local)

    input("\nEl local ha sido registrado exitosamente. Presione enter para continuar...")