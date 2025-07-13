import pandas as pd  #libereria para manejar excel

# Diccionario global donde se almacenaran los datos de las empresas
datos_empresas = {
    "Razon social": [],
    "RUC": [],
    "Codigo actividad CIIU": [],
    "Representante legal": [],
    "Correo electronico": [],
    "Telefono": []
}

# Funcion para cargar datos desde un archivo Excel al diccionario
def cargar_datos_desde_excel(nombre_archivo):
    try:
        # Leer el Excel y forzar que la columna RUC se lea como texto
        df = pd.read_excel(nombre_archivo, dtype={"RUC": str})

        # Mostrar las columnas encontradas para depuracion
        print("Columnas encontradas:", df.columns.tolist())

        # Copiar los datos del DataFrame al diccionario
        for columna in datos_empresas:
            datos_empresas[columna] = df[columna].astype(str).tolist()  # Convertimos todo a texto

        print("Datos cargados correctamente del Excel.\n")
    except Exception as e:
        print("Error al cargar archivo:", e)

# Menu principal
def mostrar_menu():
    print("\n=== Menu Principal ===")
    print("1. Registrar Empresa")
    print("2. Registrar Local")
    print("3. Registrar Emisiones")
    print("4. Validar calculo de sustancias")
    print("5. Salir del programa")

# Funcion de busqueda binaria
def busqueda_binaria(lista_rucs, ruc_buscado):
    izquierda = 0
    derecha = len(lista_rucs) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_rucs[medio] == ruc_buscado:
            return medio
        elif lista_rucs[medio] < ruc_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado

# Funcion para registrar nueva empresa
def registrar_empresa():
    print("\n--- Registrar Empresa ---")
    ruc_nuevo = input("Ingrese el RUC de la empresa: ").strip()

    # Crear lista de tuplas y ordenarla por RUC
    datos_ordenados = sorted(zip(
        datos_empresas["RUC"],
        datos_empresas["Razon social"],
        datos_empresas["Codigo actividad CIIU"],
        datos_empresas["Representante legal"],
        datos_empresas["Correo electronico"],
        datos_empresas["Telefono"]
    ), key=lambda x: x[0])  # Ordenar por RUC

    # Obtener solo la lista de RUCs como texto
    rucs_ordenados = [str(r[0]) for r in datos_ordenados]

    # Buscar si el RUC ya existe
    posicion = busqueda_binaria(rucs_ordenados, ruc_nuevo)

    if posicion != -1:
        print("La empresa con ese RUC ya esta¡ registrada:")
        print("Razon Social:", datos_ordenados[posicion][1])
    else:
        # Si no existe, registrar nueva empresa
        razon = input("Ingrese la razon social: ")
        ciiu = input("Ingrese el codigo actividad CIIU: ")
        rep = input("Ingrese el representante legal: ")
        correo = input("Ingrese el correo electronico: ")
        telefono = input("Ingrese el telefono: ")

        # Agregar los datos al diccionario
        datos_empresas["RUC"].append(ruc_nuevo)
        datos_empresas["Razon social"].append(razon)
        datos_empresas["Codigo actividad CIIU"].append(ciiu)
        datos_empresas["Representante legal"].append(rep)
        datos_empresas["Correo electronico"].append(correo)
        datos_empresas["Telefono"].append(telefono)

        print("Empresa registrada correctamente.\n")

# Funcion principal que controla el menu
def main():
    archivo = "registro de datos UPC.xlsx"  # Nombre exacto del archivo
    cargar_datos_desde_excel(archivo)  # Carga inicial de datos

    while True:
        mostrar_menu()
        opcion = input("Seleccione el numero del modulo: ")

        if opcion == "1":
            registrar_empresa()
        elif opcion == "2":
            print("\nFuncion 'Registrar Local' en desarrollo.\n")
        elif opcion == "3":
            print("\nFuncion 'Registrar Emisiones' en desarrollo.\n")
        elif opcion == "4":
            print("\nFuncion 'Validar calculo de sustancias' en desarrollo.\n")
        elif opcion == "5":
            print("\nSaliendo del programa. ¡Hasta luego!\n")
            break
        else:
            print("\nOpcion invalida. Intente nuevamente.\n")

# Ejecutar el programa
main()
