import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):
    def test_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])
        self.assertEqual(consecutive_duplicates([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10])
        self.assertEqual(consecutive_duplicates([]), [])
        self.assertEqual(consecutive_duplicates([1]), [1])
        self.assertEqual(consecutive_duplicates([1, 2]), [1, 2])
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])
