import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_last_occurrence([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1], 2), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 3], 1), 4)
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 3], 2), 2)
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 3], 3), 4)

    def test_duplicates_at_beginning(self):
        self.assertEqual(find_last_occurrence([1, 1, 2, 1], 1), 3)

    def test_duplicates_at_end(self):
        self.assertEqual(find_last_occurrence([1, 2, 1], 1), 2)

    def test_duplicates_in_middle(self):
        self.assertEqual(find_last_occurrence([1, 2, 1, 2, 1], 1), 4)

    def test_not_found(self):
        self.assertEqual(find_last_occurrence([1, 2, 3], 4), -1)
