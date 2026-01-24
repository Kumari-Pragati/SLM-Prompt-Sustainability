import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(geometric_sum(0), 1, places=6)
        self.assertAlmostEqual(geometric_sum(1), 0.5, places=6)
        self.assertAlmostEqual(geometric_sum(2), 0.25, places=6)
        self.assertAlmostEqual(geometric_sum(3), 0.125, places=6)
        self.assertAlmostEqual(geometric_sum(4), 0.0625, places=6)

    def test_negative_integer(self):
        self.assertEqual(geometric_sum(-1), 0)
        self.assertEqual(geometric_sum(-2), 0)
        self.assertEqual(geometric_sum(-3), 0)
        self.assertEqual(geometric_sum(-4), 0)

    def test_zero(self):
        self.assertAlmostEqual(geometric_sum(0), 1, places=6)

    def test_non_integer(self):
        with self.assertRaises(RecursionError):
            geometric_sum(1.5)
