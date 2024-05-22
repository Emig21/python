veiculo1 = int(input("Ingrese velosidad de veliculo 1: "))
veiculo2 = int(input("Ingrese velosidad de veliculo 2: "))
distancia = int(input("Ingrese distancia de los dos veículos: "))

if veiculo1 > 0 and veiculo2 >0:
  tiempo = distancia / (veiculo1 + veiculo2)
else:
  print("ERROR")