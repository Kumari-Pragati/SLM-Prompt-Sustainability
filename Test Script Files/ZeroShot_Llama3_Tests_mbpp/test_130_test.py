import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_max_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), (4, 4))
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), (4, 4))
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]), (4, 4))
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), (1, 1))
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), (1, 5))
        self.assertEqual(max_occurrences([]), None)
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_max_occurrences_empty_list(self):
        self.assertEqual(max_occurrences([]), None)
