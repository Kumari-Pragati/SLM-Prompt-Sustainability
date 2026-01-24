import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(negative_count([1, 2, -3, 4]), 0.25)

    def test_edge_cases(self):
        self.assertAlmostEqual(negative_count([0]), 0.0)
        self.assertAlmostEqual(negative_count([-1]), 1.0)
        self.assertAlmostEqual(negative_count([-1, -1]), 1.0)
        self.assertAlmostEqual(negative_count([-1, -1, -1]), 1.0)
        self.assertAlmostEqual(negative_count([-1, -1, -1, -1]), 1.0)
        self.assertAlmostEqual(negative_count([-1, -1, -1, -1, -1]), 1.0)

    def test_boundary_cases(self):
        self.assertAlmostEqual(negative_count([-1, 0]), 0.5)
        self.assertAlmostEqual(negative_count([-1, 1]), 0.0)
        self.assertAlmostEqual(negative_count([-1, -1, 0]), 0.5)
        self.assertAlmostEqual(negative_count([-1, -1, 1]), 0.0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, negative_count, [1, 2, "three"])
        self.assertRaises(TypeError, negative_count, [1, 2, [3, 4]])
