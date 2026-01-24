import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_single_element_input(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_two_element_input(self):
        self.assertEqual(mul_consecutive_nums([1, 2]), [])

    def test_three_element_input(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3]), [2, 6])

    def test_four_element_input(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6, 12])

    def test_five_element_input(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12, 20])

    def test_edge_case_input(self):
        self.assertEqual(mul_consecutive_nums([1, 1]), [])

    def test_negative_numbers_input(self):
        self.assertEqual(mul_consecutive_nums([-1, -2]), [])

    def test_mixed_positive_and_negative_numbers_input(self):
        self.assertEqual(mul_consecutive_nums([1, -2, 3, -4]), [])
