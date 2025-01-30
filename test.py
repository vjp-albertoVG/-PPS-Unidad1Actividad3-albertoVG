import unittest
from Calculadora import isNumber, division, multiplicacion

class TestIsNumberCajaNegra(unittest.TestCase):

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
    self.assertFalse(division(0, 1), 0)  # Dividendo es 0
    self.assertFalse(division(-10, 2), -5)  # Números negativos

def test_division_division_por_cero(self):
    # Clase de equivalencia inválida
    self.assertFalse(division(10, 0), "Error: División por cero no permitida.")

# Pruebas para multiplicacion (Caja Blanca)
def test_multiplicacion(self):
    # Cobertura de rutas del código
    self.assertTrue(multiplicacion(2, 3), 6)  # Números positivos
    self.assertTrue(multiplicacion(-2, 3), -6)  # Número negativo
    self.assertTrue(multiplicacion(0, 3), 0)  # Un número es 0
    self.assertTrue(multiplicacion(2, 0), 0)  # El otro número es 0
    self.assertTrue(multiplicacion(-2, -3), 6)  # Dos números negativos

if __name__ == "__main__":
    unittest.main(argv=['ignored', '-v'], exit=False)