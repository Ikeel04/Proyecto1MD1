def complemento(universal_set, conjunto):
    return universal_set - conjunto

def union(conjunto1, conjunto2):
    return conjunto1 | conjunto2


def interseccion(conjunto1, conjunto2):
    # Devuelve un conjunto con los elementos que están en ambos conjuntos
    interseccion = set()
    for elemento in conjunto1:
        if elemento in conjunto2:
            interseccion.add(elemento)
    return interseccion


def diferencia(conjunto1, conjunto2):
    # Devuelve un conjunto con los elementos que están en el conjunto1 pero no en el conjunto2
    diferencia = set()
    for elemento in conjunto1:
        if elemento not in conjunto2:
            diferencia.add(elemento)
    return diferencia


def diferencia_simetrica(conjunto1, conjunto2):
    # Devuelve un conjunto con los elementos que están en conjunto1 o conjunto2 pero no en ambos
    diferencia_simetrica = set()
    for elemento in union(conjunto1, conjunto2):
        if elemento in conjunto1 and elemento not in conjunto2:
            diferencia_simetrica.add(elemento)
        elif elemento in conjunto2 and elemento not in conjunto1:
            diferencia_simetrica.add(elemento)
    return diferencia_simetrica


def construir_conjunto():
    while True:
        try:
            elementos = input("Ingrese los elementos del conjunto (letras A-Z, dígitos 0-9), sin espacios: ").upper()
            if any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for c in elementos):
                raise ValueError("Los elementos deben ser letras A-Z o dígitos 0-9.")
            return set(elementos)
        except ValueError as e:
            print(f"Entrada no válida: {e}. Intente de nuevo.")


def menu():
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
            print("Conjunto 1:")
            conjunto1 = construir_conjunto()
            print(f"Conjunto 1: {conjunto1}")

            print("Conjunto 2:")
            conjunto2 = construir_conjunto()
            print(f"Conjunto 2: {conjunto2}")

        elif opcion == "2":
            if not conjunto1 or not conjunto2:
                print("Primero debe crear ambos conjuntos.")
                continue

            print("\nOperar conjuntos:")
            print("1. Complemento del conjunto 1")
            print("2. Unión de conjuntos")
            print("3. Intersección de conjuntos")
            print("4. Diferencia de conjuntos (Conjunto 1 - Conjunto 2)")
            print("5. Diferencia Simétrica de conjuntos")

            operacion = input("Seleccione una operación (1, 2, 3, 4, 5): ")

            if operacion == "1":
                print(f"Complemento del conjunto 1: {complemento(universal_set, conjunto1)}")
            elif operacion == "2":
                print(f"Unión: {union(conjunto1, conjunto2)}")
            elif operacion == "3":
                print(f"Intersección: {interseccion(conjunto1, conjunto2)}")
            elif operacion == "4":
                print(f"Diferencia (Conjunto 1 - Conjunto 2): {diferencia(conjunto1, conjunto2)}")
            elif operacion == "5":
                print(f"Diferencia Simétrica: {diferencia_simetrica(conjunto1, conjunto2)}")
            else:
                print("Operación no válida. Intente de nuevo.")

        elif opcion == "3":
            print("Finalizando el programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()