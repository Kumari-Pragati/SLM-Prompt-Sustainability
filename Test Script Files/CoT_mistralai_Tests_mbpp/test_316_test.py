import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_last_occurrence([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1], 0), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_last_occurrence([1, 2, 1, 3, 1], 1), 4)
        self.assertEqual(find_last_occurrence([1, 2, 1, 3, 1], 2), -1)
        self.assertEqual(find_last_occurrence([1, 2, 1, 3, 1], 3), 3)

    def test_duplicates(self):
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 2, 1], 1), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_last_occurrence([-1, -2, -1, -3, -1], -1), 4)
        self.assertEqual(find_last_occurrence([-1, -2, -1, -3, -1], -2), -1)
        self.assertEqual(find_last_occurrence([-1, -2, -1, -3, -1], -3), 3)

    def test_edge_cases(self):
        self.assertEqual(find_last_occurrence([1], 0), -1)
        self.assertEqual(find_last_occurrence([1], len(list(range(100000)))), -1)
        self.assertEqual(find_last_occurrence([1] * 100000, 1), 99999)
