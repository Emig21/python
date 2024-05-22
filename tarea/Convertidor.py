celsius = float(input("Ingrese la temperatura Gardos Celsius:   "))

def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5) + 32 

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")