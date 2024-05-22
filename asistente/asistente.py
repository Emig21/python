import pyttsx3

# Inicializar el motor de pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Lista de comandos y respuestas
commands = {
    "hola": "Hola, ¿cómo estás?",
    "qué hora es": "Lo siento, no tengo un reloj ahora mismo.",
    "adiós": "Adiós, que tengas un buen día."
}

# Pregunta inicial
initial_question = "¿En qué te puedo ayudar?"
print(f"Asistente: {initial_question}")
speak(initial_question)

while True:
    # Simular la entrada de un comando por el usuario
    user_input = input("Tú: ").lower()

    if user_input in commands:
        response = commands[user_input]
        print(f"Asistente: {response}")
        speak(response)
    elif user_input == "salir":
        goodbye_message = "Adiós, hasta luego."
        print(f"Asistente: {goodbye_message}")
        speak(goodbye_message)
        break
    else:
        response = "Lo siento, no entiendo el comando."
        print(f"Asistente: {response}")
        speak(response)
