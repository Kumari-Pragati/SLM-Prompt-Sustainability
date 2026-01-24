import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3]), 3)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c']), 3)

    def test_empty_tuples(self):
        self.assertEqual(count_Occurrence((), [1, 2, 3]), 0)
        self.assertEqual(count_Occurrence((), []), 0)

    def test_empty_lists(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)
        self.assertEqual(count_Occurrence([], [1, 2, 3]), 0)

    def test_no_occurrence(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['d', 'e', 'f']), 0)

    def test_duplicates_in_tuples(self):
        self.assertEqual(count_Occurrence((1, 2, 2), [2]), 2)
        self.assertEqual(count_Occurrence(('a', 'b', 'b'), ['b']), 2)

    def test_duplicates_in_lists(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [2, 2]), 2)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['b', 'b']), 2)

    def test_mixed_types(self):
        self.assertEqual(count_Occurrence((1, 'a', 2), [1, 'a']), 2)
        self.assertEqual(count_Occurrence(('a', 1, 'b'), ['a', 1]), 2)
