import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_two_elements_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_three_elements_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3], 3), -6)

    def test_large_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([1000, 2000, 3000], 3), 6000)

    def test_small_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 10), 6)

    def test_zero(self):
        self.assertEqual(max_sum_of_three_consecutive([0, 0, 0], 3), 0)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            max_sum_of_three_consecutive('not a list', 3)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            max_sum_of_three_consecutive([1, 2, 3], -1)
