import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_single_element_list(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_two_elements_list(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [1])

    def test_three_elements_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3]), [1, 1])

    def test_four_elements_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [1, 1, 2])

    def test_five_elements_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 1, 2, 3])

    def test_large_list(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_negative_numbers(self):
        self.assertEqual(add_consecutive_nums([-1, -2, -3, -4, -5]), [-1, -1, -2, -3, -4])

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(add_consecutive_nums([1, -2, 3, -4, 5]), [1, 1, 1, 1])
