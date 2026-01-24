import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 1]), 2)
    def test_empty_list(self):
        self.assertIsNone(max_occurrences([]))
    def test_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)
    def test_all_same(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)
    def test_max_occurrence_at_end(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)
    def test_max_occurrence_at_start(self):
        self.assertEqual(max_occurrences([5, 4, 3, 2, 1]), 5)
    def test_max_occurrence_at_middle(self):
        self.assertEqual(max_occurrences([1, 2, 3, 3, 4]), 3)
    def test_max_occurrence_at_start_and_end(self):
        self.assertEqual(max_occurrences([1, 2, 3, 3, 1]), 3)
