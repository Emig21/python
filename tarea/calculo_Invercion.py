# Inicio del programa
def calcular_inversion():
    while True:
        # Entrada de datos
        C = float(input("Indique el capital inicial: "))
        I = float(input("Ingrese la tasa de interés (%): "))
        M = int(input("Ingrese el tiempo (en años): "))
        
        # Verificar condiciones
        if C > 0 and 0 < I <= 100 and M > 0:
            break
        else:
            print("Introduce capital, interés y tiempo apropiados.")
    
    # Calcular la inversión con interés compuesto
    for J in range(1, M + 1):
        C = C * (1 + I / 100)
    
    # Mostrar el resultado final
    print(f"Tienes: {C} dólares")
    
# Fin del programa
calcular_inversion()
