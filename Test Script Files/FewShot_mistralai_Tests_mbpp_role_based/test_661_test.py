import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6], 6), 21)

    def test_empty_list(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_two_elements_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3], 3), -6)

    def test_all_zero(self):
        self.assertEqual(max_sum_of_three_consecutive([0, 0, 0], 3), 0)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, 1, -2, 3], 4), 2)

    def test_large_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([1000000001, 1000000002, 1000000003], 3), 3000000006)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            max_sum_of_three_consecutive([1, 2, 3], -1)
