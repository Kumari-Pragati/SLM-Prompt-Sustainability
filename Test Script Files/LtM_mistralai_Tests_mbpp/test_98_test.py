import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3]), 2.0)
        self.assertAlmostEqual(multiply_num([4, 4, 4]), 4.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(multiply_num([0]), 0.0)
        self.assertAlmostEqual(multiply_num([-1, -1, -1]), -1.0)
        self.assertAlmostEqual(multiply_num([1e100]), 1e-100)
        self.assertAlmostEqual(multiply_num([1e-100]), 1e-100)

    def test_complex_input(self):
        self.assertAlmostEqual(multiply_num([1, 0, 2]), 1.0)
        self.assertAlmostEqual(multiply_num([1, -1, 2]), 0.5)
        self.assertAlmostEqual(multiply_num([1, 1, 0, 2]), 1.5)
