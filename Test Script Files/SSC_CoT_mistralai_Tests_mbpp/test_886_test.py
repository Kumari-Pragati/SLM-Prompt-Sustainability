import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(sum_num([5, 10, 15, 20]), 12.5)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(sum_num([0, 0, 0, 0]), 0)
        self.assertAlmostEqual(sum_num([1]), 1)
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, -3]), -0.75)
        self.assertAlmostEqual(sum_num([1, -2, 3]), 1.5)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(sum_num([1.1, 2.2, 3.3]), 2.2)
        self.assertAlmostEqual(sum_num([0.1, 0.2, 0.3]), 0.2)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            sum_num([])

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sum_num(["a", "b", "c"])
