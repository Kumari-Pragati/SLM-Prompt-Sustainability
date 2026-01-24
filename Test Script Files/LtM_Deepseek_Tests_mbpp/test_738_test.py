import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(geometric_sum(0), 1.0)
        self.assertAlmostEqual(geometric_sum(1), 1.5)

    def test_edge_conditions(self):
        self.assertEqual(geometric_sum(-1), 0)
        self.assertAlmostEqual(geometric_sum(2), 1.75)

    def test_complex_cases(self):
        self.assertAlmostEqual(geometric_sum(3), 1.875)
        self.assertAlmostEqual(geometric_sum(4), 1.9375)
