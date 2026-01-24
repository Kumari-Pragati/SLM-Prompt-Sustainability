import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sort_numeric_strings(['1', '10', '2', '30']), [1, 2, 10, 30])
        self.assertEqual(sort_numeric_strings(['0', '9', '8', '7']), [0, 8, 7, 9])

    def test_edge_cases(self):
        self.assertEqual(sort_numeric_strings(['-1', '0', '1']), [-1, 0, 1])
        self.assertEqual(sort_numeric_strings(['1000', '999', '888']), [888, 999, 1000])
        self.assertEqual(sort_numeric_strings(['-1000', '-999', '-888']), [-1000, -999, -888])

    def test_complex(self):
        self.assertEqual(sort_numeric_strings(['1a', '1b', '2', '3a', '3b']), [1, 2, 3, 1a, 1b, 3a, 3b])
        self.assertEqual(sort_numeric_strings(['10z', '10y', '10x', '20', '30y']), [10x, 10y, 10z, 20, 30y])
