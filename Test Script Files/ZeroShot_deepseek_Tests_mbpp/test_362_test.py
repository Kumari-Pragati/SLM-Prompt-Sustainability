import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_max_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), 1)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([]), None)
