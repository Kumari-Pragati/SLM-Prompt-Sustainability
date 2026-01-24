import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_sort_numeric_strings_typical_case(self):
        self.assertEqual(sort_numeric_strings(['10', '20', '30', '40', '50']), [10, 20, 30, 40, 50])

    def test_sort_numeric_strings_edge_case_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_sort_numeric_strings_edge_case_single_element(self):
        self.assertEqual(sort_numeric_strings(['1']), [1])

    def test_sort_numeric_strings_edge_case_negative_numbers(self):
        self.assertEqual(sort_numeric_strings(['-10', '20', '-30', '-40', '-50']), [-50, -40, -30, -20, 10])

    def test_sort_numeric_strings_edge_case_mixed_signs(self):
        self.assertEqual(sort_numeric_strings(['10', '-20', '30', '-40', '50']), [10, -40, -20, 30, 50])

    def test_sort_numeric_strings_error_case_non_numeric_string(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings(['a', '1'])
