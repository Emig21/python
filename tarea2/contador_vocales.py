def contar_vocales_con_y_sin_tilde(frase):
    vocales_con_tilde = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    contador_con_tilde = 0
    contador_sin_tilde = 0
    
    for caracter in frase:
        if caracter in vocales_con_tilde:
            vocal_sin_tilde = vocales_con_tilde[caracter]
            contador_con_tilde += 1
            contador_sin_tilde += 1
        elif caracter.lower() in 'aeiou':
            contador_sin_tilde += 1
    
    return contador_con_tilde, contador_sin_tilde

def obtener_frase_valida():
    while True:
        frase_ingresada = input("Ingresa una frase: ")
        if frase_ingresada.strip() == "":
            print("Frase vacía. Inténtalo de nuevo.")
        elif frase_ingresada.isdigit():
            print("La frase contiene números. Inténtalo de nuevo.")
        else:
            return frase_ingresada

def main():
    frase_valida = obtener_frase_valida()
    vocales_con_tilde, vocales_sin_tilde = contar_vocales_con_y_sin_tilde(frase_valida)
    print(f"El número de vocales con tilde en la frase es: {vocales_con_tilde}")
    print(f"El número de vocales sin tilde en la frase es: {vocales_sin_tilde}")

if __name__ == "__main__":
    main()
