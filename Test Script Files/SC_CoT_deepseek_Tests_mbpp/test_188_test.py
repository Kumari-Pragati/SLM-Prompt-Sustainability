import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(prod_Square(4))
        self.assertTrue(prod_Square(16))
        self.assertTrue(prod_Square(81))

    def test_edge_cases(self):
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))
        self.assertFalse(prod_Square(5))
        self.assertFalse(prod_Square(7))

    def test_corner_cases(self):
        self.assertFalse(prod_Square(100))
        self.assertFalse(prod_Square(144))
        self.assertFalse(prod_Square(196))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            prod_Square('abc')
        with self.assertRaises(TypeError):
            prod_Square(None)
        with self.assertRaises(TypeError):
            prod_Square([1, 2, 3])
