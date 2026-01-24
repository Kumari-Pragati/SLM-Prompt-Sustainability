import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_jacobsthal_lucas_positive_integer(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(5), 14)
        self.assertEqual(jacobsthal_lucas(10), 77)

    def test_jacobsthal_lucas_zero(self):
        self.assertRaises(ValueError, jacobsthal_lucas, 0)

    def test_jacobsthal_lucas_negative_integer(self):
        self.assertRaises(ValueError, jacobsthal_lucas, -1)

    def test_jacobsthal_lucas_large_integer(self):
        self.assertEqual(jacobsthal_lucas(100), 12676506002282212597409541418223987984846575)
