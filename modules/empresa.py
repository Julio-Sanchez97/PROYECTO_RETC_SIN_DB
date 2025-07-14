from funciones.ciiu import buscar_ciius_por_clave_criterio, obtener_ciius_ordenadas_por_criterio
from funciones.empresa import buscar_empresas_por_clave_criterio, generar_codigo_empresa, obtener_empresas_ordenadas_por_criterio, registrar_empresa
from modelos.ciiu import Ciiu
from modelos.empresa import Empresa
from utils.consola import limpiar_pantalla

def seleccionar_empresa() -> Empresa:
    limpiar_pantalla()
    empresas = obtener_empresas_ordenadas_por_criterio(criterio=lambda e: e.codigo_empresa)

    print("\n{:^10} | {:<25} | {:<11} | {:<75} | {:<15}".format(
        "Código", "Razón Social", "RUC", "Actividad", "Representante"
    ))
    print("-" * 150)

    for e in empresas:
        print("{:^10} | {:<25} | {:<11} | {:<75} | {:<15}".format(
            e.codigo_empresa,
            e.razon_social,
            e.ruc,
            e.actividad,
            e.representante_legal
        ))

    while True:
        try:
            empresa_seleccionado = int(input("\nSeleccione el código de la empresa: "))
            resultado = buscar_empresas_por_clave_criterio(empresa_seleccionado, lambda c: c.codigo_empresa, empresas)
            
            if not resultado:
                print("El código no ha sido encontrado. Intente nuevamente.")
            else:
                return resultado[0]
        except ValueError:
            print("Por favor, ingrese un valor válido.")

def seleccionar_ciiu() -> Ciiu:
    limpiar_pantalla()
    ciius = obtener_ciius_ordenadas_por_criterio(criterio=lambda c: c.codigo_ciiu)

    print("\n{:^10} | {:<60}".format("Código", "Descripción"))
    print("-" * 75)

    for c in ciius:
        print("{:^10} | {:<60}".format(c.codigo_ciiu, c.descripcion))

    while True:
        try:
            ciiu_seleccionado = int(input("\nSeleccione el código del ciiu: "))
            resultado = buscar_ciius_por_clave_criterio(ciiu_seleccionado, lambda c: c.codigo_ciiu, ciius)
            
            if not resultado:
                print("El código no ha sido encontrado. Intente nuevamente.")
            else:
                return resultado[0]
        except ValueError:
            print("Por favor, ingrese un valor válido.")

def empresa():
    limpiar_pantalla()

    ruc = ""
    
    while True:
        ruc = input("Ingrese el RUC: ")
        empresa_encontrada = buscar_empresas_por_clave_criterio(ruc, lambda e: e.ruc)

        if empresa_encontrada:
            print("La empresa ya ha sido registrada. Intente con otro RUC.\n")
        else:
            break

    razon_social = input("\nIngrese la razón social: ")
    ciiu = seleccionar_ciiu()
    
    representante_legal = input("\nIngrese al representante legal: ")
    correo_electronico = input("\nIngrese el correo electrónico: ")
    telefono = input("\nIngrese el teléfono: ")
    codigo_empresa = generar_codigo_empresa()

    empresa = Empresa(
        codigo_empresa=codigo_empresa,
        razon_social=razon_social,
        ruc=ruc,
        codigo_actividad_ciiu=ciiu.codigo_ciiu,
        actividad=ciiu.descripcion,
        representante_legal=representante_legal,
        correo_electronico=correo_electronico,
        telefono=telefono
    )

    registrar_empresa(empresa)

    input("La empresa ha sido registrada exitosamente. Presione enter para continuar...")

    
