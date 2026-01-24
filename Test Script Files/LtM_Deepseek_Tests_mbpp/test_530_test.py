import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(negative_count([-1, 2, -3, 4]), 0.5)
        self.assertAlmostEqual(negative_count([1, -2, 3, -4]), 0.5)
        self.assertAlmostEqual(negative_count([-1, -2, -3, -4]), 1.0)

    def test_edge_conditions(self):
        self.assertEqual(negative_count([]), 0.0)
        self.assertEqual(negative_count([0]), 0.0)
        self.assertEqual(negative_count([-1]), 1.0)
        self.assertEqual(negative_count([1]), 0.0)

    def test_complex_cases(self):
        self.assertAlmostEqual(negative_count([-1, 0, 1]), 0.33)
        self.assertAlmostEqual(negative_count([-1, -1, -1]), 1.0)
        self.assertAlmostEqual(negative_count([1, 1, 1]), 0.0)
