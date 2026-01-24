import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(jacobsthal_lucas(0), 2)

    def test_one(self):
        self.assertEqual(jacobsthal_lucas(1), 1)

    def test_small(self):
        self.assertEqual(jacobsthal_lucas(2), 3)

    def test_medium(self):
        self.assertEqual(jacobsthal_lucas(3), 4)

    def test_large(self):
        self.assertEqual(jacobsthal_lucas(4), 7)

    def test_edge(self):
        self.assertEqual(jacobsthal_lucas(5), 11)

    def test_negative(self):
        with self.assertRaises(ValueError):
            jacobsthal_lucas(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas(3.5)
