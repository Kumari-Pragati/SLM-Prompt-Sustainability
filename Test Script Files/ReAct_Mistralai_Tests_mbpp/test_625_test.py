import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_empty_list(self):
        """Test swapping in an empty list"""
        result = swap_List([])
        self.assertListEqual([], result)

    def test_single_element_list(self):
        """Test swapping in a list with one element"""
        result = swap_List([1])
        self.assertListEqual([1], result)

    def test_regular_list(self):
        """Test swapping in a regular list"""
        result = swap_List([1, 2, 3, 4])
        self.assertListEqual([4, 1, 2, 3], result)

    def test_list_with_duplicates(self):
        """Test swapping in a list with duplicates"""
        result = swap_List([1, 1, 2, 3])
        self.assertListEqual([3, 1, 1, 2], result)

    def test_list_with_negative_numbers(self):
        """Test swapping in a list with negative numbers"""
        result = swap_List([-1, 0, 1])
        self.assertListEqual([1, -1, 0], result)

    def test_list_with_floats(self):
        """Test swapping in a list with floats"""
        result = swap_List([1.0, 2.0, 3.0])
        self.assertListEqual([3.0, 1.0, 2.0], result)

    def test_list_with_strings(self):
        """Test swapping in a list with strings"""
        result = swap_List(["a", "b", "c"])
        self.assertListEqual(["c", "a", "b"], result)

    def test_list_with_mixed_types(self):
        """Test swapping in a list with mixed types"""
        result = swap_List([1, "a", 2.0])
        self.assertListEqual([2.0, 1, "a"], result)
