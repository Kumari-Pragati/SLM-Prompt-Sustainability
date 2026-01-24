import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sort_numeric_strings(""), [])

    def test_single_element_input(self):
        self.assertEqual(sort_numeric_strings("5"), [5])

    def test_multiple_elements_input(self):
        self.assertEqual(sort_numeric_strings("5,2,8,4"), [2, 4, 5, 8])

    def test_negative_numbers_input(self):
        self.assertEqual(sort_numeric_strings("-5,-2,-8,-4"), [-8, -5, -4, -2])

    def test_duplicates_input(self):
        self.assertEqual(sort_numeric_strings("5,2,2,8,4,4"), [2, 2, 4, 4, 5, 8])

    def test_non_numeric_strings_input(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings("5,abc,8,4")
