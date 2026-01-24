import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c', 'd']), 3)

    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), ['a', 'b', 'c', 'd']), 0)

    def test_empty_list(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), []), 0)

    def test_all_occurrences(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c']), 3)

    def test_no_occurrences(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['d', 'e', 'f']), 0)

    def test_duplicate_elements(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'b'), ['a', 'b']), 3)

    def test_case_sensitivity(self):
        self.assertEqual(count_Occurrence(('a', 'A'), ['a', 'A']), 2)
