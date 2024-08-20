# Funciones para las operaciones de conjuntos

def complemento(universal_set, conjunto):
    return universal_set - conjunto

def union(conjunto1, conjunto2):
    return conjunto1 | conjunto2

def interseccion(conjunto1, conjunto2):
    return conjunto1 & conjunto2

def diferencia(conjunto1, conjunto2):
    return conjunto1 - conjunto2

def diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1 ^ conjunto2

# Función para construir un conjunto a partir de la entrada del usuario
def construir_conjunto():
    elementos = input("Ingrese los elementos del conjunto (letras A-Z, dígitos 0-9), sin espacios: ").upper()
    conjunto = set(elementos)
    return conjunto

# Función principal para ejecutar el programa
def menu():
    # Conjunto universal (A-Z y 0-9)
    universal_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    conjunto1 = set()
    conjunto2 = set()

    while True:
        print("\nMenú Principal:")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Finalizar")
        
        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == "1":

        elif opcion == "2":

        elif opcion == "3":

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()