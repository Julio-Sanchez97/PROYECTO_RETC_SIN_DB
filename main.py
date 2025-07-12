# Importamos las funciones de los modulos
from modules.empresa import empresa
from modules.local import local
from modules.emisiones import emisiones
from modules.validacion import validacion
from modules.reporte import reporte


def main():
    while True:
        print("\nPrograma Registro de Emisiones y Transferencia de Contaminantes - MINAM")
        print("************************************************************************")
        print("1. MÓDULO DE REGISTRO DE EMPRESA")
        print("2. MÓDULO DE REGISTRO DE LOCAL")
        print("3. MÓDULO DE REGISTRO DE EMISIONES")
        print("4. MÓDULO DE VALIDACIÓN DE CALCULOS")
        print("5. MÓDULO DE VALIDACIÓN DE REPORTES")
        print("6. SALIR DEL PROGRAMA")
        print("************************************************************************")
        numero_modulo = input("Ingrese el número del módulo a visualizar: ")
        
        match numero_modulo:
            case "1":
                empresa()
            case "2":
                local()
            case "3":
                emisiones()
            case "4":
                validacion()
            case "5":
                reporte()
            case "6":
                print("Saliendo del programa")
                break
            case _:
                print("Opción no válida")
            
if __name__ == "__main__":
    main()