import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_last_occurrence_in_list(self):
        self.assertEqual(find_last_occurrence([3, 3, 2, 3, 4], 3), 3)

    def test_last_occurrence_at_beginning(self):
        self.assertEqual(find_last_occurrence([3, 3], 3), 0)

    def test_last_occurrence_at_end(self):
        self.assertEqual(find_last_occurrence([3, 3], 3), 1)

    def test_last_occurrence_not_found(self):
        self.assertEqual(find_last_occurrence([3, 3, 2, 4], 5), -1)

    def test_empty_list(self):
        self.assertEqual(find_last_occurrence([], 3), -1)

    def test_single_element_list(self):
        self.assertEqual(find_last_occurrence([3], 3), 0)

    def test_negative_number(self):
        self.assertEqual(find_last_occurrence([-1, -2, -3], -3), 2)
