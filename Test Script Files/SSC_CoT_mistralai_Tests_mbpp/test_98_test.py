import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3]), 1.5)
        self.assertAlmostEqual(multiply_num([4, 5, 6]), 12 / 3)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(multiply_num([0]), 0)
        self.assertAlmostEqual(multiply_num([1]), 1)
        self.assertAlmostEqual(multiply_num([1000000]), 1)
        self.assertAlmostEqual(multiply_num([-1, -2, -3]), -1.5)
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55 / 10)

    def test_special_cases(self):
        self.assertAlmostEqual(multiply_num([1, 0]), 0.5)
        self.assertAlmostEqual(multiply_num([0, 0]), 0)
