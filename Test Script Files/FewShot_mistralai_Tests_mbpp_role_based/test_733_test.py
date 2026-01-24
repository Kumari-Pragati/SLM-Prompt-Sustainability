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

    def test_found_at_beginning(self):
        self.assertEqual(find_first_occurrence([1, 2, 1], 1), 0)

    def test_found_in_middle(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 1], 1), 2)

    def test_found_at_end(self):
        self.assertEqual(find_first_occurrence([1, 2, 3], 3), 2)
