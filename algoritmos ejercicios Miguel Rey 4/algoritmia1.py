from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def sucesor(dia):
    """
    Función que devuelve el sucesor de un día de la semana.
    
    Parámetros:
        - dia: Objeto de tipo DiaSemana, representa el día de la semana.
        
    Retorna:
        - Objeto de tipo DiaSemana que representa el sucesor del día dado.
    """
    if dia == DiaSemana.DOMINGO:
        return DiaSemana.LUNES
    else:
        return DiaSemana(dia.value + 1)

def main():
    # Solicitar al usuario que ingrese un día de la semana
    print("Ingrese un día de la semana:")
    print("1. Lunes")
    print("2. Martes")
    print("3. Miércoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sábado")
    print("7. Domingo")
    opcion = int(input("Seleccione una opción (1-7): "))
    
    # Validar la opción ingresada por el usuario
    if opcion < 1 or opcion > 7:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        return
    
    # Obtener el objeto DiaSemana correspondiente a la opción ingresada por el usuario
    dia = DiaSemana(opcion)
    
    # Calcular el sucesor del día ingresado
    sucesor_dia = sucesor(dia)
    
    # Imprimir el resultado
    print(f"El sucesor de {dia.name} es {sucesor_dia.name}.")

if __name__ == "__main__":
    main()
