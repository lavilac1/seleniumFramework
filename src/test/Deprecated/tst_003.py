import unittest

class test_003(unittest.TestCase):

    def setUP(self):
        pass

    def test_001(self):
        self.variableA = 20
        self.variableB = 30

        self.assertNotEqual(self.variableA, self.variableB, "Los valores NO son distintos")

    def test_002(self):
        self.variableA = 20
        self.variableB = 20

        self.assertEqual(self.variableA, self.variableB, "Los valores son distintos")

    def test_003(self):
        self.variableA = 10

        if self.variableA >= 10:
            self.Resultado = True

        else:
            self.Resultado = False

        self.assertTrue(self.Resultado, f"El valor es inferior a 10 es: {self.variableA}")

    def test_004(self):
        self.variableA = "Bienvenido a la clase de unittest"
        self.variableB = "unittest"

        self.assertIn(self.variableB, self.variableA, f"No coincide")

    def test_005(self):
        self.variableA = "Bienvenido a la clase de unittest"
        self.variableB = " a la clase de unittest"

        self.assertIsNot(self.variableB, self.variableA, f"Coinciden A Y B")




    def tearDown(self):
        pass


#constructor que llama la clase, investigar
if __name__ == '__main__':
    unittest.main()

