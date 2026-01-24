import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_jacobsthal_lucas_zero(self):
        self.assertEqual(jacobsthal_lucas(0), 2)

    def test_jacobsthal_lucas_one(self):
        self.assertEqual(jacobsthal_lucas(1), 1)

    def test_jacobsthal_lucas_positive(self):
        self.assertEqual(jacobsthal_lucas(5), 47)

    def test_jacobsthal_lucas_negative(self):
        with self.assertRaises(IndexError):
            jacobsthal_lucas(-1)

    def test_jacobsthal_lucas_large(self):
        self.assertEqual(jacobsthal_lucas(20), 1048575)
