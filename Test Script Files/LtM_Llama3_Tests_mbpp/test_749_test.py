import unittest
from mbpp_749_code import sort_numeric_strings

class Test749Code(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sort_numeric_strings(''), [])

    def test_single_element(self):
        self.assertEqual(sort_numeric_strings('1'), [1])

    def test_multiple_elements(self):
        self.assertEqual(sort_numeric_strings('1 2 3'), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(sort_numeric_strings('-1 0 1'), [-1, 0, 1])

    def test_duplicates(self):
        self.assertEqual(sort_numeric_strings('1 2 2 3'), [1, 2, 2, 3])

    def test_non_numeric_strings(self):
        with self.assertRaises(ValueError):
            sort_numeric_strings('1 a 3')

    def test_mixed_input(self):
        self.assertEqual(sort_numeric_strings('1 2 -3 4'), [-3, 1, 2, 4])
