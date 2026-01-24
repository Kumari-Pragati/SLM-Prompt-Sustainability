import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(geometric_sum(0), 1.0)
        self.assertAlmostEqual(geometric_sum(1), 0.5)
        self.assertAlmostEqual(geometric_sum(2), 0.25)
        self.assertAlmostEqual(geometric_sum(3), 0.125)
        self.assertAlmostEqual(geometric_sum(4), 0.0625)

    def test_zero(self):
        self.assertEqual(geometric_sum(0), 1.0)

    def test_negative_integer(self):
        self.assertEqual(geometric_sum(-1), 0.0)
        self.assertEqual(geometric_sum(-2), 0.0)
        self.assertEqual(geometric_sum(-3), 0.0)
        self.assertEqual(geometric_sum(-4), 0.0)

    def test_non_integer(self):
        self.assertEqual(geometric_sum(5.5), 0.0)
        self.assertEqual(geometric_sum(-5.5), 0.0)
        self.assertEqual(geometric_sum(3.0), 0.125)
        self.assertEqual(geometric_sum(-3.0), 0.0)
