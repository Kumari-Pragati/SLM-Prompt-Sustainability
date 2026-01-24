import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1], 2), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_duplicates(self):
        self.assertEqual(find_first_occurrence([1, 1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([1, 1, 2, 3, 4, 5], 2), 3)

    def test_edge_cases(self):
        self.assertEqual(find_first_occurrence([1], 0), -1)
        self.assertEqual(find_first_occurrence([1, 2], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 3], 0), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3], 4), -1)
