import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_geometric_sum_positive(self):
        self.assertAlmostEqual(geometric_sum(0), 1, places=5)
        self.assertAlmostEqual(geometric_sum(1), 0.5, places=5)
        self.assertAlmostEqual(geometric_sum(2), 0.375, places=5)
        self.assertAlmostEqual(geometric_sum(3), 0.1875, places=5)
        self.assertAlmostEqual(geometric_sum(4), 0.09375, places=5)
        self.assertAlmostEqual(geometric_sum(5), 0.046875, places=5)

    def test_geometric_sum_negative(self):
        self.assertEqual(geometric_sum(-1), 0)
        self.assertEqual(geometric_sum(-2), 0)
        self.assertEqual(geometric_sum(-3), 0)
        self.assertEqual(geometric_sum(-4), 0)
        self.assertEqual(geometric_sum(-5), 0)

    def test_geometric_sum_zero(self):
        self.assertAlmostEqual(geometric_sum(0), 1, places=5)
