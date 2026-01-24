import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_max_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 3, 3, 3]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9