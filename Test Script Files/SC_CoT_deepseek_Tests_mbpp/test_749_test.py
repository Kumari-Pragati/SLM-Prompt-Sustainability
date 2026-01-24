import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sort_numeric_strings(['10', '2', '3']), [2, 3, 10])

    def test_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_single_element(self):
        self.assertEqual(sort_numeric_strings(['5']), [5])

    def test_duplicate_elements(self):
        self.assertEqual(sort_numeric_strings(['3', '1', '2', '1']), [1, 1, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(sort_numeric_strings(['1000', '200', '30']), [30, 200, 1000])

    def test_negative_numbers(self):
        self.assertEqual(sort_numeric_strings(['-1', '-2', '-3']), [-3, -2, -1])

    def test_mixed_positive_negative(self):
        self.assertEqual(sort_numeric_strings(['1', '-1', '2', '-2']), [-2, -1, 1, 2])

    def test_non_numeric_strings(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings(['1', '2', 'three'])

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            sort_numeric_strings([1, '2', '3'])
