import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(sum_num([]), 0.0)

    def test_single_element(self):
        self.assertAlmostEqual(sum_num([1]), 1.0)

    def test_multiple_elements(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, 3]), 0.3333333333333333)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(sum_num([1.1, 2.2, 3.3]), 2.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(sum_num([1000000001, 1000000002, 1000000003]), 3.0)
