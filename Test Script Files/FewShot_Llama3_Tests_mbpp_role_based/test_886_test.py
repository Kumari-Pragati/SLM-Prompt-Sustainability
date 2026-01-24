import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(sum_num([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(sum_num([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(sum_num([]), 0)

    def test_list_with_zero(self):
        self.assertEqual(sum_num([0, 1, 2, 3]), 1)

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_num([-1, -2, -3, -4]), -2)

    def test_list_with_float_numbers(self):
        self.assertAlmostEqual(sum_num([1.0, 2.0, 3.0, 4.0]), 2.5)
