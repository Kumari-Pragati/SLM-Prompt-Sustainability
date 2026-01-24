import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(get_inv_count(arr, len(arr)), 2)

    def test_empty_list(self):
        arr = []
        self.assertEqual(get_inv_count(arr, len(arr)), 0)

    def test_single_element_list(self):
        arr = [1]
        self.assertEqual(get_inv_count(arr, len(arr)), 0)

    def test_sorted_list(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(get_inv_count(arr, len(arr)), 0)

    def test_reverse_sorted_list(self):
        arr = [4, 3, 2, 1]
        self.assertEqual(get_inv_count(arr, len(arr)), 6)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        self.assertEqual(get_inv_count(arr, len(arr)), 6)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            get_inv_count(arr, -1)
