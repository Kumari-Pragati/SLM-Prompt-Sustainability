import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(geometric_sum(0), 1.0)
        self.assertAlmostEqual(geometric_sum(1), 0.5)
        self.assertAlmostEqual(geometric_sum(2), 0.25)
        self.assertAlmostEqual(geometric_sum(3), 0.125)
        self.assertAlmostEqual(geometric_sum(4), 0.0625)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(geometric_sum(-1), 0)
        self.assertAlmostEqual(geometric_sum(5), 0.03125)
        self.assertAlmostEqual(geometric_sum(6), 0.015625)
        self.assertAlmostEqual(geometric_sum(7), 0.0078125)
        self.assertAlmostEqual(geometric_sum(8), 0.00390625)
