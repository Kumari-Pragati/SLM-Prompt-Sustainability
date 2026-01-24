import unittest
from mbpp_10_code import small_nnum  # replace 'your_module' with the actual name of your module

class TestSmallNnum(unittest.TestCase):

    def test_small_nnum(self):
        # Test with a list of positive integers
        self.assertEqual(small_nnum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3), [1, 1, 2])

        # Test with a list of negative integers
        self.assertEqual(small_nnum([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5], 3), [-9, -6, -5])

        # Test with a list of mixed positive and negative integers
        self.assertEqual(small_nnum([3, -1, 4, -1, 5, -9, 2, 6, -5, 3, 5], 3), [-9, -1, 2])

        # Test with a list of floats
        self.assertEqual(small_nnum([3.1, 1.2, 4.3, 1.4, 5.5, 9.6, 2.7, 6.8, 5.9, 3.1, 5.2], 3), [1.2, 1.4, 2.7])

        # Test with a list of mixed positive, negative and floats
        self.assertEqual(small_nnum([3.1, -1.2, 4.3, -1.4, 5.5, -9.6, 2.7, 6.8, -5.9, 3.1, 5.2], 3), [-9.6, -1.4, 2.7])

        # Test with a list of one element
        self.assertEqual(small_nnum([5], 1), [5])

        # Test with a list of duplicate elements
        self.assertEqual(small_nnum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4), [1, 1, 2, 3])

        # Test with n greater than the length of the list
        self.assertEqual(small_nnum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 11), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

        # Test with an empty list
        self.assertEqual(small_nnum([], 3), [])

        # Test with n equals to zero
        self.assertEqual(small_nnum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 0), [])
