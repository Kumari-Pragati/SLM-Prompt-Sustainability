import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_single_element_list(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_two_elements_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2]), [])

    def test_three_elements_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3]), [1, 2])

    def test_four_elements_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6])

    def test_five_elements_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [6, 12])

    def test_list_with_duplicates(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 2, 3, 3, 3]), [2, 6, 9])

    def test_list_with_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([-1, -2, -3, -4]), [2, -6, 12])

    def test_list_with_mixed_positive_and_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([1, -2, 3, -4]), [-2, 12, -12])
