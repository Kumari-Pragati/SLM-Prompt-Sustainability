import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 3)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            max_of_nth([], 0)

    def test_edge_case_single_sublist(self):
        self.assertEqual(max_of_nth([[1, 2, 3]], 0), 1)

    def test_edge_case_single_sublist_with_zero(self):
        self.assertEqual(max_of_nth([[1, 2, 3]], 2), 3)

    def test_edge_case_single_sublist_with_negative(self):
        with self.assertRaises(IndexError):
            max_of_nth([[1, 2, 3]], -1)

    def test_edge_case_sublist_with_zero(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 0]], 2), 8)

    def test_edge_case_sublist_with_negative(self):
        with self.assertRaises(IndexError):
            max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, -1]], 2)

    def test_edge_case_sublist_with_non_numeric(self):
        with self.assertRaises(TypeError):
            max_of_nth([[1, 2, 3], [4, 5, 'a'], [7, 8, 9]], 1)
