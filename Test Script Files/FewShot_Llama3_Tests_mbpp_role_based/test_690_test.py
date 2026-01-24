import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_single_element_list(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_two_element_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2]), [])

    def test_three_element_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3]), [2, 6])

    def test_four_element_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6, 12])

    def test_list_with_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([-1, 2, 3, 4]), [2, 6, 12])

    def test_list_with_zero(self):
        self.assertEqual(mul_consecutive_nums([0, 1, 2, 3]), [0, 2, 6])
