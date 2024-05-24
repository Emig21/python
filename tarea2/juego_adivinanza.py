import time

def generar_numero_aleatorio():
    
    semilla = int(time.time())
    
    semilla = (semilla * 1103515245 + 12345) & 0x7fffffff
    
    numero_aleatorio = (semilla % 10) + 1
    return numero_aleatorio

def juego_de_adivinanza():
    numero_secreto = generar_numero_aleatorio()
    intentos = 0
    
    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 10. ¡Adivina cuál es!")
    
    while True:
        intento = input("Ingresa un número (o 'salir' para terminar el juego): ")
        
        if intento.lower() == 'salir':
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break
        
        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        intentos += 1
        
        if intento < 1 or intento > 10:
            print("El número debe estar entre 1 y 10.")
        elif intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! ¡El numero era {numero_secreto} ╰(*°▽°*)╯!")
            print(f"¡Has adivinado el número en {intentos} intentos!")
            break

juego_de_adivinanza()
