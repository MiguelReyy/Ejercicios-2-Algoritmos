def calcular_prima_anual(num_accidentes, kilometros_recorridos, antiguedad):
    if num_accidentes == 0:
        responsabilidad = 0
    elif num_accidentes == 1:
        responsabilidad = 0.5
    elif num_accidentes == 2:
        responsabilidad = 1/3
    elif num_accidentes == 3:
        responsabilidad = 0.25
    else:
        responsabilidad = 0
    
    prima_distancia = min(kilometros_recorridos * 0.01, 400)
    
    if antiguedad < 4:
        prima_antiguedad = 0
    else:
        prima_antiguedad = 200 + (antiguedad - 4) * 20
    
    prima_total = prima_distancia + prima_antiguedad
    
    prima_final = prima_total * (1 - responsabilidad)
    
    return prima_final

# Ejemplo para conductor sin accidentes
prima_sin_accidentes = calcular_prima_anual(0, 25000, 5)
print("Prima para conductor sin accidentes:", prima_sin_accidentes, "€")

# Ejemplo para conductor con 1 accidente
prima_un_accidente = calcular_prima_anual(1, 30000, 3)
print("Prima para conductor con 1 accidente:", prima_un_accidente, "€")

# Ejemplo para conductor con 2 accidentes
prima_dos_accidentes = calcular_prima_anual(2, 35000, 6)
print("Prima para conductor con 2 accidentes:", prima_dos_accidentes, "€")

# Ejemplo para conductor con 3 accidentes
prima_tres_accidentes = calcular_prima_anual(3, 40000, 8)
print("Prima para conductor con 3 accidentes:", prima_tres_accidentes, "€")

# Ejemplo para conductor con más de 3 accidentes
prima_mas_tres_accidentes = calcular_prima_anual(4, 42000, 10)
print("Prima para conductor con más de 3 accidentes:", prima_mas_tres_accidentes, "€")
