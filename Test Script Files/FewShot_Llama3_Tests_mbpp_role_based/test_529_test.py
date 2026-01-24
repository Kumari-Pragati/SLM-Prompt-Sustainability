import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_small_positive_integer(self):
        self.assertEqual(jacobsthal_lucas(3), 4)

    def test_large_positive_integer(self):
        self.assertEqual(jacobsthal_lucas(10), 123)

    def test_zero(self):
        self.assertEqual(jacobsthal_lucas(0), 2)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas(3.5)
