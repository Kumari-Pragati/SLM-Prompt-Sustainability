import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_empty_lists(self):
        """Test finding minimum sum with empty lists"""
        self.assertEqual(find_Min_Sum([], [], 0), 0)

    def test_single_element_lists(self):
        """Test finding minimum sum with single-element lists"""
        self.assertEqual(find_Min_Sum([1], [1], 1), 0)
        self.assertEqual(find_Min_Sum([1], [2], 1), 1)

    def test_same_lists(self):
        """Test finding minimum sum with same lists"""
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 3), 0)

    def test_different_lengths(self):
        """Test finding minimum sum with lists of different lengths"""
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2], 2), 1)
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3, 4], 3), 4)

    def test_negative_numbers(self):
        """Test finding minimum sum with negative numbers"""
        self.assertEqual(find_Min_Sum([-1, 2, -3], [-4, -2, 3], 3), 9)

    def test_out_of_range_index(self):
        """Test handling out-of-range indices"""
        with self.assertRaises(IndexError):
            find_Min_Sum([1, 2, 3], [1, 2], 4)
