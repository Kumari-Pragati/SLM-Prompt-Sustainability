import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 2, 1], 2), 3)
        self.assertEqual(find_last_occurrence([1, 1, 1, 1], 1), 3)
        self.assertEqual(find_last_occurrence([], 0), -1)
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1, 1], 1), 1)

    def test_edge_cases(self):
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 3], 2), 3)
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 1], 2), 1)
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 1], 1), 4)
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 1], 3), -1)

    def test_boundary_cases(self):
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 1], 0), -1)
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 1], 2, 0), -1)
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 1], 2, len(A) + 1), -1)
