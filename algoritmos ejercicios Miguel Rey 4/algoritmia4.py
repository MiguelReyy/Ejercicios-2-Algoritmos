class Alumno:
    def __init__(self, notas):
        self.notas = notas
        self.media = sum(self.notas) / len(self.notas)
    
    def evaluar(self):
        if self.media > 15:
            return "Alumno con talento"
        elif 12 <= self.media <= 15:
            return "Con capacidad"
        else:
            return "Debe reorientarse"

def calcular_evaluacion():
    # Solicitar al usuario que ingrese las cuatro notas del alumno
    notas = []
    for i in range(4):
        # Validar que la nota ingresada esté en el rango de 0 a 20
        nota = float(input(f"Ingrese la nota {i+1} (de 0 a 20): "))
        while nota < 0 or nota > 20:
            print("La nota debe estar entre 0 y 20.")
            nota = float(input(f"Ingrese la nota {i+1} (de 0 a 20): "))
        notas.append(nota)
    
    # Crear un objeto Alumno con las notas ingresadas
    alumno = Alumno(notas)
    
    # Obtener la evaluación del alumno
    evaluacion = alumno.evaluar()
    
    # Devolver la media del alumno y su evaluación
    return alumno.media, evaluacion

# Función principal para ejecutar el programa
def main():
    # Calcular la media y la evaluación del alumno
    media, evaluacion = calcular_evaluacion()
    
    # Imprimir la media y la evaluación
    print(f"La media del alumno es: {media}")
    print(f"Evaluación: {evaluacion}")

# Llamar a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
