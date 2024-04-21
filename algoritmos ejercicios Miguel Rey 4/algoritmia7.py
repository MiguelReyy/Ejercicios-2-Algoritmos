def calcular_precio_coste_alumno(num_alumnos):
    # Calcular el costo del trayecto por alumno
    costo_trayecto = 67.30 if num_alumnos <= 25 else 61.00
    
    # Definir el costo de la comida por día y por alumno
    costo_comida = 3.50
    
    # Determinar el costo del alojamiento por día y por alumno según la cantidad de alumnos
    if num_alumnos < 30:
        costo_alojamiento = 4.75
    elif num_alumnos <= 35:
        costo_alojamiento = 4.00
    else:
        costo_alojamiento = 3.50
    
    # Calcular el precio total por alumno sumando los costos del trayecto, comida y alojamiento
    precio_coste_alumno = costo_trayecto + costo_comida + costo_alojamiento
    return precio_coste_alumno

def calcular_coste_viaje(num_alumnos, num_dias):
    # Calcular el precio de coste por alumno
    precio_coste_alumno = calcular_precio_coste_alumno(num_alumnos)
    
    # Calcular el coste total del viaje multiplicando el precio de coste por alumno por el número de alumnos y por el número de días
    coste_total = precio_coste_alumno * num_alumnos * num_dias
    return coste_total

def testing():
    # Casos de prueba
    casos_prueba = [
        (20, 3),   # Menos de 30 alumnos, menos de 30 días
        (30, 3),   # Entre 30 y 35 alumnos, menos de 30 días
        (40, 3),   # Más de 35 alumnos, menos de 30 días
        (20, 10),  # Menos de 30 alumnos, más de 30 días
        (30, 10),  # Entre 30 y 35 alumnos, más de 30 días
        (40, 10)   # Más de 35 alumnos, más de 30 días
    ]
    
    # Realizar pruebas para cada caso
    for i, (num_alumnos, num_dias) in enumerate(casos_prueba):
        # Calcular el coste total del viaje para cada caso de prueba
        coste_viaje = calcular_coste_viaje(num_alumnos, num_dias)
        print(f"Caso de prueba {i+1}: {num_alumnos} alumnos, {num_dias} días. Coste total: {coste_viaje} euros.")

# Ejecutar las pruebas
testing()
