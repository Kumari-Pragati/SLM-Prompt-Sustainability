import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(geometric_sum(3), 7 / 8)
        self.assertAlmostEqual(geometric_sum(5), 31 / 64)

    def test_zero(self):
        self.assertEqual(geometric_sum(0), 1)

    def test_negative_integer(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_fraction(self):
        with self.assertRaises(ValueError):
            geometric_sum(0.5)

    def test_large_integer(self):
        self.assertAlmostEqual(geometric_sum(100), 1.0 / (pow(2, 100)))
