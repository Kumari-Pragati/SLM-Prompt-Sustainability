import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 7)

    def test_edge_case_empty_input(self):
        with self.assertRaises(IndexError):
            max_of_nth([], 1)

    def test_edge_case_single_sublist(self):
        self.assertEqual(max_of_nth([[1, 2, 3]], 1), 3)

    def test_edge_case_max_value(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 9)

    def test_edge_case_min_value(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 5)

    def test_edge_case_invalid_nth(self):
        with self.assertRaises(IndexError):
            max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10)

    def test_edge_case_sublist_with_single_element(self):
        self.assertEqual(max_of_nth([[1], [2], [3]], 0), 1)

    def test_edge_case_sublist_with_single_element_at_nth(self):
        self.assertEqual(max_of_nth([[1], [2], [3]], 0), 1)
