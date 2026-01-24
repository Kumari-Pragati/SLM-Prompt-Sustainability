import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sort_numeric_strings(['10', '2', '3']), [2, 3, 10])

    def test_edge_case_single_element(self):
        self.assertEqual(sort_numeric_strings(['5']), [5])

    def test_boundary_case_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_boundary_case_all_same_elements(self):
        self.assertEqual(sort_numeric_strings(['5', '5', '5']), [5, 5, 5])

    def test_error_handling_non_string_elements(self):
        with self.assertRaises(TypeError):
            sort_numeric_strings([10, '2', '3'])

    def test_error_handling_non_numeric_strings(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings(['10', '2a', '3'])
