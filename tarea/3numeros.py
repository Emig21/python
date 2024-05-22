print("Ingrese los 3 numeros")

def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero != 0:
                return numero
            else:
                print("El número no puede ser cero. Por favor, ingrese un número válido.")
        except ValueError:
            print("Ingrese un número, letras no son válidas.")

a = solicitar_numero("Ingrese primer numero: ")
b = solicitar_numero("Ingrese segundo numero: ")
c = solicitar_numero("Ingrese tercer numero: ")

if a < 0:
    r = a * b * c
else:
    r = a + b + c

print(r)
