import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(geometric_sum(3), 0.375, places=3)

    def test_negative_integer(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_zero(self):
        self.assertEqual(geometric_sum(0), 1)

    def test_large_positive_integer(self):
        self.assertAlmostEqual(geometric_sum(10), 0.0009765625, places=10)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            geometric_sum('a')
