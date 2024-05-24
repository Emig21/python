def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

def obtener_numero_valido():
    while True:
        try:
            numero_ingresado = int(input("Ingresa un número entero no negativo: "))
            if numero_ingresado < 0:
                print("El número no puede ser negativo. Inténtalo de nuevo.")
            else:
                return numero_ingresado
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def main():
    numero_valido = obtener_numero_valido()
    factorial = calcular_factorial(numero_valido)
    print(f"El factorial de {numero_valido} es {factorial}")

if __name__ == "__main__":
    main()
