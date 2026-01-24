import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), []), 0)

    def test_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)

    def test_no_occurrences(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)

    def test_single_occurrence(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 4, 5]), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3, 4, 5]), 3)

    def test_duplicates_in_tuple(self):
        self.assertEqual(count_Occurrence((1, 1, 2, 2, 3), [1, 2, 3]), 3)

    def test_duplicates_in_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 1, 2, 2, 3]), 3)

    def test_duplicates_in_both(self):
        self.assertEqual(count_Occurrence((1, 1, 2, 2, 3), [1, 1, 2, 2, 3]), 4)
