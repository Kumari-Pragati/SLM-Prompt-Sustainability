import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_numeric_strings(['10', '2', '30']), [2, 10, 30])

    def test_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_single_element(self):
        self.assertEqual(sort_numeric_strings(['5']), [5])

    def test_negative_numbers(self):
        self.assertEqual(sort_numeric_strings(['-1', '1']), [-1, 1])

    def test_large_numbers(self):
        self.assertEqual(sort_numeric_strings(['1000000', '2000000', '1000000']), [1000000, 1000000, 2000000])

    def test_duplicate_numbers(self):
        self.assertEqual(sort_numeric_strings(['5', '5', '5']), [5, 5, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_numeric_strings(['10', '20', None])
