import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3]), 2.0)
        self.assertAlmostEqual(multiply_num([4, 5, 6]), 24.0/3)

    def test_edge_conditions(self):
        self.assertEqual(multiply_num([1]), 1)
        self.assertEqual(multiply_num([0]), 0)
        self.assertAlmostEqual(multiply_num([-1, -2, -3]), -6.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(multiply_num([float('inf'), 2]), float('inf'))
        self.assertAlmostEqual(multiply_num([float('-inf'), -2]), float('inf'))
        self.assertAlmostEqual(multiply_num([float('nan'), 2]), float('nan'))

    def test_complex_cases(self):
        self.assertAlmostEqual(multiply_num([1, 2, 0]), 0)
        self.assertAlmostEqual(multiply_num([1, -1, -1]), -1)
        self.assertAlmostEqual(multiply_num([float('inf'), float('inf')]), float('inf'))
        self.assertAlmostEqual(multiply_num([float('-inf'), float('-inf')]), float('inf'))
