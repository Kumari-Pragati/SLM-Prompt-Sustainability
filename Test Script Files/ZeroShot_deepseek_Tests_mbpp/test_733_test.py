import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_no_occurrence(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_single_occurrence(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(find_first_occurrence([1, 2, 2, 3, 4, 5], 2), 1)

    def test_first_occurrence(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5, 5, 6], 5), 4)
