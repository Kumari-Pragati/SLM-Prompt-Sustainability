import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 2)
        self.assertEqual(jacobsthal_lucas(3), 3)
        self.assertEqual(jacobsthal_lucas(4), 4)
        self.assertEqual(jacobsthal_lucas(5), 5)
        self.assertEqual(jacobsthal_lucas(6), 9)
        self.assertEqual(jacobsthal_lucas(7), 13)
        self.assertEqual(jacobsthal_lucas(8), 21)
        self.assertEqual(jacobsthal_lucas(9), 34)
        self.assertEqual(jacobsthal_lucas(10), 55)

    def test_zero(self):
        self.assertEqual(jacobsthal_lucas(0), 2)

    def test_negative_numbers(self):
        self.assertEqual(jacobsthal_lucas(-1), None)
        self.assertEqual(jacobsthal_lucas(-2), None)
        self.assertEqual(jacobsthal_lucas(-3), None)
