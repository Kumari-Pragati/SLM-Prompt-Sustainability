import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_sort_numeric_strings_positive(self):
        self.assertEqual(sort_numeric_strings(['10', '20', '5', '15', '3']), [3, 5, 10, 15, 20])
        self.assertEqual(sort_numeric_strings(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sort_numeric_strings(['100', '200', '50', '150', '30']), [30, 50, 100, 150, 200])

    def test_sort_numeric_strings_negative(self):
        self.assertEqual(sort_numeric_strings(['-10', '-20', '-5', '-15', '-3']), [-3, -5, -10, -15, -20])
        self.assertEqual(sort_numeric_strings(['-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']), [-9, -8, -7, -6, -5, -4, -3, -2, -1, -0])
        self.assertEqual(sort_numeric_strings(['-100', '-200', '-50', '-150', '-30']), [-30, -50, -100, -150, -200])

    def test_sort_numeric_strings_mixed(self):
        self.assertEqual(sort_numeric_strings(['1a', '20z', '5', '15b', '3', '-1', '00x']), ['-1', '00x', '1a', '15b', 3, 5, 20])
        self.assertEqual(sort_numeric_strings(['10', '20z', '5', '15b', '3', '-1', '00x', '100y']), ['-1', '00x', '10', '100y', '15b', 3, 5, 20])
        self.assertEqual(sort_numeric_strings(['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
