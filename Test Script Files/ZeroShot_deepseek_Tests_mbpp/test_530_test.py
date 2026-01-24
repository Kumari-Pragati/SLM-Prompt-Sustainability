import unittest
from mbpp_530_code import array
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_negative_count(self):
        # Test with a list of positive and negative numbers
        nums = array('i', [1, -2, 3, -4, 5, -6])
        self.assertEqual(negative_count(nums), 0.42)

        # Test with a list of only positive numbers
        nums = array('i', [1, 2, 3, 4, 5])
        self.assertEqual(negative_count(nums), 0.0)

        # Test with a list of only negative numbers
        nums = array('i', [-1, -2, -3, -4, -5])
        self.assertEqual(negative_count(nums), 1.0)

        # Test with an empty list
        nums = array('i', [])
        self.assertEqual(negative_count(nums), 0.0)

        # Test with a list of zeros
        nums = array('i', [0, 0, 0, 0, 0])
        self.assertEqual(negative_count(nums), 0.0)
