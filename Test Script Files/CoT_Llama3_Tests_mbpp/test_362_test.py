import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_max_occurrences_typical(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 1]), 1)

    def test_max_occurrences_edge(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)

    def test_max_occurrences_multiple_max(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3]), 2)

    def test_max_occurrences_empty_list(self):
        self.assertRaises(IndexError, max_occurrences, [])

    def test_max_occurrences_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_max_occurrences_all_unique(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_max_occurrences_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), 1)
