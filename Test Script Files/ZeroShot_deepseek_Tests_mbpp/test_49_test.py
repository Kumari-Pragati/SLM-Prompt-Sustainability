import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_specified_element(self):
        # Test with a list of lists with different lengths
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(specified_element(nums, N), [2, 5, 8])

        # Test with a list of lists with same lengths
        nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        N = 2
        self.assertEqual(specified_element(nums, N), [3, 7, 11])

        # Test with a list of lists with empty lists
        nums = [[], [], []]
        N = 0
        self.assertEqual(specified_element(nums, N), [])

        # Test with a list of lists with negative indices
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        self.assertEqual(specified_element(nums, N), [3, 6, 9])

        # Test with a list of lists with out of range indices
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertRaises(IndexError, specified_element, nums, N)
