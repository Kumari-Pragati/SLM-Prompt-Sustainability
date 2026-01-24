import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_empty_lists(self):
        """Check sum_list with empty lists"""
        self.assertListEqual(sum_list([], []), [])

    def test_single_element_lists(self):
        """Check sum_list with lists containing a single element"""
        self.assertListEqual(sum_list([1], [2]), [3])
        self.assertListEqual(sum_list([2], [1]), [3])
        self.assertListEqual(sum_list([-1], [-2]), [1])
        self.assertListEqual(sum_list([-2], [-1]), [1])

    def test_lists_of_different_lengths(self):
        """Check sum_list with lists of different lengths"""
        self.assertListEqual(sum_list([1, 2], [3, 4]), [4, 6])
        self.assertListEqual(sum_list([1, 2], [3]), [4, 5])
        self.assertListEqual(sum_list([1], [3, 4]), [4, 5])

    def test_lists_with_negative_numbers(self):
        """Check sum_list with lists containing negative numbers"""
        self.assertListEqual(sum_list([-1, 2], [-3, 4]), [1, -1])
        self.assertListEqual(sum_list([-1, 2], [-3]), [-4, 1])
        self.assertListEqual(sum_list([-1], [-3]), [-4])

    def test_lists_with_zero(self):
        """Check sum_list with lists containing zero"""
        self.assertListEqual(sum_list([0, 2], [3, 0]), [2, 3])
        self.assertListEqual(sum_list([0, 2], [3]), [2, 3])
        self.assertListEqual(sum_list([0], [3]), [3])

    def test_list_with_non_numeric_value(self):
        """Check sum_list with lists containing non-numeric values"""
        with self.assertRaises(TypeError):
            sum_list([1, 'a'], [2, 'b'])
