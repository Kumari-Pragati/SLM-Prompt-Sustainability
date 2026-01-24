import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_last_occurrence([], 10), -1)

    def test_single_element_list(self):
        self.assertEqual(find_last_occurrence([5], 5), 0)
        self.assertEqual(find_last_occurrence([5], 10), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 4, 5, 6], 3), 3)
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 4, 5, 6], 10), -1)
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 4, 5, 6], 1), 0)
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 4, 5, 6], 6), 6)

    def test_duplicate_elements(self):
        self.assertEqual(find_last_occurrence([1, 2, 2, 3, 4, 5, 6], 2), 3)
        self.assertEqual(find_last_occurrence([1, 2, 2, 3, 4, 5, 6], 10), -1)
