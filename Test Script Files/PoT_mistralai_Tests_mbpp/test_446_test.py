import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3, 4]), 3)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c', 'd']), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_Occurrence((), [1, 2, 3]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_Occurrence((1,), [1]), 1)
        self.assertEqual(count_Occurrence(('a',), ['a']), 1)

    def test_edge_case_non_matching_element(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['d', 'e', 'f']), 0)
