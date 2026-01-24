import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 2]), 2)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_occurrences([5, 5, 5, 5, 5]), 5)

    def test_edge_cases(self):
        self.assertEqual(max_occurrences([]), None)
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1]), 1)

    def test_boundary_conditions(self):
        self.assertEqual(max_occurrences([-10, -10, -10, 0, 0, 0]), -10)
        self.assertEqual(max_occurrences([2147483647, 2147483647, 2147483647, 0, 0, 0]), 2147483647)

    def test_complex_cases(self):
        self.assertEqual(max_occurrences([1, 2, 1, 2, 1, 2, 3, 2, 1]), 2)
        self.assertEqual(max_occurrences([0, 0, 1, 0, 0, 1, 0, 0, 1]), 1)
