import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_first_occurrence([1, 2, 3], 2), 1)
        self.assertEqual(find_first_occurrence([3, 3, 3], 3), 0)
        self.assertEqual(find_first_occurrence([4, 5, 6], 3), -1)

    def test_edge_and_boundary(self):
        self.assertEqual(find_first_occurrence([], 1), -1)
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 1], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 3], 4), -1)

    def test_complex(self):
        self.assertEqual(find_first_occurrence([1, 3, 5, 7, 9], 5), 2)
        self.assertEqual(find_first_occurrence([1, 3, 5, 7, 9], 0), -1)
        self.assertEqual(find_first_occurrence([1, 3, 5, 7, 9], 8), -1)
        self.assertEqual(find_first_occurrence([1, 3, 5, 7, 9], 6), -1)
