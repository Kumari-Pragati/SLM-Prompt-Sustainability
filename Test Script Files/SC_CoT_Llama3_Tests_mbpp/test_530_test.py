import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(negative_count([1, 2, 3, 4, 5]), 0.0)
        self.assertAlmostEqual(negative_count([-1, -2, -3, -4, -5]), 1.0)
        self.assertAlmostEqual(negative_count([1, -2, 3, -4, 5]), 0.5)
        self.assertAlmostEqual(negative_count([-1, 2, -3, 4, -5]), 1.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(negative_count([]), 0.0)
        self.assertAlmostEqual(negative_count([0]), 0.0)
        self.assertAlmostEqual(negative_count([0, 0, 0, 0, 0]), 0.0)
        self.assertAlmostEqual(negative_count([-0, -0, -0, -0, -0]), 1.0)

    def test_special_cases(self):
        self.assertAlmostEqual(negative_count([1, 1, 1, 1, 1]), 0.0)
        self.assertAlmostEqual(negative_count([-1, -1, -1, -1, -1]), 1.0)
        self.assertAlmostEqual(negative_count([1, -1, 1, -1, 1]), 0.5)
        self.assertAlmostEqual(negative_count([-1, 1, -1, 1, -1]), 0.5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            negative_count('abc')
        with self.assertRaises(TypeError):
            negative_count([1, '2', 3, 4, 5])
