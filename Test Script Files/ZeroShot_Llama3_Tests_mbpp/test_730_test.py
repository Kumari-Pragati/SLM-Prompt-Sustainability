import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(consecutive_duplicates([]), [])
