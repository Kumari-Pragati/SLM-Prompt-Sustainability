import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_simple_positive_input(self):
        self.assertAlmostEqual(geometric_sum(1), 1)
        self.assertAlmostEqual(geometric_sum(2), 0.5)
        self.assertAlmostEqual(geometric_sum(3), 0.375)

    def test_edge_cases(self):
        self.assertAlmostEqual(geometric_sum(0), 1)
        self.assertAlmostEqual(geometric_sum(4), 0.125)
        self.assertAlmostEqual(geometric_sum(5), 0.0625)

    def test_negative_input(self):
        self.assertEqual(geometric_sum(-1), 0)
