import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 2, 1], 2), 3)
        self.assertEqual(find_last_occurrence([1, 2, 3, 2, 1], 1), 4)
        self.assertEqual(find_last_occurrence([], 1), -1)
        self.assertEqual(find_last_occurrence([1], 1), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 2], 2), 2)
        self.assertEqual(find_last_occurrence([1, 2, 3], 2), -1)
        self.assertEqual(find_last_occurrence([2, 1], 2), 0)
        self.assertEqual(find_last_occurrence([2, 1], 1), 1)

    def test_complex(self):
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 1, 2, 1], 1), 5)
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 1, 2, 1], 2), 3)
