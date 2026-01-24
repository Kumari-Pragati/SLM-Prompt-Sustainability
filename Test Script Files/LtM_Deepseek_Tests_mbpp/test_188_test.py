import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(prod_Square(4))
        self.assertTrue(prod_Square(144))
        self.assertFalse(prod_Square(5))
        self.assertFalse(prod_Square(18))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertFalse(prod_Square(0))
        self.assertFalse(prod_Square(1))
        self.assertFalse(prod_Square(2))
        self.assertFalse(prod_Square(3))
        self.assertTrue(prod_Square(4))
        self.assertFalse(prod_Square(6))
        self.assertFalse(prod_Square(8))
        self.assertFalse(prod_Square(9))
        self.assertFalse(prod_Square(10))
        self.assertFalse(prod_Square(11))
        self.assertFalse(prod_Square(12))
        self.assertFalse(prod_Square(13))
        self.assertFalse(prod_Square(15))
        self.assertFalse(prod_Square(16))
        self.assertFalse(prod_Square(17))
        self.assertFalse(prod_Square(18))
        self.assertFalse(prod_Square(19))
        self.assertFalse(prod_Square(20))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(prod_Square(100))
        self.assertFalse(prod_Square(225))
        self.assertFalse(prod_Square(3600))
        self.assertFalse(prod_Square(441))
        self.assertFalse(prod_Square(500))
        self.assertFalse(prod_Square(625))
        self.assertFalse(prod_Square(729))
        self.assertFalse(prod_Square(800))
        self.assertFalse(prod_Square(900))
        self.assertFalse(prod_Square(1000))
