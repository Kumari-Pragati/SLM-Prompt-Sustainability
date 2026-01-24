import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)

    def test_edge_case_with_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_boundary_case_with_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)

    def test_boundary_case_with_all_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)

    def test_boundary_case_with_all_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)

    def test_invalid_input_size_less_than_array_length(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum([1, 2, 3, 4], 3)

    def test_invalid_input_size_equal_to_array_length(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum([1, 2, 3, 4], 4)

    def test_invalid_input_size_greater_than_array_length(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum([1, 2, 3, 4], 5)
