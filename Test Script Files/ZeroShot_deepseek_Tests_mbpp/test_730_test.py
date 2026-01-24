import unittest
from mbpp_730_code import groupby

def consecutive_duplicates(nums):
    return [key for key, group in groupby(nums)]

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_no_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 3]), [1, 2, 3])

    def test_all_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 1]), [1])

    def test_mixed_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])
