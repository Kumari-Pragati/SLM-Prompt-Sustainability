import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_numeric_strings(['1', '2', '3']), [1, 2, 3])

    def test_edge_case_empty_input(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_edge_case_single_element_input(self):
        self.assertEqual(sort_numeric_strings(['5']), [5])

    def test_edge_case_all_negative_input(self):
        self.assertEqual(sort_numeric_strings(['-1', '-2', '-3']), [-3, -2, -1])

    def test_edge_case_all_positive_input(self):
        self.assertEqual(sort_numeric_strings(['1', '2', '3']), [1, 2, 3])

    def test_edge_case_mixed_sign_input(self):
        self.assertEqual(sort_numeric_strings(['-1', '2', '-3']), [-3, -1, 2])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings(['a', 'b', 'c'])
