import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_Max([], 0, 0), None)

    def test_single_element_list(self):
        self.assertEqual(find_Max([1], 0, 0), 1)

    def test_multiple_elements_ascending_order(self):
        self.assertEqual(find_Max([1, 2, 3], 0, 2), 1)

    def test_multiple_elements_descending_order(self):
        self.assertEqual(find_Max([3, 2, 1], 0, 2), 3)

    def test_multiple_elements_mixed_order(self):
        self.assertEqual(find_Max([1, 3, 2], 0, 2), 3)

    def test_duplicate_elements(self):
        self.assertEqual(find_Max([1, 1, 2], 0, 2), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Max([-1, -2, -3], 0, 2), -1)

    def test_large_numbers(self):
        self.assertEqual(find_Max([1000000001, 1000000002, 1000000003], 0, 2), 1000000001)

    def test_invalid_input_low_greater_than_high(self):
        with self.assertRaises(ValueError):
            find_Max([1, 2, 3], 3, 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            find_Max([1, 2, 3], -1, 0)
