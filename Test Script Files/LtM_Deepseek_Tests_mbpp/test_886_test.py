import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_empty_list(self):
        self.assertEqual(sum_num([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_num([1]), 1)

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, -3, -4, -5]), -3.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(sum_num(list(range(1, 1001))), 500.5)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(sum_num([1.1, 2.2, 3.3, 4.4, 5.5]), 3.0)
