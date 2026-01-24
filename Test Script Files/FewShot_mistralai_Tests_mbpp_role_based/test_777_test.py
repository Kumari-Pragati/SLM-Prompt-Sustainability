import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_duplicate_elements(self):
        self.assertEqual(find_Sum([1, 1, 2, 3, 4, 4, 5], 7), 15)

    def test_sorted_ascending(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_sorted_descending(self):
        self.assertEqual(find_Sum([5, 4, 3, 2, 1], 5), 15)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4, -5], 5), -15)

    def test_mixed_numbers(self):
        self.assertEqual(find_Sum([1, -2, 3, -4, 5], 5), 15)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            find_Sum(1.5, 0)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            find_Sum([1, 2, 3], -1)
