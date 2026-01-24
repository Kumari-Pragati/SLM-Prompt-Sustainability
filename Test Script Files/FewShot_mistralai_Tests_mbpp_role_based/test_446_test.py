import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3, 4]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_Occurrence((1, 2, 3), []), 0)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_Occurrence((), [1, 2, 3]), 0)

    def test_edge_case_single_item_tuple(self):
        self.assertEqual(count_Occurrence((1,), [1]), 1)

    def test_edge_case_single_item_list(self):
        self.assertEqual(count_Occurrence((1,), [1]), 0)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(count_Occurrence((-1, 0, 1), [-1, 0, 1]), 1)

    def test_boundary_case_duplicate_items(self):
        self.assertEqual(count_Occurrence((1, 1, 2), [1, 1, 2]), 2)
