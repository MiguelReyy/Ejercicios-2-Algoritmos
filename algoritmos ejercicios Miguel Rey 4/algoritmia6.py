
def calcular_descuento(cantidad_componentes, cliente):
    # Porcentaje de descuento base según la cantidad de componentes
    if 10000 <= cantidad_componentes <= 20000:
        descuento_base = 0.10  # 10% de descuento para 10,000 a 20,000 componentes
    elif 20001 <= cantidad_componentes <= 40000:
        descuento_base = 0.15  # 15% de descuento para 20,001 a 40,000 componentes
    else:
        descuento_base = 0.20  # 20% de descuento para más de 40,000 componentes
    
    # Ajustes al porcentaje de descuento según el cliente
    if cliente == "COMMAQ":
        descuento_base -= 0.02  # Reducción del 2% si el cliente es COMMAQ
    elif cliente == "BEL":
        descuento_base += 0.01  # Aumento del 1% si el cliente es BEL
    
    return descuento_base

def calcular_importe_descuento(cantidad_componentes, cliente, precio_total):
    porcentaje_descuento = calcular_descuento(cantidad_componentes, cliente)
    importe_descuento = precio_total * porcentaje_descuento
    return importe_descuento

# Ejemplo de uso
cantidad_componentes = 25000
cliente = "COMMAQ"
precio_total_componentes = 10000  # Precio total de los componentes
descuento = calcular_importe_descuento(cantidad_componentes, cliente, precio_total_componentes)
print("El importe del descuento es:", descuento)
