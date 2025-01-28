import unittest
import Calculadora

ca = Calculadora

class TestIsNumberCajaNegra(unittest.TestCase):

    def test_integer(self):
        self.assertTrue(ca.isnumber(1))
        self.assertTrue(ca.isnumber(-1))
        self.assertTrue(ca.isnumber(0))
        self.assertTrue(ca.isnumber(3))
        
    def test_great_integer(self):
        self.assertTrue(ca.isnumber(1111111111111111111111111111111111111111111111111111111111111111111111))

    def test_float(self):
        self.assertTrue(ca.isnumber(1.5))
        self.assertTrue(ca.isnumber(-1.5))
        self.assertTrue(ca.isnumber(-0))
        self.assertTrue(ca.isnumber(0.00000000000000000000000000000000000000001))

    def test_string_number(self):
        self.assertTrue(ca.isnumber("2.5"))
        self.assertTrue(ca.isnumber("2"))
        self.assertTrue(ca.isnumber("0"))

    def test_string_non_number(self):
        self.assertFalse(ca.isnumber("hello"))
        self.assertTrue(ca.isnumber(""))

    def test_none(self):
        self.assertFalse(ca.isnumber(None))

    def test_boolean(self):
        self.assertTrue(ca.isnumber(True))
        self.assertTrue(ca.isnumber(False))

    # Pruebas para division (Caja Negra)
    def test_division_valores_validos(self):
        # Clases de equivalencia válidas
    def test_Positivo(self):
        self.assertEqual(ca.division(1,1),1)
    def test_Divisor0(self):
        self.assertFalse(ca.division(1,0),False)
    def test_positivo(self):
        self.assertFalse(ca.division(1,3),False)

    def test_division_division_por_cero(self):
        # Clase de equivalencia inválida
        self.assertFalse(division(10, 0), "Error: División por cero no permitida.")

    # Pruebas para multiplicacion (Caja Blanca)
    def test_multiplicacion(self):
        # Cobertura de rutas del código
        self.assertTrue(ca.multiplicacion(2, 3), 6)  # Números positivos
        self.assertTrue(ca.multiplicacion(-2, 3), -6)  # Número negativo
        self.assertTrue(ca.multiplicacion(0, 3), 0)  # Un número es 0
        self.assertTrue(ca.multiplicacion(2, 0), 0)  # El otro número es 0
        self.assertTrue(ca.multiplicacion(-2, -3), 6)  # Dos números negativos

    if __name__ == '__main__':     
    unittest.main(argv=['ignored', '-v'], exit=False)