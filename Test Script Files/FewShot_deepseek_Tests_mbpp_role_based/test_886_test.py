import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_edge_condition(self):
        self.assertAlmostEqual(sum_num([0]), 0.0)

    def test_boundary_condition(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_num('123')

        with self.assertRaises(ZeroDivisionError):
            sum_num([])
