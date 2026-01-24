import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1], 2), -1)

    def test_not_found(self):
        self.assertEqual(find_first_occurrence([1, 2, 3], 4), -1)

    def test_found(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 1], 1), 2)
        self.assertEqual(find_first_occurrence([1, 1, 2, 1, 3], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
