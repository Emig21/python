def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def salir():
    valor = input("Presione S para ingresar otro número, N para salir: ").strip().upper()
    if valor == "S":
        return 1
    elif valor == "N":
        return 0
    else:
        print("Presionó otra tecla, se cerrará el programa.")
        return 0
    
variable = 1
while variable == 1:
    try:
        n = int(input("Ingrese el valor para calcular el Fibonacci: "))
        fib(n)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
    variable = salir()
