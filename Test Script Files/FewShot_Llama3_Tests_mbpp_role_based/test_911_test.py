import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(maximum_product(nums), 60)

    def test_edge_case_all_positive(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(maximum_product(nums), 60)

    def test_edge_case_all_negative(self):
        nums = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(maximum_product(nums), -60)

    def test_edge_case_mixed_signs(self):
        nums = [1, 2, 3, -4, -5, -6]
        self.assertEqual(maximum_product(nums), 6)

    def test_invalid_input_empty_list(self):
        nums = []
        with self.assertRaises(IndexError):
            maximum_product(nums)

    def test_invalid_input_single_element_list(self):
        nums = [1]
        with self.assertRaises(IndexError):
            maximum_product(nums)
