import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_geometric_sum_positive_integer(self):
        self.assertAlmostEqual(geometric_sum(0), 1)
        self.assertAlmostEqual(geometric_sum(1), 1)
        self.assertAlmostEqual(geometric_sum(2), 0.5)
        self.assertAlmostEqual(geometric_sum(3), 0.375)
        self.assertAlmostEqual(geometric_sum(4), 0.25)

    def test_geometric_sum_zero(self):
        self.assertEqual(geometric_sum(0), 1)

    def test_geometric_sum_negative_integer(self):
        self.assertEqual(geometric_sum(-1), 0)
        self.assertEqual(geometric_sum(-2), 0)
        self.assertEqual(geometric_sum(-3), 0)

    def test_geometric_sum_non_integer(self):
        self.assertEqual(geometric_sum(5.5), 0)
        self.assertEqual(geometric_sum(-5.5), 0)
