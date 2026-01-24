import unittest
from mbpp_749_code import sort_numeric_strings

class Test749Code(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sort_numeric_strings(""), [])

    def test_single_element(self):
        self.assertEqual(sort_numeric_strings("5"), [5])

    def test_multiple_elements(self):
        self.assertEqual(sort_numeric_strings("5,2,8,4"), [2, 4, 5, 8])

    def test_negative_numbers(self):
        self.assertEqual(sort_numeric_strings("-5,-2,8,4"), [-5, -2, 4, 8])

    def test_duplicates(self):
        self.assertEqual(sort_numeric_strings("5,5,2,8,4,4"), [2, 4, 4, 5, 5, 8])

    def test_non_numeric_strings(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings("5,abc,8,4")

    def test_mixed_types(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings("5,2,'8',4")
