def calcular_descuento(num_ninos):
    if num_ninos == 2:
        descuento = 0.10  # 10% de descuento para 2 niños
    elif num_ninos == 3:
        descuento = 0.15  # 15% de descuento para 3 niños
    elif num_ninos == 4:
        descuento = 0.18  # 18% de descuento para 4 niños
    elif num_ninos >= 5:
        # Para 5 o más niños, el descuento es del 18% + 1% por cada niño adicional
        descuento = 0.18 + (num_ninos - 4) * 0.01
    else:
        descuento = 0  # No hay descuento para menos de 2 niños
    return descuento

def calcular_importe_descuento(num_ninos, precio_total):
    porcentaje_descuento = calcular_descuento(num_ninos)
    importe_descuento = precio_total * porcentaje_descuento
    return importe_descuento

# Datos de la familia
num_ninos_familia = 3
precio_total_entradas = 150

# Calcular el importe del descuento
descuento = calcular_importe_descuento(num_ninos_familia, precio_total_entradas)

# Mostrar el resultado
print(f"La familia con {num_ninos_familia} niños tiene derecho a un descuento de {descuento} euros.")
