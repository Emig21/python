print("Ingrese fecha")

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

def siguiente_dia(d, m, a):
    if d > 0 and d < 30:
        d += 1
    else:
        d = 1
        if m > 0 and m < 12:
            m += 1
        else:
            m = 1
            a += 1
    return d, m, a

nuevo_dia, nuevo_mes, nuevo_anio = siguiente_dia(dia, mes, anio)

print(f"La fecha del siguiente día es: {nuevo_dia}/{nuevo_mes}/{nuevo_anio}")
