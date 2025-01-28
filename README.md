# -PPS-Unidad1Actividad3-albertoVG


1. Clases de Equivalencia para isNumber y division

# Clases de equivalencia para isNumber:

Entrada válida: Cualquier valor numérico (int, float, str que represente un número como "3.5", "42", etc.).

Entrada no válida: Cualquier valor no numérico (str como "abc", "3a", etc., o valores como None).

# Clases de equivalencia para division:

División válida: b ≠ 0.

División inválida: b = 0 (debe devolver "Error: División por cero no permitida.").

2. Grafo de flujo para division y multiplicacion

# Grafo de flujo para division

Inicio

Condición: b == 0

Si es verdadero → Retorna mensaje de error.

Si es falso → Continúa.

Realiza la división: a / b.

Fin

# Grafo de flujo para multiplicacion

Inicio

Realiza la multiplicación: a * b.

Fin

3. Pruebas Unitarias para las Funciones

Herramientas:

Usaremos unittest para las pruebas. Implementaremos tanto Caja Negra como Caja Blanca.

# Código de las Pruebas Unitarias

## Aquí está el código de las pruebas:


    import unittest
    from calculadora import isNumber, division, multiplicacion
    
    class TestCalculadora(unittest.TestCase):

    # Pruebas para isNumber (Caja Negra y Caja Blanca)
    def test_isNumber_valores_validos(self):
        # Clases de equivalencia válidas
        self.assertTrue(isNumber("123"))  # Cadena numérica
        self.assertTrue(isNumber("3.14"))  # Cadena decimal
        self.assertTrue(isNumber(42))  # Entero
        self.assertTrue(isNumber(3.14))  # Flotante

    def test_isNumber_valores_invalidos(self):
        # Clases de equivalencia inválidas
        self.assertFalse(isNumber("abc"))  # Cadena no numérica
        self.assertFalse(isNumber("123abc"))  # Mixta
        self.assertFalse(isNumber(None))  # Valor None

    # Pruebas para division (Caja Negra)
    def test_division_valores_validos(self):
        # Clases de equivalencia válidas
        self.assertEqual(division(10, 2), 5)  # División normal
        self.assertEqual(division(0, 1), 0)  # Dividendo es 0
        self.assertEqual(division(-10, 2), -5)  # Números negativos

    def test_division_division_por_cero(self):
        # Clase de equivalencia inválida
        self.assertEqual(division(10, 0), "Error: División por cero no permitida.")

    # Pruebas para multiplicacion (Caja Blanca)
    def test_multiplicacion(self):
        # Cobertura de rutas del código
        self.assertEqual(multiplicacion(2, 3), 6)  # Números positivos
        self.assertEqual(multiplicacion(-2, 3), -6)  # Número negativo
        self.assertEqual(multiplicacion(0, 3), 0)  # Un número es 0
        self.assertEqual(multiplicacion(2, 0), 0)  # El otro número es 0
        self.assertEqual(multiplicacion(-2, -3), 6)  # Dos números negativos

    if __name__ == "__main__":
        unittest.main()

4. Generación del Grafo de Flujo

Voy a generar el grafo de flujo para las funciones division y multiplicacion en Python mediante pseudocódigo y visualización.

# Código del Grafo de Flujo

Vamos a dibujar los grafos de flujo en texto para cada función. Aquí están:

# Grafo para division:

Inicio

Condición: b == 0

Si es verdadero → Retorna "Error: División por cero no permitida."

Si es falso → Calcula a / b y retorna.

Fin

# Grafo para multiplicacion:

Inicio

Multiplica a * b.

Retorna el resultado.

Fin
