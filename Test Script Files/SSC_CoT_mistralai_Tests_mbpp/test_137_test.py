import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(zero_count([1, 2, 3, 0, 5, 0]), 2.0)
        self.assertAlmostEqual(zero_count([0, 0, 0]), 1.0)
        self.assertAlmostEqual(zero_count([0]), 1.0)
        self.assertAlmostEqual(zero_count([1, 2, 3]), 0.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(zero_count([]), 0.0)
        self.assertAlmostEqual(zero_count([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 1.0)
        self.assertAlmostEqual(zero_count([-1, 0, 1]), 0.3333333333333333)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            zero_count(123)
        with self.assertRaises(TypeError):
            zero_count('abc')
