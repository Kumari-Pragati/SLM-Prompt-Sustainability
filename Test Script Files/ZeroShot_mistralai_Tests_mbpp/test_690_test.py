import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(mul_consecutive_nums([]), [])

    def test_single_element_list(self):
        self.assertListEqual(mul_consecutive_nums([1]), [])

    def test_two_elements_list(self):
        self.assertListEqual(mul_consecutive_nums([1, 2]), [2])

    def test_three_elements_list(self):
        self.assertListEqual(mul_consecutive_nums([1, 2, 3]), [2, 3])

    def test_four_elements_list(self):
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 3, 4])

    def test_negative_numbers(self):
        self.assertListEqual(mul_consecutive_nums([-1, -2, -3]), [2, 3, -4])

    def test_zero_in_list(self):
        self.assertListEqual(mul_consecutive_nums([0, 1, 2]), [0, 1])

    def test_duplicate_numbers(self):
        self.assertListEqual(mul_consecutive_nums([1, 1, 2]), [2])
