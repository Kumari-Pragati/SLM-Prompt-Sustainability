import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_numeric_strings(['1', '10', '2', '3', '100']), [1, 2, 10, 100])

    def test_edge_case_leading_zero(self):
        self.assertEqual(sort_numeric_strings(['0', '1', '10', '2', '3']), [0, 1, 2, 10, 3])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sort_numeric_strings(['-1', '1', '10', '-2', '3']), ['-2', '-1', 1, 3, 10])

    def test_edge_case_alphanumeric(self):
        self.assertEqual(sort_numeric_strings(['1a', '1b', '2', '3', '10']), [10, 1a, 1b, 2, 3])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_edge_case_single_item(self):
        self.assertEqual(sort_numeric_strings(['1']), [1])
