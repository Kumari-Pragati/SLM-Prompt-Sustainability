import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(zero_count([0, 1, 0, 1, 0]), 0.6, 2)
        self.assertAlmostEqual(zero_count([0, 0, 0, 0, 0]), 1.0, 2)
        self.assertAlmostEqual(zero_count([1, 1, 1, 1, 1]), 0.0, 2)

    def test_edge_conditions(self):
        self.assertAlmostEqual(zero_count([]), 0.0, 2)
        self.assertAlmostEqual(zero_count([0]), 1.0, 2)
        self.assertAlmostEqual(zero_count([1]), 0.0, 2)

    def test_complex_cases(self):
        self.assertAlmostEqual(zero_count([0, 0, 1, 0, 1, 0, 1]), 0.428571, 5)
        self.assertAlmostEqual(zero_count([1, 0, 0, 1, 0, 0, 1]), 0.428571, 5)
