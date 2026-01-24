import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns an empty list"""
        self.assertListEqual(heap_assending([]), [])

    def test_single_element(self):
        """Test that a list with one element returns that element"""
        self.assertListEqual(heap_assending([4]), [4])

    def test_multiple_elements(self):
        """Test that a list with multiple elements returns them in sorted order"""
        self.assertListEqual(heap_assending([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        """Test that a list with negative numbers returns them in sorted order"""
        self.assertListEqual(heap_assending([-5, -3, -1, -4, -2]), [-5, -4, -3, -2, -1])

    def test_duplicates(self):
        """Test that a list with duplicates returns them in sorted order"""
        self.assertListEqual(heap_assending([2, 2, 1, 3, 2]), [1, 2, 2, 3])

    def test_large_numbers(self):
        """Test that a list with large numbers returns them in sorted order"""
        self.assertListEqual(heap_assending([1000000, 999999, 1, 2, 3]), [1, 2, 3, 999999, 1000000])

    def test_floats(self):
        """Test that a list with floats returns them in sorted order"""
        self.assertListEqual(heap_assending([3.14, 2.71, 1.618, 0.0]), [0.0, 1.618, 2.71, 3.14])

    def test_list_modification(self):
        """Test that modifying the list during the heapify process does not affect the result"""
        nums = [5, 3, 1, 4, 2]
        heap_assending(nums)
        nums[0] = 100
        self.assertListEqual(heap_assending(nums), [1, 2, 3, 4])
