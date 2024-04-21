
def calcular_descuento(importe):
    if 100 <= importe <= 500:
        descuento = importe * 0.05
    else:
        descuento = importe * 0.08
    return descuento

# Ejemplo de uso
importe_compra = 600  # Puedes cambiar este valor para probar diferentes importes
descuento = calcular_descuento(importe_compra)
print("El importe del descuento es:", descuento, "€")
