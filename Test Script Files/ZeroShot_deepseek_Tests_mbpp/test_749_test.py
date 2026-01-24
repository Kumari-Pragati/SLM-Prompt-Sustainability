import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_sort_numeric_strings(self):
        self.assertEqual(sort_numeric_strings(['10', '2', '30']), [2, 10, 30])
        self.assertEqual(sort_numeric_strings(['1', '2', '3']), [1, 2, 3])
        self.assertEqual(sort_numeric_strings(['100', '20', '3']), [3, 20, 100])
        self.assertEqual(sort_numeric_strings(['10', '20', '30']), [10, 20, 30])
        self.assertEqual(sort_numeric_strings(['10', '20', '30', '10', '20', '30']), [10, 10, 20, 20, 30, 30])
        self.assertEqual(sort_numeric_strings(['10', '20', '30', '10', '20', '30', '10']), [10, 10, 10, 20, 20, 30, 30])
