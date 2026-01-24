import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_positive_number(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)

    def test_zero(self):
        self.assertEqual(sqrt_root(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt_root(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt_root('a')
