# creamos las funciones de las cuatro operaciones básicas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

#recordar que al dividir un número no se puede dividir entre 0
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero [0]"

def calculadora():
    while True:

        print("!Bienvenido a la calculadora!")
        print("Seleccione la operación que dese calcular:")
        print("Presione [1] si desea sumar")
        print("Presione [2] si sea restar")
        print("Presione [3] si desea multiplicar")
        print("Presione [4] si desea divir")

        operacion = input("Ingresa el número de la operación:  ")
        

        try:
            num1 = float(input("Ingresa primer número: "))
            num2 = float(input("Ingresa segundo número: "))
        except ValueError:
            print("Error: Por favor ingresa un número válido.")
            continue

        if operacion == '1':
            print(f"Resultado de la suma es : {sumar(num1, num2)}")
        elif operacion == '2':
            print(f"Resultado de la resta es : {restar(num1, num2)}")
        elif operacion == '3':
            print(f"Resultado de la multiplicación es : {multiplicar(num1, num2)}")
        elif operacion == '4':
            print(f"Resultado de la divición es : {dividir(num1, num2)}")
        else:
            print("Operación no válida. Seleccione una operación correcta")
            continue

        continuar = input("¿Deseas realizar otra operación? [S] si es si, [N] si es no: ").lower()
        if continuar == 'n':
            print("Presione cualquier tecla para cerrar el programa.")
            input()
            break

if __name__ == "__main__":
    calculadora()
