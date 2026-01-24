import unittest
from mbpp_730_code import groupby

def consecutive_duplicates(nums):
    return [key for key, group in groupby(nums)]

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_single_duplicate(self):
        self.assertEqual(consecutive_duplicates([1, 1]), [1])

    def test_multiple_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5]), [1, 2, 3, 4])

    def test_consecutive_numbers(self):
        self.assertEqual(consecutive_duplicates(range(1, 6)), [1, 2, 3])

    def test_consecutive_duplicates_with_gaps(self):
        self.assertEqual(consecutive_duplicates([1, 2, 1, 2, 3, 2, 3]), [1, 2])

    def test_non_consecutive_numbers(self):
        self.assertEqual(consecutive_duplicates([3, 2, 1, 2, 3, 4]), [3, 2])
