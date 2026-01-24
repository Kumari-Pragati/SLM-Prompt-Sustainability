import unittest
from mbpp_749_code import sort_numeric_strings

class Test749Code(unittest.TestCase):
    def test_sort_numeric_strings(self):
        self.assertEqual(sort_numeric_strings(['1', '3', '2']), [1, 2, 3])
        self.assertEqual(sort_numeric_strings(['5', '2', '4']), [2, 4, 5])
        self.assertEqual(sort_numeric_strings(['10', '8', '9']), [8, 9, 10])
        self.assertEqual(sort_numeric_strings(['1', '1', '1']), [1, 1, 1])
        self.assertEqual(sort_numeric_strings(['10', '10', '10']), [10, 10, 10])
        self.assertEqual(sort_numeric_strings(['1', '2', '3', '4', '5']), [1, 2, 3, 4, 5])
        self.assertEqual(sort_numeric_strings(['5', '4', '3', '2', '1']), [1, 2, 3, 4, 5])
        self.assertEqual(sort_numeric_strings(['1', '2', '3', '4', '5', '6']), [1, 2, 3, 4, 5, 6])
        self.assertEqual(sort_numeric_strings(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sort_numeric_strings(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sort_numeric_strings(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '10']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])
        self.assertEqual(sort_numeric_strings(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1']), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sort_numeric_strings(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '10', '10']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10])
        self.assertEqual(sort_numeric_strings(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])
        self.assertEqual(sort_numeric_strings(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '10', '10', '10']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
        self.assertEqual(sort_numeric_strings(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1']), [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])
        self.assertEqual(sort_numeric_strings(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '10', '10', '10', '10']), [1, 2, 3, 4, 5, 6,