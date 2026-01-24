import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3]), 3)

    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), [1, 2, 3]), 0)

    def test_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)

    def test_all_occurrences(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3]), 3)

    def test_no_occurrences(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)

    def test_duplicate_elements(self):
        self.assertEqual(count_Occurrence((1, 2, 2, 3), [2]), 2)

    def test_duplicate_in_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [2, 2]), 2)

    def test_large_inputs(self):
        large_tuple = tuple(range(1, 10001))
        large_list = list(range(1, 10001))
        self.assertEqual(count_Occurrence(large_tuple, large_list), 10000)
