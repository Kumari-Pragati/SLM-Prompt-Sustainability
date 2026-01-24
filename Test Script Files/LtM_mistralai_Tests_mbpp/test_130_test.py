import unittest
from mbpp_130_code import defaultdict
from 130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), (4, 4))
        self.assertEqual(max_occurrences([5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9]), (8, 8))

    def test_edge_cases(self):
        self.assertEqual(max_occurrences([]), (None, None))
        self.assertEqual(max_occurrences([1]), (1, 1))
        self.assertEqual(max_occurrences([1, 1, 1]), (1, 3))
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]), (4, 4))

    def test_complex(self):
        self.assertEqual(max_occurrences([1000000000, 1000000000, 1000000000]), (1000000000, 3))
        self.assertEqual(max_occurrences([-1, -1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3]), (3, 3))
