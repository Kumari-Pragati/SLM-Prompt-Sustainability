import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 2]), 2)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_occurrences([-1, -1, -1, 0, 0, 0]), -1)

    def test_edge_cases(self):
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([]), None)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1]), 1)

    def test_boundary_cases(self):
        self.assertEqual(max_occurrences([sys.maxsize, sys.maxsize, sys.maxsize]), sys.maxsize)
        self.assertEqual(max_occurrences([-sys.maxsize, -sys.maxsize, -sys.maxsize]), -sys.maxsize)
