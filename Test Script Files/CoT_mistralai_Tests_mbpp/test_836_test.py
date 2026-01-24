import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        for num in range(-100, 101):
            self.assertEqual(max_sub_array_sum([num], 1), 1)

    def test_positive_numbers(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_sub_array_sum(test_list, len(test_list)), len(test_list))

    def test_negative_numbers(self):
        test_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        self.assertEqual(max_sub_array_sum(test_list, len(test_list)), 1)

    def test_mixed_numbers(self):
        test_list = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        self.assertEqual(max_sub_array_sum(test_list, len(test_list)), 5)

    def test_negative_sum(self):
        test_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        self.assertEqual(max_sub_array_sum(test_list, 1), 1)

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, max_sub_array_sum, 'invalid_input', 10)

    def test_invalid_input_size(self):
        self.assertRaises(TypeError, max_sub_array_sum, [1, 2, 3], -1)
