import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_empty_list(self):
        """Test swapping in an empty list"""
        self.assertEqual(swap_List([]), [])

    def test_single_element_list(self):
        """Test swapping in a list with one element"""
        self.assertEqual(swap_List([1]), [1])

    def test_regular_list(self):
        """Test swapping in a regular list"""
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 1, 2, 3])

    def test_list_with_duplicates(self):
        """Test swapping in a list with duplicates"""
        self.assertEqual(swap_List([1, 2, 2, 3, 4]), [4, 1, 2, 2, 3])

    def test_negative_index(self):
        """Test swapping with negative index"""
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_out_of_range_index(self):
        """Test swapping with out-of-range index"""
        self.assertEqual(swap_List([1, 2, 3]), [1, 3, 2])

    def test_list_with_non_integer_elements(self):
        """Test swapping with a list containing non-integer elements"""
        self.assertRaises(TypeError, swap_List, ['a', 1, 'b'])
