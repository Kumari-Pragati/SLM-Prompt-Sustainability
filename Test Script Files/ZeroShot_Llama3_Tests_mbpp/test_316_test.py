import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_find_last_occurrence(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_last_occurrence([], 5), -1)
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5, 5, 5, 5, 5, 5], 5), 9)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5, 5, 5, 5, 5, 5], 6), -1)
