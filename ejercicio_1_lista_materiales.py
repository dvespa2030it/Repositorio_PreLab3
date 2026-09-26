# Lista de pesos de piezas

pesos_piezas = [-5.0, 0.0, 10.5, 12.5, 14.2, 18.1]

# Evaluación de cada pieza según su peso

for i in range(len(pesos_piezas)): # 0, 1, 2, 3, 4, 5
    if pesos_piezas[i] <= 0:
        print("Error de lectura: Flujo negativo descartado")
    elif pesos_piezas[i] > 1 and pesos_piezas[i] <= 13:
        print("Pieza Ligera aprobada")
    elif pesos_piezas[i] > 13:
        print("Pieza Pesada aprobada")

# Conteo de piezas aprobadas

def pieza_ligera_aprobadas():
    print("Piezas ligeras aprobadas: ", sum(1 for peso in pesos_piezas if 1 < peso <= 13))
    return sum(1 for peso in pesos_piezas if 1 < peso <= 13)

def pieza_pesada_aprobadas():
    print("Piezas pesadas aprobadas: ", sum(1 for peso in pesos_piezas if peso > 13))
    return sum(1 for peso in pesos_piezas if peso > 13)

# Conteo total de piezas válidas

piezas_ligeras = pieza_ligera_aprobadas()
piezas_pesadas = pieza_pesada_aprobadas()

piezas_validas = piezas_ligeras + piezas_pesadas
print("Piezas válidas totales = ", piezas_validas)