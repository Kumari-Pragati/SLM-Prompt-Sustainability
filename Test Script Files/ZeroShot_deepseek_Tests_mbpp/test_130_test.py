import unittest
from mbpp_130_code import defaultdict
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_max_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), (1, 2))
        self.assertEqual(max_occurrences([1]), (1, 1))
        self.assertEqual(max_occurrences([]), None)
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), (4, 4))
