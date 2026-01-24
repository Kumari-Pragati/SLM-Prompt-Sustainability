import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_increasing_list(self):
        self.assertEqual(get_inv_count([1, 2, 3], 3), 0)

    def test_decreasing_list(self):
        self.assertEqual(get_inv_count([3, 2, 1], 3), 3)

    def test_mixed_list(self):
        self.assertEqual(get_inv_count([1, 3, 2], 3), 2)

    def test_duplicates(self):
        self.assertEqual(get_inv_count([1, 1, 3, 2], 4), 2)

    def test_negative_numbers(self):
        self.assertEqual(get_inv_count([-1, -2, -3], 3), 6)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            get_inv_count([], -1)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            get_inv_count([1, 2, 3], -1)
