import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurrence(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(get_odd_occurrence([1, 1, 2, 2, 3], 5), 1)
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5, 5], 6), 1)

    def test_empty_input(self):
        self.assertEqual(get_odd_occurrence([], 0), -1)

    def test_single_element(self):
        self.assertEqual(get_odd_occurrence([1], 1), 1)
        self.assertEqual(get_odd_occurrence([1, 1], 2), 1)

    def test_all_same(self):
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1], 5), 1)

    def test_all_unique(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5, 6], 6), 1)

    def test_max_size(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)

    def test_max_size_all_same(self):
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10), 1)
