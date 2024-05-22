print(".................................")
print("     PROMEDIO DE N CANTIDAD      ")
print("           DE NUMEROS            ")
print(".................................")
print("------------------------------------------")

cantidad = int(input ("Indique la cantidad de números a promediar"))
print("------------------------------------------")

numeros=[]

for i in range(cantidad):
    while True:
        try:
            numero = float(input(f"Ingrese número{ i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Numero no valid, Ingrese un número valido")

suma = sum (numeros)

promedio = suma / cantidad 
print("-------------------------------------------------------")
print("El promedio de la suma de N cantidad de números es: ", promedio)
print("-------------------------------------------------------")