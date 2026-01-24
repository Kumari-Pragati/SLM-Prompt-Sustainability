import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_geometric_sum_positive(self):
        self.assertAlmostEqual(geometric_sum(0), 1, places=6)
        self.assertAlmostEqual(geometric_sum(1), 0.5, places=6)
        self.assertAlmostEqual(geometric_sum(2), 0.25, places=6)
        self.assertAlmostEqual(geometric_sum(3), 0.125, places=6)

    def test_geometric_sum_negative(self):
        self.assertEqual(geometric_sum(-1), 0)
        self.assertEqual(geometric_sum(-2), 0)
        self.assertEqual(geometric_sum(-3), 0)

    def test_geometric_sum_zero(self):
        self.assertAlmostEqual(geometric_sum(0), 1, places=6)

    def test_geometric_sum_edge(self):
        self.assertAlmostEqual(geometric_sum(10), 0.0009765625, places=6)
