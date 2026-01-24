import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_numeric_strings(""), [])

    def test_single_element_list(self):
        self.assertEqual(sort_numeric_strings("10"), [10])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_numeric_strings("10,20,30,1,2,3"), [1, 2, 3, 10, 20, 30])

    def test_negative_numbers(self):
        self.assertEqual(sort_numeric_strings("-10,-20,-30,1,2,3"), [-30, -20, -10, 1, 2, 3])

    def test_duplicates(self):
        self.assertEqual(sort_numeric_strings("10,10,20,30,1,2,3"), [1, 2, 3, 10, 10, 20, 30])

    def test_non_numeric_strings(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings("10,abc,20,30,1,2,3")
