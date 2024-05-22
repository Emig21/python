
while True:
    try:
        tiempo = float(input("Ingrese el tiempo en segundos: "))
        if tiempo == 0:
            print("Cero no es número")
        else:
            break
    except ValueError:
        print("ingrese un número")


while True:
    try:
        distancia = float(input("Ingrese la distancia en metros: "))
        break
    except ValueError:
        print("Ingrese un número")


velocidad = distancia / tiempo

print("La velocidad es:", velocidad, "m/s")

