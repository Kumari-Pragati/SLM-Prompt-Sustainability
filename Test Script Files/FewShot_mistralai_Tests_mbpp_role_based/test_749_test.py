import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):
    def test_sort_positive_numbers(self):
        self.assertEqual(sort_numeric_strings(["10", "20", "30"]), [10, 20, 30])

    def test_sort_negative_numbers(self):
        self.assertEqual(sort_numeric_strings(["-10", "-20", "-30"]), [-30, -20, -10])

    def test_sort_mixed_numbers(self):
        self.assertEqual(sort_numeric_strings(["10", "-20", "30", "-1"]), [-1, -20, 10, 30])

    def test_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_single_element(self):
        self.assertEqual(sort_numeric_strings(["1"]), [1])

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings(["a", "1"])
