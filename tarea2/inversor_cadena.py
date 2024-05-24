def invertir_cadena_recursiva(cadena_original):
    if len(cadena_original) == 0:
        return cadena_original
    else:
        return cadena_original[-1] + invertir_cadena_recursiva(cadena_original[:-1])


def obtener_cadena_valida():
    while True:
        cadena_ingresada = input("Ingresa una cadena: ")
        if cadena_ingresada.strip() == "":
            print("La cadena no puede estar vacía. Inténtalo de nuevo.")
        else:
            return cadena_ingresada

def main():
    cadena_valida = obtener_cadena_valida()
    cadena_invertida = invertir_cadena_recursiva(cadena_valida)
    print(f"La cadena invertida es: {cadena_invertida}")

if __name__ == "__main__":
    main()
