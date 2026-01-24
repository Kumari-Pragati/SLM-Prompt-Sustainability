import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), []), 0)

    def test_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)

    def test_no_occurrence(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)

    def test_occurrence(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3]), 3)

    def test_occurrence_with_duplicates(self):
        self.assertEqual(count_Occurrence((1, 2, 2, 3), [1, 2, 2, 3]), 3)

    def test_occurrence_with_duplicates_and_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 2, 3), []), 0)

    def test_occurrence_with_duplicates_and_empty_tuple(self):
        self.assertEqual(count_Occurrence((), [1, 2, 2, 3]), 0)
