import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4), 2), 2)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_tuplex((), 5), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_tuplex((5,), 5), 1)

    def test_edge_case_tuple_with_single_element(self):
        self.assertEqual(count_tuplex((1, 2, 3, 4, 5), 5), 1)

    def test_edge_case_tuple_with_no_occurrences(self):
        self.assertEqual(count_tuplex((1, 2, 3, 4), 5), 0)

    def test_edge_case_tuple_with_all_occurrences(self):
        self.assertEqual(count_tuplex((1, 1, 1, 1), 1), 4)

    def test_edge_case_tuple_with_duplicates(self):
        self.assertEqual(count_tuplex((1, 2, 2, 3, 3, 3), 3), 3)

    def test_edge_case_tuple_with_duplicates_and_non_duplicates(self):
        self.assertEqual(count_tuplex((1, 2, 2, 3, 3, 4), 2), 2)
