import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_typical_case(self):
        # Typical case: list of lists with valid indices
        input_tuplex = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_output = [
            [1, 2, 3],
            [4, 5, 6, 10],  # New value at (1, 2)
            [7, 8, 9]
        ]
        self.assertEqual(colon_tuplex(input_tuplex, 1, 2), expected_output)

    def test_edge_case_negative_index(self):
        # Edge case: negative index
        input_tuplex = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        with self.assertRaises(IndexError):
            colon_tuplex(input_tuplex, -1, 2)

    def test_edge_case_out_of_range_index(self):
        # Edge case: index out of range
        input_tuplex = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        with self.assertRaises(IndexError):
            colon_tuplex(input_tuplex, 3, 2)

    def test_edge_case_empty_list(self):
        # Edge case: empty list
        input_tuplex = []
        with self.assertRaises(TypeError):
            colon_tuplex(input_tuplex, 1, 2)

    def test_edge_case_non_list(self):
        # Edge case: non-list input
        input_tuplex = "Not a list"
        with self.assertRaises(TypeError):
            colon_tuplex(input_tuplex, 1, 2)
