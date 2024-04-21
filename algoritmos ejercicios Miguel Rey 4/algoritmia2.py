def clasificar_numeros(a, b):
    # Calcular la suma y el producto de los números
    suma = a + b
    producto = a * b
    
    # Crear una lista con los números y calcular la suma y el producto
    numeros = [a, b, suma, producto]
    
    # Ordenar la lista
    numeros.sort()
    
    return numeros

# Ejemplo de uso
a = -15
b = -2
resultado = clasificar_numeros(a, b)
print(resultado)
