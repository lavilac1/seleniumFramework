import unittest


class test001(unittest.TestCase):

    def setUp(self):
        self.VariableA = 60
        self.VariableB = 70
       

    def test_001(self):
        self.Resultado = self.VariableA + self.VariableB


    def tearDown(self):
        self.assertTrue(self.Resultado >= 100, f"El resultado no es 100, es {self.Resultado}")


if __name__ == '__main__':
    unittest.main()


class test002(unittest.TestCase):

    def setUp(self):
        self.VariableA = 'Luisa '
        self.VariableB = 'Avila'

    def test_002(self):
        self.Resultado = self.VariableA + self.VariableB

    def tearDown(self):
        self.assertEqual("Luisa Avila", self.Resultado, f"El resultado es diferente al esperado, fue {self.Resultado}")


if __name__ == '__main__':
    unittest.main()