# Calculadora con módulo incluido

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def division(a, b):
    if not mayorCero(b):
        print ("El divisor debe de ser mayor que cero")
        return False
    else: 
        resultado = a / b
        return resultado

def isNumber(value):
    """Devuelve True si el valor es un número, False en caso contrario."""
    if value is None:
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False

def mayorCero(value):
    """Devuelve True si el número es mayor que cero, False en caso contrario."""
    return value > 0

def main():
    """Programa principal para interactuar con el usuario."""
    print("Bienvenido a la calculadora.")
    
    # Solicitar los dos números al usuario
    num1 = input("Introduce el primer número: ")
    while not isNumber(num1):
        num1 = input("Esto no es un número. Introduce un número válido: ")
    num1 = float(num1)

    num2 = input("Introduce el segundo número: ")
    while not isNumber(num2):
        num2 = input("Esto no es un número. Introduce un número válido: ")
    num2 = float(num2)

    # Mostrar el menú de operaciones
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Introduce el número de la operación: ")
        
        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")
        elif opcion == "5":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

# Llamada al programa principal
if __name__ == "__main__":
    main()